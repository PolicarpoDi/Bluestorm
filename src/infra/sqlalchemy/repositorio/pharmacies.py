from infra.sqlalchemy.models.models import Transactions, Pharmacies, Patients
from sqlalchemy.orm import Session
from sqlalchemy import select


class RepositorioPharmacies():

    def __init__(self, session: Session):
        self.db = session


    def list_patient(self):
        query = select(Patients)
        patient = self.db.execute(query).all()
        return patient

    
    def list_pharmacie(self):
        query = select(Pharmacies)
        uuid_pharmacy = self.db.execute(query).all()
        return uuid_pharmacy


    def list_transaction(self, UUID: str):
        query = select(Patients, Pharmacies,Transactions).where(Transactions.UUID == UUID)
        transaction_uuid = self.db.execute(query).all()
        return transaction_uuid
        