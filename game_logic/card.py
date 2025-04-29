# game_logic/card.py
# --- Ячейка 1: Импорты и определение Card ---
from typing import NamedTuple, List 

class Card(NamedTuple):
    """Представляет игральную карту с рангом и мастью."""
    rank: str
    suit: str
    def __str__(self):
        return f"{self.rank}{self.suit}"


# --- Ячейка 2: Константы ---
# Определим возможные масти и ранги (для 36 карт)
SUITS: List[str] = ['♥', '♦', '♣', '♠'] # Червы, Бубны, Трефы, Пики
RANKS: List[str] = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # Валет, Дама, Король, Туз


