from typing import List

from app.database import get_db
from models.to_do_item import ToDo

session = next(get_db())


class ToDoRepository:

    async def create_item(self, item):
        item = ToDo(**item)
        session.add(item)
        session.commit()
        return item

