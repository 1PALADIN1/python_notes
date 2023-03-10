from datetime import datetime

import model
import argparse
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

    del_parser = subparsers.add_parser('del', help='deletes note')
    del_parser.add_argument('-i', '--id', help='note id', type=int, required=True)

    edit_parser = subparsers.add_parser('edit', help='edits note')
    edit_parser.add_argument('-i', '--id', help='note id', type=int, required=True)
    edit_parser.add_argument('-t', '--title', help='note title', type=str)
    edit_parser.add_argument('-m', '--msg', help='note body', type=str)

    return main_parser.parse_args()


def run():
    args = parse_args()

    model.init()
    if args.subparser_name == 'add':
        model.add(args.title, args.msg)
    elif args.subparser_name == 'show':
        if args.date:
            try:
                datetime.strptime(args.date, _date_format)
            except ValueError:
                view.show_message('Invalid date format (example: 20.05.1994)')
                return

        notes = model.get(args.id, args.date)
        view.show(notes)
    elif args.subparser_name == 'del':
        found = model.delete(args.id)
        if found:
            view.show_message('Record successfully deleted!')
        else:
            view.show_message(f'Record with id:{args.id} not found...')
    elif args.subparser_name == 'edit':
        err_msg = model.edit(args.id, args.title, args.msg)
        if err_msg:
            view.show_message(err_msg)
        else:
            view.show_message('Record successfully changed!')


if __name__ == '__main__':
    run()
