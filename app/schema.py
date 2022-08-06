from datetime import date
from pydantic import BaseModel


class Patients(BaseModel):
    UUID: str
    FIRST_NAME: str
    LAST_NAME: str
    DATE_OF_BIRTH: date


class Pharmacies(BaseModel):
    UUID: str
    NAME: str
    CITY: str


class Transactions(BaseModel):
    UUID: str
    PATIENT_UUID: str
    PHARMACY_UUID: str
    AMOUNT: int
    TIMESTAMP: date