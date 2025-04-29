# game_logic/deck.py

# --- Ячейка 1: Импорты ---
import random
from .card import Card, SUITS, RANKS
from .exceptions import EmptyDeckError
from typing import List, Optional # Для аннотаций


# --- Ячейка 2: Класс Deck ---
class Deck:
    """Представляет колоду игральных карт."""

    def __init__(self, num_decks: int = 1):
        """
        Инициализирует колоду. По умолчанию создает и перемешивает
        стандартную колоду из 36 карт.

        Args:
            num_decks: Количество стандартных 36-карточных колод для использования.
        """

        self.cards: List[Card] = [Card(rank, suit) for _ in range(num_decks)
                                   for suit in SUITS
                                   for rank in RANKS]
        print(f"Колода создана с {len(self.cards)} картами.") # Для отладки
        self.shuffle() # Перемешиваем сразу при создании


    # --- НОВЫЙ МЕТОД для пополнения ---
    def add_cards_and_shuffle(self, cards_to_add: List[Card]):
        """
        Добавляет список карт в колоду и перемешивает её.
        Обычно используется для возврата карт из стопки сброса.

        Args:
            cards_to_add: Список объектов Card для добавления.
        """
        if not cards_to_add:
            print("Нет карт для добавления в колоду.")
            return

        # Добавляем новые карты к существующим (или к пустому списку)
        self.cards.extend(cards_to_add)

        # Обязательно перемешиваем после добавления
        self.shuffle()
    # --- КОНЕЦ НОВОГО МЕТОДА ---

    def shuffle(self) -> None:
        """Перемешивает карты в колоде."""
        random.shuffle(self.cards)
        print("Колода перемешана.") # Для отладки

    def deal_one(self) -> Card:
        """
        Сдает одну карту с верха колоды (из конца списка).
        Удаляет карту из колоды.
        Возвращает карту (Card) или None, если колода пуста.
        """

        if self.cards: # Проверка на непустой список - более Pythonic
            return self.cards.pop()
        else:
            raise EmptyDeckError

    def is_empty(self) -> bool:
        """Проверяет, пуста ли колода."""
        return not self.cards #

    def __len__(self) -> int:
        """Возвращает текущее количество карт в колоде."""       
        return len(self.cards)



