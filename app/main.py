from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from database import SessionLocal
from models import PatientsModel, PharmaciesModel, TransactionsModel
from crud import get_patient, get_pharmacies, get_transactions
from fastapi.responses import JSONResponse


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Initial Route
@app.get("/")
async def rota_root():
    return {"Messagem": "Bem vindo a API da Bruestorm"}


# /patients [GET] { .. }
@app.get("/patients/", response_model=List[PatientsModel])
def read_patients(db: Session = Depends(get_db)):
    patients = get_patient(db)
    return JSONResponse(content=patients)


# /pharmacies [GET] { .. }
@app.get("/pharmacies/", response_model=List[PharmaciesModel])
def read_pharmacies(db: Session = Depends(get_db)):
    pharmacies = get_pharmacies(db)
    return JSONResponse(content=pharmacies)


# /Transactions [GET] { .. }
@app.get("/transactions/", response_model=List[TransactionsModel])
def red_transaction_one(db: Session = Depends(get_db)):
    transaction = get_transactions(db)
    return JSONResponse(content=transaction)
