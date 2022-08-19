import sys
from code.list import ls
from code.add import copy
from code.delete import delete


commands = {
    'add': copy,
    'delete': delete,
    'list': ls
}


def execute():

    _, command, *args = sys.argv

    if command not in commands:
        exit('Not in commands\n')

    if command == 'list':
        ls()
        exit()

    commands[command](args)


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        exit()
    execute()
