from typing import List

from app.database import get_db
from models.user import User

session = next(get_db())
class UserRepository:

    # def get_all_items(self) -> List[User]:
    #     return self.items

    def get_item_by_username(self, username: string):
            return session.query(User).get(username)


