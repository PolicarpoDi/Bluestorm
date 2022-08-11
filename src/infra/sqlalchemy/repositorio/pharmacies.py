from sqlalchemy.orm import Session
from infra.sqlalchemy.models.models import Transactions, Pharmacies, Patients

class RepositorioPharmacies():

    def __init__(self, session: Session):
        self.db = session

    def list_patients(self):
        patients = self.db.query(Patients).all()
        return patients
    
    def list_pharmacies(self):
        pharmacies = self.db.query(Pharmacies).all()
        return pharmacies

    def list_transactions(self):
        transactions = self.db.query(Transactions).all()
        return transactions
        