class GameLogicError(Exception):
    """Базовый класс для всех исключений, связанных с логикой игры '101'."""
    # Можно добавить общую логику или атрибуты для всех игровых ошибок сюда
    pass

class DeckError(GameLogicError):
    """Исключения, связанные с операциями над колодой."""
    pass


class EmptyDeckError(DeckError):
    """Исключение: Попытка взять карту из пустой колоды."""
    def __init__(self, message="Попытка взять карту из пустой колоды"):
        self.message = message
        super().__init__(self.message)

class CountPlayersException(GameLogicError):
    """Исключение: Не корректное количество игроков"""
    def __init__(self, num_player: int, message="Некорректное число игроков"):
        self.message = f"{message}: {num_player}"
        super().__init__(self.message)
