# game_logic/game.py

# --- Ячейка 1: Импорты ---
from .exceptions import CountPlayersException, EmptyDeckError
from .card import Card
from .deck import Deck
from .player import Player
from typing import List, Optional
    
# --- Ячейка 2: Класс Game ---
class Game:
    """
    Управляет состоянием и логикой игры '101'.
    """
    def __init__(self, deck: Deck, players: List[Player]):
        """
        Инициализирует игру.
        Args:
            deck: Экземпляр колоды карт.
            players: Список экземпляров игроков.
        """
        self.deck = deck
        self.players = players
        self.discard_pile: List[Card] = [] # Стопка сброса (отбой)
        self.current_player_index: int = 0 # Индекс текущего игрока


    def _deal_initial_hands_and_start_discard(self, target_hand_size: int = 4) -> bool:
        """
        Раздает карты по особым правилам и инициализирует стопку сброса.
        - Все игроки, кроме последнего, получают target_hand_size карт.
        - Последний игрок получает target_hand_size - 1 карт.
        - Следующая карта из колоды становится первой картой сброса.

        Args:
            target_hand_size: Целевое количество карт на руках у большинства игроков.

        Returns:
            True, если раздача и старт сброса прошли успешно, False в случае ошибки (пустая колода).
        """
        
        # Определение количества игроков
        num_players = len(self.players)

        # Если число игроков некорректно, выкидываем ошибку
        if num_players <=0 or num_players > 8:
            raise CountPlayersException(num_players)

        print(f"--------Раздаем карты---------")

        try:
            # Раздаем N-1 карт всем игрокам
            for i in range(target_hand_size - 1):
                for player in self.players:
                    card = self.deck.deal_one()
                    player.receive_card(card)

            # Раздаем последнюю карту всем, КРОМЕ последнего игрока
            for i in range(num_players - 1): # Итерируем по индексам игроков, кроме последнего
                player = self.players[i]
                card = self.deck.deal_one()
                player.receive_card(card)

            # Берем карту для старта сброса
            initial_discard_card = self.deck.deal_one()
            self.discard_pile = [initial_discard_card] # Инициализируем сброс этой картой
            print(f"Стартовая карта в сбросе: {initial_discard_card}")

        except EmptyDeckError as e:
            print(f"Ошибка: {e}")
            return False

        return True # Раздача и старт сброса прошли успешно

    def _show_player_hands(self):
        """Выводит текущие руки всех игроков."""

        print("\nРуки игроков:")
        for player in self.players:
            print(player.show_hand())


    def start_game(self):
        """Запускает основной процесс игры."""

        # Шаг 1: Раздача карт и инициализация стопки сброса по новым правилам
        if not self._deal_initial_hands_and_start_discard(target_hand_size=10):
            print("Ошибка инициализации игры. Завершение.")
            return 

        # Шаг 2: Отображение начальных рук
        self._show_player_hands()

        # Шаг 3: Установка первого игрока
        self.current_player_index = 0
        current_player = self.players[self.current_player_index]

        # Шаг 4: Запуск игры
        print(f"\n--- Начало игры ---")
        num_players = len(self.players)

        flag_game = True
        turn_number = -1
        while(flag_game):

            # Счетчик
            turn_number += 1
            print(f"\nХод {turn_number}")
            # Выбор игрока
            self.current_player_index = turn_number % num_players
            current_player = self.players[self.current_player_index]

            # Просмотр руки перед ходом
            print(f"Рука {current_player.name}: {current_player.show_hand()}")

            # Ход игрока
            self.players_turn(current_player)

            # Если у игрока после хода не осталось карт выход из цикла
            if current_player.is_hand_empty():
                print(f"Игрок {current_player.name} победил!!!")
                flag_game = False

            

    def players_turn(self, current_player: Player) -> Optional[Player]:
        
        # Попытка найти карту и сходить
        current_card = current_player.find_and_remove_matching_card(self.discard_pile[-1])

        # Если карта найдена
        if current_card != None:
            self.discard_pile.append(current_card)
            print(f"{current_player.name} сходил: {current_card}")


        # Если нужной карты нет
        else:
            try:
                # Берем карту из колоды
                card = self.deck.deal_one()

            # Если колода пустая берем стопку сброса кроме последней карты и тасуем.     
            except EmptyDeckError:

                self.shuffling_discard_pile()
                # Берем карту из новой колоды
                card = self.deck.deal_one()
    

            # Присваиваем игроку карту из колоды
            current_player.receive_card(card)

            # Просмотр взятой карты
            print(f"{current_player.name} взял: {card}")

            # Попытка найти карту и сходить после взятия карты из колоды
            current_card = current_player.find_and_remove_matching_card(self.discard_pile[-1])

            # Если карта найдена то ходим ею
            if current_card != None:
                self.discard_pile.append(current_card)
                print(f"{current_player.name} сходил: {current_card}")
            
            # Если не найдена пишем об этом
            else:
                print(f"{current_player.name} не нашел после взятия подходящую карту")

            

    def shuffling_discard_pile(self):
        print(f"ВНИМАНИЕ: Колода закончилась! Берем стопку сброса и тасуем. ")

        # Достаем все карты кроме последней из стопки сброса
        self.deck.add_cards_and_shuffle(self.discard_pile[:-1])
        del self.discard_pile[:-1]

        print(f"Теперь в колоде {len(self.deck)} карт")


        
