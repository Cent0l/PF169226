import pytest
import json
from src import data_io
from unittest.mock import mock_open, patch


@pytest.fixture
def valid_game_entry():
    return {
        "title": "Hollow Knight",
        "platform": "PC",
        "hours_played": 45.5,
        "completion_date": "2024-01-10"
    }


def test_validate_correct_entry(valid_game_entry):
    assert data_io.validate_game_entry(valid_game_entry) is True


def test_save_data_mock(valid_game_entry):
    m = mock_open()
    with patch("builtins.open", m), patch("json.dump") as dump_mock:
        data_io.save_data("fake.json", [valid_game_entry])
        dump_mock.assert_called_once_with(
            [valid_game_entry],
            m(),
            indent=2,
            ensure_ascii=False
        )


def test_load_data_mock_valid():
    mock_json = '[{"title": "Game", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"}]'
    with patch("builtins.open", mock_open(read_data=mock_json)), patch("json.load", return_value=json.loads(mock_json)):
        result = data_io.load_data("fake.json")
        assert isinstance(result, list)
        assert result[0]["title"] == "Game"


def test_load_data_file_not_found_mock():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            data_io.load_data("missing.json")


def test_load_data_invalid_json_mock():
    m = mock_open(read_data="not json")
    with patch("builtins.open", m), patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "not json", 0)):
        with pytest.raises(json.JSONDecodeError):
            data_io.load_data("broken.json")


def test_load_data_not_list_mock():
    m = mock_open(read_data='{"not": "a list"}')
    with patch("builtins.open", m), patch("json.load", return_value={"not": "a list"}):
        with pytest.raises(ValueError):
            data_io.load_data("notalist.json")


@pytest.mark.parametrize("entry", [
    {},
    {"title": "", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "", "hours_played": 10, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "PC", "hours_played": -1, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "PC", "hours_played": 10, "completion_date": "invalid-date"},
])
def test_validate_invalid_entry(entry):
    assert data_io.validate_game_entry(entry) is False


@pytest.mark.parametrize("missing_field", ["title", "platform", "hours_played", "completion_date"])
def test_validate_missing_fields(valid_game_entry, missing_field):
    entry = valid_game_entry.copy()
    del entry[missing_field]
    assert data_io.validate_game_entry(entry) is False


@pytest.mark.parametrize("field,value", [
    ("title", 123),
    ("platform", 999),
    ("hours_played", "ten"),
    ("completion_date", "2024-31-01")
])
def test_validate_wrong_types(valid_game_entry, field, value):
    entry = valid_game_entry.copy()
    entry[field] = value
    assert data_io.validate_game_entry(entry) is False


@pytest.mark.parametrize("hours", [0, 0.1, 9999])
def test_validate_hours_boundary(valid_game_entry, hours):
    entry = valid_game_entry.copy()
    entry["hours_played"] = hours
    assert data_io.validate_game_entry(entry) is True


@pytest.mark.parametrize("date", ["2024-01-01", "2000-12-31"])
def test_validate_various_dates(valid_game_entry, date):
    entry = valid_game_entry.copy()
    entry["completion_date"] = date
    assert data_io.validate_game_entry(entry) is True


@pytest.mark.parametrize("bad_date", ["2024-13-01", "2024-00-01", "2024-01-32"])
def test_validate_bad_calendar_dates(valid_game_entry, bad_date):
    entry = valid_game_entry.copy()
    entry["completion_date"] = bad_date
    assert data_io.validate_game_entry(entry) is False


def test_validate_game_entry_non_dict():
    assert data_io.validate_game_entry("not a dict") is False


def test_validate_game_entry_empty_dict():
    assert data_io.validate_game_entry({}) is False


def test_save_data_unicode_characters():
    entry = {
        "title": "Żółw Ninja",
        "platform": "🕹️",
        "hours_played": 3,
        "completion_date": "2024-05-01"
    }
    m = mock_open()
    with patch("builtins.open", m), patch("json.dump") as dump_mock:
        data_io.save_data("file.json", [entry])
        dump_mock.assert_called_once()


def test_save_data_type_error():
    entry = {
        "title": "Test",
        "platform": "PC",
        "hours_played": set([1, 2, 3]),
        "completion_date": "2024-01-01"
    }
    m = mock_open()
    with patch("builtins.open", m), patch("json.dump", side_effect=TypeError):
        with pytest.raises(TypeError):
            data_io.save_data("bad.json", [entry])