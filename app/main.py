from database import database, session
from typing import List
from fastapi import FastAPI

from model import PATIENTS, PHARMACIES, TRANSACTIONS
from schema import Patients, Pharmacies, Transactions


app = FastAPI()


# Informa quando conectar no banco
@app.on_event("startup")
async def startup():
    await database.connect()


# Informa quando desconectar no banco
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



app = FastAPI()

@app.get("/")
async def rota_root():
    return {"Messagem": "Bem vindo a API da Bruestorm"}


# /patients [GET] { .. }
@app.get("/patients/", response_model=List[Patients])
async def read_patients():
    return session.query(PATIENTS).all()


# /patients/UUID [GET] { .. }
@app.get("/patients/{UUID}")
async def read_uuid_patients(UUID):
    return session.query(PATIENTS).filter_by(UUID=UUID).all()


# /pharmacies [GET] { .. }
@app.get("/pharmacies/", response_model=List[Pharmacies])
async def read_pharmacies():
    return session.query(PHARMACIES).all()


# /pharmacies/UUID [GET] { .. }
@app.get("/pharmacies/{UUID}", response_model=List[Pharmacies])
async def read_pharmacies(UUID):
    return session.query(PHARMACIES).filter_by(UUID=UUID).all()


# /transaction [GET] { .. }
@app.get("/transactions/", response_model=List[Transactions])
async def read_transaction():
    return session.query(TRANSACTIONS).all()