from typing import List

from app.database import get_db
from models.user import User

session = next(get_db())


class UserRepository:

    def get_item_by_username(self, username: str):
        return session.query(User).get(username)

    def create_user(self, user: User):
        session.add(user)
