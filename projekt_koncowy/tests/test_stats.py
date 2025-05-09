
import pytest
from src import stats

@pytest.fixture
def game_data():
    return [
        {"title": "Game A", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
        {"title": "Game B", "platform": "PC", "hours_played": 20, "completion_date": "2024-01-15"},
        {"title": "Game C", "platform": "PS4", "hours_played": 30, "completion_date": "2024-02-01"},
        {"title": "Game D", "platform": "PS4", "hours_played": 40, "completion_date": "2024-02-15"},
        {"title": "Game E", "platform": "Switch", "hours_played": 25, "completion_date": "2024-03-01"},
    ]

def test_average_playtime(game_data):
    assert stats.average_playtime(game_data) == 25.0

def test_average_playtime_empty():
    assert stats.average_playtime([]) == 0.0

def test_total_playtime(game_data):
    assert stats.total_playtime(game_data) == 125.0

def test_total_playtime_empty():
    assert stats.total_playtime([]) == 0.0

def test_most_used_platform(game_data):
    assert stats.most_used_platform(game_data) in ["PC", "PS4"]

def test_most_used_platform_empty():
    assert stats.most_used_platform([]) is None

def test_games_completed_by_month(game_data):
    result = stats.games_completed_by_month(game_data)
    assert result == {
        "2024-01": 2,
        "2024-02": 2,
        "2024-03": 1
    }

def test_games_completed_by_month_with_invalid_date():
    data = [{"title": "Bad", "platform": "PC", "hours_played": 5, "completion_date": "bad-date"}]
    assert stats.games_completed_by_month(data) == {}

def test_get_games_in_date_range(game_data):
    result = stats.get_games_in_date_range(game_data, "2024-01-01", "2024-01-31")
    assert len(result) == 2

def test_get_games_in_date_range_full(game_data):
    result = stats.get_games_in_date_range(game_data, "2024-01-01", "2024-12-31")
    assert len(result) == 5

def test_get_games_in_date_range_none(game_data):
    result = stats.get_games_in_date_range(game_data, "2023-01-01", "2023-12-31")
    assert result == []

def test_get_games_in_date_range_invalid_format(game_data):
    result = stats.get_games_in_date_range(game_data, "bad-date", "also-bad")
    assert result == []

def test_average_playtime_rounding():
    data = [
        {"title": "Game A", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
        {"title": "Game B", "platform": "PC", "hours_played": 20, "completion_date": "2024-01-01"},
        {"title": "Game C", "platform": "PC", "hours_played": 25, "completion_date": "2024-01-01"}
    ]
    assert stats.average_playtime(data) == 18.33

@pytest.mark.parametrize("entries,expected", [
    ([], 0.0),
    ([{"hours_played": 0}], 0.0),
    ([{"hours_played": 1.5}], 1.5),
])
def test_average_playtime_param(entries, expected):
    for e in entries:
        e.update({"title": "X", "platform": "X", "completion_date": "2024-01-01"})
    assert stats.average_playtime(entries) == expected

@pytest.mark.parametrize("entries,expected", [
    ([], 0.0),
    ([{"hours_played": 0}], 0.0),
    ([{"hours_played": 1.5}], 1.5),
    ([{"hours_played": 1}, {"hours_played": 2}], 3.0),
])
def test_total_playtime_param(entries, expected):
    for e in entries:
        e.update({"title": "X", "platform": "X", "completion_date": "2024-01-01"})
    assert stats.total_playtime(entries) == expected

def test_games_completed_by_month_ignores_invalid():
    data = [
        {"title": "Valid", "platform": "PC", "hours_played": 5, "completion_date": "2024-01-01"},
        {"title": "Bad", "platform": "PC", "hours_played": 5, "completion_date": "wrong"},
    ]
    result = stats.games_completed_by_month(data)
    assert result == {"2024-01": 1}

def test_get_games_in_date_range_single_match():
    data = [{"title": "One", "platform": "PC", "hours_played": 5, "completion_date": "2024-05-01"}]
    result = stats.get_games_in_date_range(data, "2024-05-01", "2024-05-01")
    assert len(result) == 1

def test_get_games_in_date_range_multiple_bounds():
    data = [
        {"title": "A", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
        {"title": "B", "platform": "PC", "hours_played": 20, "completion_date": "2024-01-02"},
        {"title": "C", "platform": "PC", "hours_played": 30, "completion_date": "2024-01-03"},
    ]
    result = stats.get_games_in_date_range(data, "2024-01-02", "2024-01-03")
    assert len(result) == 2

def test_most_used_platform_tie():
    data = [
        {"title": "1", "platform": "PC", "hours_played": 1, "completion_date": "2024-01-01"},
        {"title": "2", "platform": "PS4", "hours_played": 1, "completion_date": "2024-01-01"},
    ]
    assert stats.most_used_platform(data) in ["PC", "PS4"]

def test_games_completed_by_month_unsorted_dates():
    data = [
        {"title": "1", "platform": "PC", "hours_played": 10, "completion_date": "2024-03-01"},
        {"title": "2", "platform": "PC", "hours_played": 20, "completion_date": "2024-01-01"},
        {"title": "3", "platform": "PC", "hours_played": 30, "completion_date": "2024-01-10"},
    ]
    result = stats.games_completed_by_month(data)
    assert result["2024-01"] == 2
    assert result["2024-03"] == 1

def test_average_playtime_missing_hours():
    data = [{"title": "A", "platform": "PC", "completion_date": "2024-01-01"}]
    assert stats.average_playtime(data) == 0.0

def test_total_playtime_missing_hours():
    data = [{"title": "A", "platform": "PC", "completion_date": "2024-01-01"}]
    assert stats.total_playtime(data) == 0.0

def test_average_playtime_mixed_valid_invalid():
    data = [
        {"title": "A", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
        {"title": "B", "platform": "PC", "completion_date": "2024-01-01"},
    ]
    assert stats.average_playtime(data) == 5.0

def test_total_playtime_mixed_valid_invalid():
    data = [
        {"title": "A", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
        {"title": "B", "platform": "PC", "completion_date": "2024-01-01"},
    ]
    assert stats.total_playtime(data) == 10.0

def test_games_completed_by_month_missing_date():
    data = [{"title": "A", "platform": "PC", "hours_played": 10}]
    assert stats.games_completed_by_month(data) == {}

def test_get_games_in_date_range_missing_completion_date():
    data = [{"title": "A", "platform": "PC", "hours_played": 10}]
    result = stats.get_games_in_date_range(data, "2024-01-01", "2024-12-31")
    assert result == []

def test_average_playtime_float_rounding():
    data = [
        {"title": "A", "platform": "PC", "hours_played": 1, "completion_date": "2024-01-01"},
        {"title": "B", "platform": "PC", "hours_played": 2, "completion_date": "2024-01-01"},
    ]
    assert stats.average_playtime(data) == 1.5

def test_total_playtime_large_numbers():
    data = [{"title": "X", "platform": "PC", "hours_played": 1e6, "completion_date": "2024-01-01"}]
    assert stats.total_playtime(data) == 1e6

def test_get_games_in_date_range_edge_match():
    data = [{"title": "Edge", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"}]
    result = stats.get_games_in_date_range(data, "2024-01-01", "2024-01-01")
    assert len(result) == 1

def test_most_used_platform_empty_strings():
    data = [{"title": "X", "platform": "", "hours_played": 1, "completion_date": "2024-01-01"}]
    assert stats.most_used_platform(data) == ""

def test_most_used_platform_null_values():
    data = [{"title": "X", "platform": None, "hours_played": 1, "completion_date": "2024-01-01"}]
    assert stats.most_used_platform(data) is None

def test_get_games_in_date_range_partial_dates():
    data = [{"title": "X", "platform": "PC", "hours_played": 5}]
    result = stats.get_games_in_date_range(data, "2024-01-01", "2024-01-01")
    assert result == []

def test_games_completed_by_month_all_same_month():
    data = [
        {"title": f"Game {i}", "platform": "PC", "hours_played": i, "completion_date": "2024-01-01"}
        for i in range(10)
    ]
    result = stats.games_completed_by_month(data)
    assert result == {"2024-01": 10}

def test_games_completed_by_month_multiple_years():
    data = [
        {"title": "Old", "platform": "PC", "hours_played": 10, "completion_date": "2020-01-01"},
        {"title": "New", "platform": "PC", "hours_played": 20, "completion_date": "2024-01-01"},
    ]
    result = stats.games_completed_by_month(data)
    assert result["2020-01"] == 1
    assert result["2024-01"] == 1

def test_total_playtime_non_numeric():
    data = [{"title": "X", "platform": "PC", "hours_played": "five", "completion_date": "2024-01-01"}]
    with pytest.raises(TypeError):
        stats.total_playtime(data)
