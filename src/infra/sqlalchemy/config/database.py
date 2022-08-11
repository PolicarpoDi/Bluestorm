from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a Database URL for SQLAlchemy
DATABASE_URL = "sqlite:///./backend_test.db"

# Create engine SQLAlchemy
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()


def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

