from typing import List, Optional, Dict

class GameManager:
    """
    Klasa do zarządzania listą ukończonych gier.
    """

    def __init__(self):
        self.games: List[Dict] = []

    def add_game(self, game: Dict) -> None:
        """
        Dodaje nową grę do listy.

        :param game: Słownik z informacjami o grze (title, platform, hours_played, completion_date)
        """
        self.games.append(game)

    def remove_game(self, title: str) -> bool:
        """
        Usuwa grę na podstawie tytułu.

        :param title: Tytuł gry do usunięcia
        :return: True jeśli gra została usunięta, False jeśli jej nie znaleziono
        """
        for i, game in enumerate(self.games):
            if game.get("title") == title:
                del self.games[i]
                return True
        return False

    def edit_game(self, title: str, updated_game: Dict) -> bool:
        """
        Zastępuje dane gry o podanym tytule.

        :param title: Tytuł gry do edycji
        :param updated_game: Nowe dane gry (słownik)
        :return: True jeśli edytowano, False jeśli nie znaleziono gry
        """
        for i, game in enumerate(self.games):
            if game.get("title") == title:
                self.games[i] = updated_game
                return True
        return False

    def get_all_games(self) -> List[Dict]:
        """
        Zwraca wszystkie gry w kolekcji.

        :return: Lista słowników reprezentujących gry
        """
        return self.games

    def get_game(self, title: str) -> Optional[Dict]:
        """
        Zwraca dane gry o podanym tytule.

        :param title: Tytuł gry
        :return: Słownik z danymi gry lub None, jeśli nie znaleziono
        """
        for game in self.games:
            if game.get("title") == title:
                return game
        return None
