from datetime import datetime, timedelta
from secrets import token_bytes
from jose import jwt


# Config
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def create_acess_token(data: dict):
    datas = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'exp': expire})

    token_jwt = jwt.encode(datas, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_acess_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')