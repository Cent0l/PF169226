
Aplikacja do zarządzania i śledzenia ukończonych gier komputerowych. Projekt został napisany w Pythonie z naciskiem na **modularną strukturę kodu** oraz **pełne pokrycie testami jednostkowymi (pytest)**.

---

##  Struktura projektu

```
cntl/
├── src/
│   ├── game_manager.py     # Logika zarządzania grami (dodawanie, edycja, usuwanie)
│   ├── data_io.py          # Obsługa plików JSON (zapis/odczyt, walidacja)
│   ├── stats.py            # Statystyki na podstawie danych o grach
│   └── __init__.py
├── tests/
│   ├── test_game_manager.py  # Testy jednostkowe modułu game_manager
│   ├── test_data_io.py       # Testy jednostkowe modułu data_io
│   ├── test_stats.py         # Testy jednostkowe modułu stats
│   └── __init__.py
├── check_coverage.py       # Skrypt do sprawdzania pokrycia kodu testami
├── requirements.txt        # Biblioteki potrzebne do uruchomienia testów
```

---

## ️ Opis funkcjonalności

### `game_manager.py`
- `add_game(game: dict)` – dodaje grę do listy
- `remove_game(title: str)` – usuwa grę po tytule
- `edit_game(title: str, updated_game: dict)` – modyfikuje dane gry
- `get_game(title: str)` – zwraca grę o podanym tytule
- `get_all_games()` – zwraca wszystkie gry

### `data_io.py`
- `load_data(filepath: str)` – ładuje dane z pliku `.json`
- `save_data(filepath: str, data: list)` – zapisuje listę do pliku `.json`
- `validate_game_entry(entry: dict)` – sprawdza poprawność formatu danych

### `stats.py`
- `average_playtime(data: list)` – średnia liczba godzin gry
- `total_playtime(data: list)` – suma godzin gry
- `most_used_platform(data: list)` – najczęściej używana platforma
- `games_completed_by_month(data: list)` – liczba ukończonych gier w miesiącach
- `get_games_in_date_range(data: list, start_date: str, end_date: str)` – gry ukończone w danym przedziale czasu

---

## Uruchamianie testów

Instalacja zależności:

```
pip install -r requirements.txt
```

Uruchomienie wszystkich testów:

```
pytest tests/
```

Sprawdzenie pokrycia kodu:

```
python check_coverage.py
```

---

