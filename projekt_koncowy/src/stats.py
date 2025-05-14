from typing import List, Dict, Optional
from collections import Counter
from datetime import datetime


def average_playtime(data: List[Dict]) -> float:
    """
    Zwraca średni czas grania dla wszystkich gier.

    :param data: Lista gier
    :return: Średni czas w godzinach, 0.0 jeśli brak gier
    """
    if not data:
        return 0.0
    total = sum(game.get("hours_played", 0) for game in data)
    return round(total / len(data), 2)


def total_playtime(data: List[Dict]) -> float:
    """
    Zwraca łączny czas grania.

    :param data: Lista gier
    :return: Suma godzin
    """

    return round(sum(game.get("hours_played", 0) for game in data), 2)


def most_used_platform(data: List[Dict]) -> Optional[str]:
    """
    Zwraca najczęściej używaną platformę.

    :param data: Lista gier
    :return: Nazwa platformy lub None jeśli brak danych
    """
    if not data:
        return None
    platforms = [game.get("platform", "") for game in data]
    counter = Counter(platforms)
    return counter.most_common(1)[0][0]


def games_completed_by_month(data: List[Dict]) -> Dict[str, int]:
    """
    Zwraca liczbę ukończonych gier w podziale na miesiące (format YYYY-MM).

    :param data: Lista gier
    :return: Słownik {YYYY-MM: liczba gier}
    """
    result: Dict[str, int] = {}
    for game in data:
        try:
            date = datetime.strptime(game.get("completion_date", ""), "%Y-%m-%d")
            key = date.strftime("%Y-%m")
            result[key] = result.get(key, 0) + 1
        except ValueError:
            continue
    return result


def get_games_in_date_range(data: List[Dict], start: str, end: str) -> List[Dict]:
    """
    Zwraca gry ukończone między podanymi datami (włącznie).

    :param data: Lista gier
    :param start: Data początkowa (YYYY-MM-DD)
    :param end: Data końcowa (YYYY-MM-DD)
    :return: Lista gier z danego zakresu
    """
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        return []

    return [
        game for game in data
        if "completion_date" in game
        and start_date <= datetime.strptime(game["completion_date"], "%Y-%m-%d") <= end_date
    ]
