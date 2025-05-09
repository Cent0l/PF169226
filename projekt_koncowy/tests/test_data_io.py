
import pytest
import json
from src import data_io

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

def test_save_and_load_data(tmp_path, valid_game_entry):
    path = tmp_path / "data.json"
    data_io.save_data(str(path), [valid_game_entry])
    loaded = data_io.load_data(str(path))
    assert loaded == [valid_game_entry]

def test_save_empty_list(tmp_path):
    path = tmp_path / "empty.json"
    data_io.save_data(str(path), [])
    with open(path, "r") as f:
        data = json.load(f)
    assert data == []

@pytest.mark.parametrize("entry", [
    {},
    {"title": "", "platform": "PC", "hours_played": 10, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "", "hours_played": 10, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "PC", "hours_played": -1, "completion_date": "2024-01-01"},
    {"title": "Game", "platform": "PC", "hours_played": 10, "completion_date": "invalid-date"},
])
def test_validate_invalid_entry(entry):
    assert data_io.validate_game_entry(entry) is False

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        data_io.load_data("nonexistent.json")

def test_load_data_invalid_json(tmp_path):
    file_path = tmp_path / "bad.json"
    file_path.write_text("not json")
    with pytest.raises(json.JSONDecodeError):
        data_io.load_data(str(file_path))

def test_load_data_not_list(tmp_path):
    file_path = tmp_path / "object.json"
    with open(file_path, "w") as f:
        json.dump({"a": 1}, f)
    with pytest.raises(ValueError):
        data_io.load_data(str(file_path))

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

@pytest.mark.parametrize("dataset", [
    [],
    [{"title": "G1", "platform": "PC", "hours_played": 1, "completion_date": "2024-01-01"}],
    [{"title": "G2", "platform": "PS4", "hours_played": 2, "completion_date": "2024-01-02"}],
    [{"title": f"G{i}", "platform": "PC", "hours_played": i, "completion_date": "2024-01-01"} for i in range(10)],
])
def test_roundtrip_dataset(tmp_path, dataset):
    path = tmp_path / "games.json"
    data_io.save_data(str(path), dataset)
    loaded = data_io.load_data(str(path))
    assert loaded == dataset

@pytest.mark.parametrize("invalid_structure", [
    {"not": "a list"},
    "string",
    123,
    4.5,
    None
])
def test_load_data_invalid_structure(tmp_path, invalid_structure):
    path = tmp_path / "struct.json"
    with open(path, "w") as f:
        json.dump(invalid_structure, f)
    with pytest.raises(ValueError):
        data_io.load_data(str(path))

def test_load_data_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("")
    with pytest.raises(json.JSONDecodeError):
        data_io.load_data(str(file_path))

def test_save_data_non_serializable(tmp_path):
    path = tmp_path / "bad_save.json"
    data = [{"title": "Game", "platform": set(), "hours_played": 10, "completion_date": "2024-01-01"}]
    with pytest.raises(TypeError):
        data_io.save_data(str(path), data)

def test_load_data_list_of_non_dicts(tmp_path):
    file_path = tmp_path / "bad_list.json"
    json.dump(["not_a_dict"], open(file_path, "w"))
    loaded = data_io.load_data(str(file_path))
    assert loaded == ["not_a_dict"]

def test_save_data_unicode_characters(tmp_path):
    game = {
        "title": "Żółw Ninja",
        "platform": "🕹️",
        "hours_played": 42.0,
        "completion_date": "2024-05-01"
    }
    path = tmp_path / "unicode.json"
    data_io.save_data(str(path), [game])
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data[0]["title"] == "Żółw Ninja"
    assert data[0]["platform"] == "🕹️"
