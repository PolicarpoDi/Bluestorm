from datetime import date, datetime
from importlib.metadata import metadata
from multiprocessing.connection import wait
from sqlite3 import connect
from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI, Query
from pydantic import BaseModel


bd_bluestorm = "sqlite:////home/diegopolicarpo/Works/Projects/Pessoal/API_Bluestorm/app/db/backend_test.db"
# SQLAlchemy specific code, as with any other 
DATABASE_URL = bd_bluestorm
# DATABASE_URL = "postgresql://user:password@postgresserver/db"
 
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

PATIENTS = sqlalchemy.Table(
    "PATIENTS",
    metadata,
    sqlalchemy.Column("UUID", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("FIRST_NAME", sqlalchemy.String),
    sqlalchemy.Column("LAST_NAME", sqlalchemy.String),
    sqlalchemy.Column("DATE_OF_BIRTH", sqlalchemy.Date),
)

PHARMACIES = sqlalchemy.Table(
    "pharmacies",
    metadata,
    sqlalchemy.Column("UUID", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("NAME", sqlalchemy.String),
    sqlalchemy.Column("CITY", sqlalchemy.String),
)

TRANSACTIONS = sqlalchemy.Table(
    "transactions",
    metadata,
    sqlalchemy.Column("UUID", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("PATIENT_UUID", sqlalchemy.String),
    sqlalchemy.Column("PHARMACY_UUID", sqlalchemy.String),
    sqlalchemy.Column("AMOUNT", sqlalchemy.Integer),
    sqlalchemy.Column("TIMESTAMP", sqlalchemy.Date),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

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


app = FastAPI()


# Conecta no banco 
@app.on_event("startup")
async def startup():
    await database.connect()


# desconecta no banco 
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def rota_root():
    return {"Messagem": "Bem vindo a API da Bruestorm"}


# /patients [GET] { .. }
@app.get("/patients/", response_model=List[Patients])
async def read_patients():
    query = PATIENTS.select()
    return await database.fetch_all(query)


# /pharmacies [GET] { .. }
@app.get("/pharmacies/", response_model=List[Pharmacies])
async def read_pharmacies():
    query = PHARMACIES.select()
    return await database.fetch_all(query)


# /transaction [GET] { .. }
@app.get("/transactions/", response_model=List[Transactions])
async def read_transaction():
    query = TRANSACTIONS.select()
    return await database.fetch_all(query)