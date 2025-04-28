# game_logic/player.py

from .card import card_to_string # Для красивого вывода руки

class Player:
    """Представляет игрока."""

    def __init__(self, name="Игрок"):
        self.name = name
        self.hand = [] # Карты на руках у игрока

    def receive_card(self, card):
        """Добавляет карту в руку игрока."""
        if card:
            self.hand.append(card)

    def show_hand(self):
        """Возвращает строковое представление руки игрока."""
        if not self.hand:
            return f"{self.name}: Рука пуста."
        # Сортируем руку для удобства просмотра (опционально, можно настроить сортировку)
        # sorted_hand = sorted(self.hand) # Потребует определения сравнения для Card
        hand_str = ", ".join(card_to_string(card) for card in self.hand)
        return f"{self.name}: {hand_str}"

    def __str__(self):
        return self.name

# Пример использования:
# player1 = Player("Вася")
# print(player1)
# card_example = Card('A', '♠')
# player1.receive_card(card_example)
# print(player1.show_hand())