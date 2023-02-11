from datetime import date
from typing import Optional

import repository

_date_format = '%d.%m.%Y'


def add(title: str, message: str):
    repository.notes.append(
        {
            "id": repository.get_next_id(),
            "title": title,
            "message": message,
            "date": date.today().strftime(_date_format),
        }
    )


def get(note_id: Optional[int] = None, filter_date: Optional[str] = None) -> []:
    result = []

    for note in repository.notes:
        if note_id and note['id'] != note_id:
            continue

        if filter_date and note['date'] != filter_date:
            continue

        result.append(note)

    return result
