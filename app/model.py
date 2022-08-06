from sqlalchemy import Table, Column, String, Date, Integer, MetaData

metadata = MetaData()

PATIENTS = Table(
    "PATIENTS",
    metadata,
    Column("UUID", String, primary_key=True),
    Column("FIRST_NAME", String),
    Column("LAST_NAME", String),
    Column("DATE_OF_BIRTH", Date),
)

PHARMACIES = Table(
    "pharmacies",
    metadata,
    Column("UUID", String, primary_key=True),
    Column("NAME", String),
    Column("CITY", String),
)

TRANSACTIONS = Table(
    "transactions",
    metadata,
    Column("UUID", String, primary_key=True),
    Column("PATIENT_UUID", String),
    Column("PHARMACY_UUID", String),
    Column("AMOUNT", Integer),
    Column("TIMESTAMP", Date),
)