
from infra.sqlalchemy.repositorio.pharmacies import RepositorioPharmacies
from infra.sqlalchemy.config.database import get_bd
from routers.utils import get_logged_in_user
from fastapi import Depends, status
from sqlalchemy.orm import Session
from fastapi import APIRouter


router = APIRouter()

@router.get("/patient/", status_code=status.HTTP_200_OK)
def get_patients(user = Depends(get_logged_in_user), session: Session = Depends(get_bd)):
    patient = RepositorioPharmacies(session).list_patient()
    return patient


@router.get("/pharmacie/", status_code=status.HTTP_200_OK)
def get_pharmacies(user = Depends(get_logged_in_user), session: Session = Depends(get_bd)):
    pharmacies = RepositorioPharmacies(session).list_pharmacie()
    return pharmacies
    

@router.get("/transaction/{UUID}", status_code=status.HTTP_200_OK)
def get_transactions(UUID: str, user = Depends(get_logged_in_user), session: Session = Depends(get_bd)):
    transact = RepositorioPharmacies(session).list_transaction(UUID)
    return transact
   