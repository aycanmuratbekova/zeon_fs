import sys

from code.controllers import commands


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        exit()

    _, command, *args = sys.argv

    if command not in commands:
        exit('Not in commands\n')

    commands[command](args)
