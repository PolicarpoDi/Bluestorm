from sqlalchemy.orm import Session
from schema.schemas import Patients, Pharmacies, Transactions, User
from model.models import UserModel


# Create User
def create_user(user: UserModel, db: Session):
    db_users = User(UUID=user.UUID ,USERNAME=user.USERNAME, PASSWORD=user.PASSWORD)
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users.to_dict()
    

# Search all patients
def get_users(db: Session):
    users = db.query(User).all()
    dict = []
    for user in users:
        dict.append(user.to_dict())
    return dict


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


