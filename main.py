# main.py
from game_logic.deck import Deck
from game_logic.player import Player
from game_logic.game import Game
from game_logic.exceptions import CountPlayersException, EmptyDeckError


def main():

    """Основная функция для запуска игры '101'."""
    print("--- Начало игры '101' (Базовая логика) ---")

    # 1. Создаем колоду
    deck = Deck()

    # 2. Создаем игроков
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    player3 = Player("Игрок 3")
    players = [player1, player2, player3]
    
    print(f"Игроки: {[p.name for p in players]}") # Добавим вывод имен для наглядности


    # 3. Создаем и запускаем игру
    try:
        game_instance = Game(deck, players)
        game_instance.start_game()
        print("\n--- Игра завершена (или прервана) ---")
        
    except CountPlayersException as e:
        print(e)
        print("Игра не будет запущена")

    

# --- Ячейка 3: Точка входа ---
if __name__ == "__main__":

    main()