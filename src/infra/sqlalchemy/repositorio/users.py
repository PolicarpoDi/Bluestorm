from infra.sqlalchemy.models.models import User
from schemas.schemas import UserModel
from sqlalchemy.orm import Session
from sqlalchemy import select


class RepositorioUser():

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserModel):
        user_db = User(UUID=user.UUID,  
                        USERNAME=user.USERNAME, 
                        PASSWORD=user.PASSWORD)
        self.session.add(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return user_db


    def list_user(self):
        query = select(User)
        users = self.session.execute(query).scalars().all()
        return users


    def get_user_uuid(self, UUID: str) -> User:
        query = select(User).where(User.UUID == UUID)
        uuid_user = self.session.execute(query).scalars().first()
        return uuid_user

