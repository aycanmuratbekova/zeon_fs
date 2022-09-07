from .init import init
from .list import ls
from .add2 import copy
from .delete import delete
from .helper import root_path


def ctl_add(file_name):
    file_name = file_name[0]
    if not file_name:
        exit(f"\n Needs more arguments \n")

    if not (root_path / 'home' / file_name).exists():
        exit(f"\nThere is no such file '{file_name}' in the system, therefore we cannot add it to the file system:\n")

    copy(file_name)


def ctl_delete(file_name):
    delete(file_name)


def ctl_list(file_name):
    ls()


def ctl_init(file_name):
    init()


commands = {
    'add': ctl_add,
    'delete': ctl_delete,
    'list': ctl_list,
    'init': ctl_init,
}