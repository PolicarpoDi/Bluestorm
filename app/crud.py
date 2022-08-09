from sqlalchemy.orm import Session
from schemas import Patients, Pharmacies, Transactions


# Search all patients
def get_patient(db: Session):
    patients = db.query(Patients).all()
    dict = []
    for pacient in patients:
        dict.append(pacient.to_dict())
    return dict


# Search all pharmacies 
def get_pharmacies(db: Session):
    pharmacies = db.query(Pharmacies).all()
    dict = []
    for pharmacy in pharmacies:
        dict.append(pharmacy.to_dict())
    return dict


# Search all transactions
def get_transactions(db: Session):
    transactions = db.query(Transactions).all()
    dict = []
    for transaction in transactions:
        dict.append(transaction.to_dict())
    return dict


