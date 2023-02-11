from datetime import date
from typing import Optional

import repository

_date_format = '%d.%m.%Y'


def init():
    repository.load()


def add(title: str, message: str):
    repository.notes.append(
        {
            "id": repository.get_next_id(),
            "title": title,
            "message": message,
            "date": date.today().strftime(_date_format),
        }
    )

    repository.save()


def get(note_id: Optional[int] = None, filter_date: Optional[str] = None) -> []:
    result = []

    for note in repository.notes:
        if note_id and note['id'] != note_id:
            continue

        if filter_date and note['date'] != filter_date:
            continue

        result.append(note)

    return result


def delete(note_id: int) -> bool:
    record_found = False
    new_notes = []
    for note in repository.notes:
        if note['id'] == note_id:
            record_found = True
            continue

        new_notes.append(note)

    if record_found:
        repository.notes = new_notes
        repository.save()

    return record_found


def edit(note_id: int, title: Optional[str], message: Optional[str]) -> Optional[str]:
    if not title and not message:
        return 'Nothing to change (specify at least title or message)'

    for note in repository.notes:
        if note['id'] == note_id:
            if title:
                note['title'] = title

            if message:
                note['message'] = message

            repository.save()
            return None

    return f'Record with id:{note_id} not found...'
