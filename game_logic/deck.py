import random
from .card import Card, SUITS, RANKS # Используем относительный импорт внутри пакета


class Deck:
    """Представляет колоду карт."""

    def __init__(self, num_decks=1):
        """
        Инициализирует колоду.
        По умолчанию создает стандартную колоду из 36 карт.
        """
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS] * num_decks
        self.shuffle()
        print(f"Колода создана с {len(self.cards)} картами.") # Для отладки

    def shuffle(self):
        """Перемешивает колоду."""
        random.shuffle(self.cards)
        print("Колода перемешана.") # Для отладки

    def deal_one(self):
        """
        Сдает одну карту из колоды.
        Возвращает карту или None, если колода пуста.
        """
        if not self.is_empty():
            return self.cards.pop()
        else:
            print("Колода пуста!")
            return None

    def is_empty(self):
        """Проверяет, пуста ли колода."""
        return len(self.cards) == 0

    def __len__(self):
        """Возвращает количество карт в колоде."""
        return len(self.cards)
