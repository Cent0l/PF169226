import json
from typing import List, Dict
from datetime import datetime


def load_data(filepath: str) -> List[Dict]:
    """
    Wczytuje dane z pliku JSON.

    :param filepath: Ścieżka do pliku JSON
    :return: Lista słowników z grami
    :raises: FileNotFoundError, json.JSONDecodeError, ValueError
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Plik nie zawiera listy danych.")
    return data


def save_data(filepath: str, data: List[Dict]) -> None:
    """
    Zapisuje dane do pliku JSON.

    :param filepath: Ścieżka do pliku JSON
    :param data: Lista słowników z grami
    :raises: IOError
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def validate_game_entry(entry: Dict) -> bool:
    """
    Waliduje dane jednej gry.

    :param entry: Słownik z informacjami o grze
    :return: True jeśli dane są poprawne, False w przeciwnym razie
    """
    required_keys = ["title", "platform", "hours_played", "completion_date"]

    if not all(key in entry for key in required_keys):
        return False

    if not isinstance(entry["title"], str) or not entry["title"].strip():
        return False

    if not isinstance(entry["platform"], str) or not entry["platform"].strip():
        return False

    if not isinstance(entry["hours_played"], (int, float)) or entry["hours_played"] < 0:
        return False

    try:
        datetime.strptime(entry["completion_date"], "%Y-%m-%d")
    except ValueError:
        return False

    return True
