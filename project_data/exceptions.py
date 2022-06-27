class StorageFullError(Exception):
    def __init__(self, message='Хранилище заполнено'):
        self.message = message
        super().__init__(message)


class ItemsNotFoundError(Exception):
    def __init__(self, message='Продукт не найден'):
        self.message = message
        super().__init__(message)


class MessageError(Exception):
    def __init__(self, message='Ошибка запроса'):
        self.message = message
        super().__init__(message)
