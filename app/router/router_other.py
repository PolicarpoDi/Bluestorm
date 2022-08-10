from fastapi.responses import JSONResponse
from model.models import PatientsModel, PharmaciesModel, TransactionsModel
from controller.crud import get_patient, get_pharmacies, get_transactions
from fastapi import Depends, status, APIRouter
from connection.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()
    

# /patients [GET] { .. }
@router.get("/patients/", status_code=status.HTTP_200_OK, response_model=List[PatientsModel])
def read_patients(db: Session = Depends(get_db)):
    patients = get_patient(db)
    return JSONResponse(content=patients)


# /pharmacies [GET] { .. }
@router.get("/pharmacies/", status_code=status.HTTP_200_OK, response_model=List[PharmaciesModel])
def read_pharmacies(db: Session = Depends(get_db)):
    pharmacies = get_pharmacies(db)
    return JSONResponse(content=pharmacies)


# /Transactions [GET] { .. }
@router.get("/transactions/", status_code=status.HTTP_200_OK, response_model=List[TransactionsModel])
def red_transaction_one(db: Session = Depends(get_db)):
    transaction = get_transactions(db)
    return JSONResponse(content=transaction)