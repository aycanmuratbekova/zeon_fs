import sys
from code.list import ls
from code.create import create
from code.delete import move


commands = {
    'create': create,
    'delete': move,
    'list': ls
}

commands_arg = {
    'zero_argument': ['list'],
    'min_one_argument': ['delete', 'create']
}


def execute():

    _, command, *args = sys.argv

    if command not in commands:
        exit('Not in commands\n')

    if command in commands_arg['min_one_argument'] and len(args) < 1:
        exit('Need more arguments\n')

    if command in commands_arg['zero_argument']:
        commands[command]()

    if command in commands_arg['min_one_argument']:
        commands[command](args)


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        exit()
    execute()
