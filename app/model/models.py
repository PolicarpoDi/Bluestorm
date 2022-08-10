from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    UUID: str
    USERNAME: str
    PASSWORD: str
    class config(BaseModel):
        orm_mode = True

class PatientsModel(BaseModel):
    UUID: str
    FIRST_NAME: str
    LAST_NAME: str
    DATE_OF_BIRTH: date
    class config(BaseModel):
        orm_mode = True

class PharmaciesModel(BaseModel):
    UUID: str
    UUID: str
    NAME: str
    CITY: str
    class config(BaseModel):
        orm_mode = True

class TransactionsModel(BaseModel):
    UUID: str
    PATIENT_UUID: str
    PHARMACY_UUID: str
    AMOUNT: float
    TIMESTAMP: date
    class config(BaseModel):
        orm_mode = True