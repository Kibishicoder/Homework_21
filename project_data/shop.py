from .storage import Storage
from .exceptions import StorageFullError


class Shop(Storage):
    def __init__(self):
        super().__init__()
        self._capacity: int = 20

    def add(self, title: str, quantity: int) -> None:
        if self._get_unique_items_count() >= 5:
            raise StorageFullError('В магазине нельзя хранить более 5 наименований товаров')
        super().add(title, quantity)
