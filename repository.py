import json
import os

notes = []
_db_path = "db.json"


def load():
    global notes
    if not os.path.exists(_db_path):
        return

    with open(_db_path, 'r', encoding='utf-8') as f:
        json_str = f.read()
        notes = json.loads(json_str)
        print(notes)


def save():
    json_str = json.dumps(notes, indent=2)
    with open(_db_path, 'w', encoding='utf-8') as f:
        f.write(json_str)


def get_next_id() -> int:
    max_id = 0
    for note in notes:
        if note['id'] > max_id:
            max_id = note['id']

    return max_id + 1
