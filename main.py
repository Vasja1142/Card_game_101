# main.py

from game_logic.deck import Deck
from game_logic.player import Player
from game_logic.card import card_to_string # Импортируем функцию для вывода

def main():
    """Основная функция для запуска простой демонстрации."""
    print("--- Начало игры '101' (Демо) ---")

    # 1. Создаем колоду
    deck = Deck()

    # 2. Создаем игроков
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    players = [player1, player2]
    print(f"Игроки: {[p.name for p in players]}")

    # 3. Раздаем карты (например, по 7 карт)
    num_cards_to_deal = 7
    print(f"\nРаздаем по {num_cards_to_deal} карт...")
    for _ in range(num_cards_to_deal):
        for player in players:
            card = deck.deal_one()
            player.receive_card(card)

    # 4. Показываем руки игроков
    print("\nРуки игроков:")
    for player in players:
        print(player.show_hand())

    # 5. (Для примера) Показываем оставшуюся колоду
    print(f"\nКарт осталось в колоде: {len(deck)}")

    # 6. (Для примера) Создаем стопку сброса
    discard_pile = []
    top_discard = deck.deal_one()
    if top_discard:
        discard_pile.append(top_discard)
        print(f"\nВерхняя карта сброса: {card_to_string(top_discard)}")
    else:
        print("\nНе удалось взять карту для стопки сброса (колода пуста?).")


    print("\n--- Демо завершено ---")

if __name__ == "__main__":
    # Эта конструкция гарантирует, что функция main() вызовется,
    # только если этот файл запускается напрямую (а не импортируется как модуль)
    main()