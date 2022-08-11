from fastapi import APIRouter, HTTPException
from fastapi import Depends, status
from schemas.schemas import UserSimpleModel
from schemas.schemas import UserModel
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorio.users import RepositorioUser
from infra.sqlalchemy.config.database import get_bd
from typing import List


router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserSimpleModel)
def create_user(user: UserModel, session: Session = Depends(get_bd)):
    new_user = RepositorioUser(session).create_user(user)
    return new_user


@router.get('/get_user', status_code=status.HTTP_200_OK, response_model=List[UserSimpleModel])
def get_users(session: Session = Depends(get_bd)):
    users = RepositorioUser(session).list_user()
    return users


@router.get('/{UUID}', status_code=status.HTTP_200_OK, response_model=UserSimpleModel)
def get_user_uuid(UUID: str, session: Session = Depends(get_bd)):
    get_uuid = RepositorioUser(session).get_uuid(UUID)
    if not get_uuid:
        raise HTTPException(
            status_code=404, detail=f'Não contem usuário cadastrado com o UUID {UUID}.')
    return get_uuid