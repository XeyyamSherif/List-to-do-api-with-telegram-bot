from models.user import User
from repositories.to_do_item_repo import ToDoRepository


class ToDoController:

    def __init__(self) -> None:
        self._to_do_repo = ToDoRepository()

    async def create_item(self, item: dict):
        item = await self._to_do_repo.create_item(item)
        print(type(item.created_at))
        return ""
