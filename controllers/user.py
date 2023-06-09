from app.schemas.user_schemas import SignUp


class UserController:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    async def sign_up(self, user: SignUp):

        return ""
