def show(notes: []):
    for note in notes:
        print("-------------------- *** --------------------")
        print(f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nDate: {note['date']}")
        print("-------------------- *** --------------------")


def show_message(message: str):
    print(message)
