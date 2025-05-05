# game_logic/player.py

# --- Ячейка 1: Импорты ---
from .card import Card # Добавили Card для аннотаций
from typing import List, Optional # Добавили для аннотаций


# --- Ячейка 2: Класс Player ---
class Player:
    """Представляет игрока в карточной игре."""

    def __init__(self, name: str = "Игрок"):
        self.name = name
        self.hand: List[Card] = [] # Карты на руках у игрока

    def is_hand_empty(self) -> bool:
        """
        Проверяет, пуста ли рука игрока.

        Returns:
            True, если в руке нет карт, False в противном случае.
        """
        return not self.hand

    def receive_card(self, card: Optional[Card]):
        """Добавляет карту в руку игрока, если она действительна."""
        if card:
            self.hand.append(card)


    def show_hand(self) -> str:
        """Возвращает строковое представление руки игрока."""

        if not self.hand:
            return "Рука пуста."

        # Формируем строку с картами и возвращаем значение
        return ", ".join(str(card) for card in self.hand)


    def find_and_remove_matching_card(self, target_card: Optional[Card]) -> Optional[Card]:
        """
        Ищет карту в руке, которая совпадает с target_card по масти или рангу (приоритет масти).
        Если находит, УДАЛЯЕТ карту из руки и возвращает её.
        Возвращает None, если подходящая карта не найдена.
        """
        
        # Сначала ищем по масти
        card_to_remove = None
        for card in self.hand:
            # Сравниваем каждую карту по масти с target_card
            if card.suit == target_card.suit:
                card_to_remove = card
                break # Нашли первое совпадение по масти, выходим

        # Если по масти не нашли, ищем по рангу
        if card_to_remove is None:           
            for card in self.hand:
                # Сравниваем каждую карту по рангу с target_card
                if card.rank == target_card.rank:
                    card_to_remove = card
                    break # Нашли первое совпадение по рангу, выходим

        # Если не нашли по карте и масти, пытаемся найти дамы 
        if card_to_remove is None:
            for card in self.hand:
                # Пытаемся найти даму
                if card.rank == 'Q':
                    card_to_remove = card
                    break # Нашли Даму, выходим

        # Если нашли карту 
        if card_to_remove:
            # Удаляем карту из руки и возвращаем значение этой карты
            self.hand.remove(card_to_remove)
            return card_to_remove        
        else:
            return None # Ничего не нашли
        

    def __str__(self) -> str:
        # ИЗМЕНЕНИЕ: Добавлена аннотация типа возвращаемого значения.
        return self.name


 
