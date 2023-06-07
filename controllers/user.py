

class UserController:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository
