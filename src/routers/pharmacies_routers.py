from fastapi import APIRouter
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_bd
from infra.sqlalchemy.repositorio.pharmacies import RepositorioPharmacies


router = APIRouter()


@router.get("/patients", status_code=status.HTTP_200_OK)
def get_patients(session: Session = Depends(get_bd)):
    patients = RepositorioPharmacies(session).list_patients()
    return patients

@router.get("/pharmacies", status_code=status.HTTP_200_OK)
def get_pharmacies(session: Session = Depends(get_bd)):
    pharmacies = RepositorioPharmacies(session).list_pharmacies()
    return pharmacies
    

@router.get("/transactions", status_code=status.HTTP_200_OK)
def get_transactions(session: Session = Depends(get_bd)):
    transaction = RepositorioPharmacies(session).list_transactions()
    return transaction