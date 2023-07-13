from app.schemas.user_schemas import SignUp
from models.user import User
from repositories.user_repo import UserRepository
from pythondi import inject


class UserController:
    def __init__(self):
        self.user_repo = user_repo

    async def create_user(self, user: SignUp):
        print(user)
        # user = User(**user)
        # print(user)
        return ""
