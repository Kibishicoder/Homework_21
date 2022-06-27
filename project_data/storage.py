from abc import ABC, abstractmethod

from .exceptions import StorageFullError, ItemsNotFoundError


class Storage(ABC):
    """Abstract class"""

    @abstractmethod
    def __init__(self):
        self._items: dict[str: int] = {}
        self._capacity: int = 0

    def __repr__(self):
        return f'Это Storage типа {self.__class__.__name__} с вместимостью {self._capacity}'

    def add(self, title: str, quantity: int) -> None:

        if self._get_free_space() < quantity:
            raise StorageFullError('Нет свободного места')
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:

        if title not in self._items.keys():
            raise ItemsNotFoundError(f'Товар с наименованием {title} не найден')
        if quantity > self._items.get(title):
            raise ItemsNotFoundError(f'Нет нужного количества товара с наименованием {title}')

        self._items[title] = self._items.get(title) - quantity
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self) -> int:
        """Получаем количество свободного места"""
        taken_space = sum([item for item in self._items.values()])
        return self._capacity - taken_space

    def get_items(self) -> dict:
        """Получаем список продуктов"""
        return self._items

    def _get_unique_items_count(self) -> int:
        """Получаем список уникальных продуктов"""
        return len([item for item in self._items.keys()])
