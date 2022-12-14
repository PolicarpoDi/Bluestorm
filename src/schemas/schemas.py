from datetime import date, datetime
from pydantic import BaseModel

class Base(BaseModel):
    class Config:
        orm_mode = True

class UserModel(Base):
    UUID: str
    USERNAME: str
    PASSWORD: str

class UserSimpleModel(Base):
    UUID: str
    USERNAME: str

class LoginData(Base):
    UUID: str
    PASSWORD: str

class LoginSucces(Base):
    USER: UserSimpleModel
    ACCESS_TOKEN: str

class PatientsModel(Base):
    UUID: str
    FIRST_NAME: str
    LAST_NAME: str
    DATE_OF_BIRTH: date

class PharmaciesModel(Base):
    UUID: str
    NAME: str
    CITY: str

class TransactionsModel(Base):
    UUID: str
    AMOUNT: float
    TIMESTAMP: datetime