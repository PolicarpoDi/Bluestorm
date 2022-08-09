from sqlalchemy import DateTime, ForeignKey, Column, String, Date, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Patients(Base):
    __tablename__ = "PATIENTS"

    UUID = Column(String, primary_key=True)
    FIRST_NAME = Column(String, index=True)
    LAST_NAME = Column(String, index=True)
    DATE_OF_BIRTH = Column(Date, index=True)

    def to_dict(self):
        return {"UUID": self.UUID,
                "FIST_NAME": self.FIRST_NAME,
                "LAST_NAME": self.LAST_NAME,
                "DATE_OF_BIRTH": str(self.DATE_OF_BIRTH)}


class Pharmacies(Base):
    __tablename__ = "PHARMACIES"

    UUID = Column(String, primary_key=True, index=True)
    NAME = Column(String, index=True)
    CITY = Column(String, index=True)

    def to_dict(self):
        return {"UUID": self.UUID,
                "NAME": self.NAME,
                "CITY": self.CITY}


class Transactions(Base):
    __tablename__ = "TRANSACTIONS"

    UUID = Column(String, primary_key=True, index=True)
    PATIENT_UUID = Column(String, ForeignKey("PATIENTS.UUID"))
    PHARMACY_UUID = Column(String, ForeignKey("PHARMACIES.UUID"))
    AMOUNT = Column(Float, index=True)
    TIMESTAMP = Column(DateTime, index=True)
    PATIENTS = relationship("Patients")
    PHARMACY = relationship("Pharmacies")

    def to_dict(self):
        return {"FIRST_NAME": self.PATIENTS.FIRST_NAME,
                "LAST_NAME": self.PATIENTS.LAST_NAME,
                "DATE_OF_BIRTH": str(self.PATIENTS.DATE_OF_BIRTH),
                "NAME": self.PHARMACY.NAME,
                "CITY": self.PHARMACY.CITY,
                "UUID": self.UUID,
                "AMOUNT": str(self.AMOUNT),
                "TIMESTAMP": str(self.TIMESTAMP)}
    