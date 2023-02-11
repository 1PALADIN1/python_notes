from datetime import date
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


def show():
    pass

