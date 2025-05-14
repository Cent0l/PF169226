import pytest
from src.game_manager import GameManager


@pytest.fixture
def sample_game():
    return {
        "title": "The Witcher 3",
        "platform": "PC",
        "hours_played": 100,
        "completion_date": "2023-12-01"
    }


@pytest.fixture
def manager_with_games():
    manager = GameManager()
    games = [
        {"title": "Game A", "platform": "PC", "hours_played": 10, "completion_date": "2023-01-01"},
        {"title": "Game B", "platform": "PS4", "hours_played": 20, "completion_date": "2023-02-01"},
        {"title": "Game C", "platform": "Switch", "hours_played": 30, "completion_date": "2023-03-01"}
    ]
    for g in games:
        manager.add_game(g)
    return manager


def test_add_game(sample_game):
    manager = GameManager()
    manager.add_game(sample_game)
    assert len(manager.get_all_games()) == 1
    assert manager.get_game("The Witcher 3") == sample_game


def test_remove_existing_game(sample_game):
    manager = GameManager()
    manager.add_game(sample_game)
    assert manager.remove_game("The Witcher 3") is True
    assert manager.get_game("The Witcher 3") is None


def test_remove_nonexistent_game():
    manager = GameManager()
    assert manager.remove_game("Nonexistent") is False


def test_edit_existing_game(sample_game):
    manager = GameManager()
    manager.add_game(sample_game)
    updated_game = sample_game.copy()
    updated_game["hours_played"] = 150
    assert manager.edit_game("The Witcher 3", updated_game) is True
    assert manager.get_game("The Witcher 3")["hours_played"] == 150


def test_edit_nonexistent_game(sample_game):
    manager = GameManager()
    assert manager.edit_game("NotThere", sample_game) is False


def test_get_game_returns_none_for_missing():
    manager = GameManager()
    assert manager.get_game("Missing Game") is None


def test_get_all_games_empty():
    manager = GameManager()
    assert manager.get_all_games() == []


def test_get_all_games_with_data(sample_game):
    manager = GameManager()
    manager.add_game(sample_game)
    assert len(manager.get_all_games()) == 1


def test_add_multiple_games(manager_with_games):
    assert len(manager_with_games.get_all_games()) == 3


def test_remove_game_from_multiple(manager_with_games):
    assert manager_with_games.remove_game("Game B") is True
    assert manager_with_games.get_game("Game B") is None


def test_edit_game_in_multiple(manager_with_games):
    updated = {"title": "Game B", "platform": "PS5", "hours_played": 25, "completion_date": "2023-02-01"}
    assert manager_with_games.edit_game("Game B", updated) is True
    assert manager_with_games.get_game("Game B")["platform"] == "PS5"


@pytest.mark.parametrize("title", ["Game A", "Game B", "Game C", "Nonexistent"])
def test_get_game_various_titles(manager_with_games, title):
    game = manager_with_games.get_game(title)
    if title == "Nonexistent":
        assert game is None
    else:
        assert game is not None
        assert game["title"] == title


@pytest.mark.parametrize("new_title", ["Game X", "Game Y", "Game Z"])
def test_add_and_find_games(new_title):
    manager = GameManager()
    game = {
        "title": new_title,
        "platform": "PC",
        "hours_played": 10,
        "completion_date": "2024-01-01"
    }
    manager.add_game(game)
    assert manager.get_game(new_title)["title"] == new_title


def test_remove_game_case_sensitive():
    manager = GameManager()
    manager.add_game({"title": "CaseTest", "platform": "PC", "hours_played": 5, "completion_date": "2023-11-11"})
    assert manager.remove_game("casetest") is False
    assert manager.remove_game("CaseTest") is True


def test_edit_game_case_sensitive():
    manager = GameManager()
    game = {"title": "EditTest", "platform": "PC", "hours_played": 5, "completion_date": "2023-11-11"}
    manager.add_game(game)
    updated = game.copy()
    updated["platform"] = "Mobile"
    assert manager.edit_game("edittest", updated) is False
    assert manager.edit_game("EditTest", updated) is True


@pytest.mark.parametrize("index", range(20))
def test_bulk_add_and_remove(index):
    manager = GameManager()
    title = f"Game_{index}"
    game = {
        "title": title,
        "platform": "PC",
        "hours_played": index * 5,
        "completion_date": f"2023-01-{(index % 28) + 1:02d}"
    }
    manager.add_game(game)
    assert manager.get_game(title) is not None
    assert manager.remove_game(title) is True
    assert manager.get_game(title) is None
