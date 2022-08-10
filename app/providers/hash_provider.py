# Método para gerar Hash
import bcrypt
from passlib.context import CryptContext

pwd = CryptContext(schemes=bcrypt)

def create_hash(text):
    return pwd.hash(text)


def verify_hash(text, hash):
    return pwd.verify(text, hash)