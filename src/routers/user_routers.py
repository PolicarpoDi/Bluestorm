from schemas.schemas import LoginSucces, UserSimpleModel, UserModel, LoginData
from infra.providers.hash_provider import generete_hash, verify_hash
from infra.sqlalchemy.repositorio.users import RepositorioUser
from fastapi import APIRouter, HTTPException, Depends, status
from infra.providers.token_provider import create_acess_token
from infra.sqlalchemy.config.database import get_bd
from infra.sqlalchemy.models.models import User
from routers.utils import get_logged_in_user
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserSimpleModel)
def create_user(user: UserModel, session: Session = Depends(get_bd)):
    get_user = RepositorioUser(session).get_user_uuid(user.UUID)
    if get_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe um usuário para esse UUID')

    user.PASSWORD = generete_hash(user.PASSWORD)
    new_user = RepositorioUser(session).create_user(user)
    return new_user


@router.get('/get_user', status_code=status.HTTP_200_OK, response_model=List[UserSimpleModel])
def get_users(session: Session = Depends(get_bd)):
    users = RepositorioUser(session).list_user()
    return users


@router.get('/get/{UUID}', status_code=status.HTTP_200_OK, response_model=UserSimpleModel)
def get_user_uuid(UUID: str, session: Session = Depends(get_bd)):
    get_u_uuid = RepositorioUser(session).get_user_uuid(UUID)
    if not get_u_uuid:
        raise HTTPException(
            status_code=404, detail=f'Não contem usuário cadastrado com o UUID {UUID}.')
    return get_u_uuid


@router.post('/token')
def login(login_data: LoginData, session: Session = Depends(get_bd)):
    uuid = login_data.UUID
    pwd = login_data.PASSWORD
    
    get_uuid = RepositorioUser(session).get_user_uuid(uuid)
    if not get_uuid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='UUID ou senha incorreto')
    pwd_valid = verify_hash(pwd, get_uuid.PASSWORD)

    if not pwd_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='UUID ou senha incorreto')

    # Gerar Token JWT
    token = create_acess_token({'sub': get_uuid.UUID})
    return LoginSucces(USER=get_uuid, ACCESS_TOKEN=token)


@router.get('/me', response_model=UserSimpleModel)
def me(user: User = Depends(get_logged_in_user)):
    return user
