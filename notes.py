import model
import argparse
import repository


def parse_args() -> argparse.Namespace:
    main_parser = argparse.ArgumentParser(
        prog='Python Notes',
        description='Simple python notes app.')

    subparsers = main_parser.add_subparsers(help='sub-command help', dest='subparser_name')
    add_parser = subparsers.add_parser('add', help='adds new note')
    add_parser.add_argument('-t', '--title', help='note title', type=str, required=True)
    add_parser.add_argument('-m', '--msg', help='note body', type=str, required=True)

    # show_parser = subparsers.add_parser('show', help='show notes')
    # show_parser.add_argument('show', help='show all notes')
    #
    # del_parser = subparsers.add_parser('del', help='deletes note')
    # del_parser.add_argument('del', help='deletes note by specified id')
    # del_parser.add_argument('-i', '--id', help='note id', type=str, required=True)

    return main_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    repository.load()
    if args.subparser_name == 'add':
        model.add(args.title, args.msg)
        repository.save()
    elif args.subparser_name == 'show':
        model.show()
