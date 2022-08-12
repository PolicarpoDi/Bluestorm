from infra.sqlalchemy.repositorio.users import RepositorioUser
from infra.sqlalchemy.config.database import get_bd
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from infra.providers import token_provider
from sqlalchemy.orm import Session
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_logged_in_user(token: str = Depends(oauth2_schema), session: Session = Depends(get_bd)):
    # decodificar o token, pegar o telefone, buscar usuário no bd e retornar
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido.')

    try:
        uuid = token_provider.verify_acess_token(token)
    except JWTError:
        raise exception

    if not uuid:
        raise exception

    user = RepositorioUser(session).get_user_uuid(uuid)

    if not user:
        raise exception

    return user 
