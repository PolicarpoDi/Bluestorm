from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


bd_bluestorm = "sqlite:////home/diegopolicarpo/Works/Projects/Pessoal/API_Bluestorm/app/backend_test.db"
# SQLAlchemy specific code, as with any other
DATABASE_URL = bd_bluestorm
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind=engine)
session = Session()

database = Database(DATABASE_URL)



Base = declarative_base()