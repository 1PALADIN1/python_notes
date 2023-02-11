from datetime import datetime

import model
import argparse
import repository
import view

_date_format = '%d.%m.%Y'


def parse_args() -> argparse.Namespace:
    main_parser = argparse.ArgumentParser(
        prog='Python Notes',
        description='Simple python notes app.')

    subparsers = main_parser.add_subparsers(help='sub-command help', dest='subparser_name')
    add_parser = subparsers.add_parser('add', help='adds new note')
    add_parser.add_argument('-t', '--title', help='note title', type=str, required=True)
    add_parser.add_argument('-m', '--msg', help='note body', type=str, required=True)

    show_parser = subparsers.add_parser('show', help='show notes')
    show_parser.add_argument('-i', '--id', help='note id', type=int)
    show_parser.add_argument('-d', '--date', help='filter date (format dd.mm.yyyy)', type=str)

    # del_parser = subparsers.add_parser('del', help='deletes note')
    # del_parser.add_argument('del', help='deletes note by specified id')
    # del_parser.add_argument('-i', '--id', help='note id', type=str, required=True)

    return main_parser.parse_args()


def run():
    args = parse_args()

    repository.load()
    if args.subparser_name == 'add':
        model.add(args.title, args.msg)
        repository.save()
    elif args.subparser_name == 'show':
        if args.date:
            try:
                datetime.strptime(args.date, _date_format)
            except ValueError:
                print('Invalid date format (example: 20.05.1994)')
                return

        notes = model.get(args.id, args.date)
        view.show(notes)


if __name__ == '__main__':
    run()
