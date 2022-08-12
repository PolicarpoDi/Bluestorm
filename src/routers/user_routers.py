from fastapi import APIRouter, HTTPException, Depends, status
from schemas.schemas import UserSimpleModel, UserModel, LoginData
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorio.users import RepositorioUser
from infra.sqlalchemy.config.database import get_bd
from typing import List
from infra.providers.hash_provider import generete_hash, verify_hash


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


@router.get('/{UUID}', status_code=status.HTTP_200_OK, response_model=UserSimpleModel)
def get_user_uuid(UUID: str, session: Session = Depends(get_bd)):
    get_uuid = RepositorioUser(session).get_user_uuid(UUID)
    if not get_uuid:
        raise HTTPException(
            status_code=404, detail=f'Não contem usuário cadastrado com o UUID {UUID}.')
    return get_uuid


@router.post('/token')
def login(login_data: LoginData, session: Session = Depends(get_bd)):
    uuid = login_data.UUID
    pwd = login_data.PASSWORD

    get_uuid = RepositorioUser(session).get_user_uuid(uuid)

    if not get_uuid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='UUID ou senha incorreto')

    pwd_valid = verify_hash(pwd, get_uuid.PASSWORD)
    if not pwd_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='UUID ou senha incorreto')

    return get_uuid