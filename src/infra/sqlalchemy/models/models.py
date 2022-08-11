from sqlalchemy import DateTime, ForeignKey, Column, String, Date, Float
from infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "USERS"

    UUID = Column(String, primary_key=True, index=True)
    USERNAME = Column(String, index=True)
    PASSWORD = Column(String, index=True)


class Patients(Base):
    __tablename__ = "PATIENTS"

    UUID = Column(String, primary_key=True)
    FIRST_NAME = Column(String, index=True)
    LAST_NAME = Column(String, index=True)
    DATE_OF_BIRTH = Column(Date, index=True)


class Pharmacies(Base):
    __tablename__ = "PHARMACIES"

    UUID = Column(String, primary_key=True, index=True)
    NAME = Column(String, index=True)
    CITY = Column(String, index=True)


class Transactions(Base):
    __tablename__ = "TRANSACTIONS"

    UUID = Column(String, primary_key=True, index=True)
    PATIENT_UUID = Column(String, ForeignKey("PATIENTS.UUID"))
    PHARMACY_UUID = Column(String, ForeignKey("PHARMACIES.UUID"))
    AMOUNT = Column(Float, index=True)
    TIMESTAMP = Column(DateTime, index=True)
    PATIENTS = relationship("Patients")
    PHARMACY = relationship("Pharmacies")