from .init import init
from .list import ls
from .add2 import copy
from .delete import delete
from .helper import root_path


def ctl_add(file_name):
    if not file_name[0]:
        exit(f"\n Needs more arguments \n")
    if not (root_path / 'home' / file_name[0]).exists():
        exit(f"\nNo such file '{file_name[0]}' in the system, therefore we can't add it:\n")
    copy(file_name[0])


def ctl_delete(file_name):
    if not file_name:
        exit("\n Needs more arguments \n")
    delete(file_name[0])


def ctl_list(file_name):
    if len(file_name) == 0:
        ls('*')
    else:
        ls(file_name[0])


def ctl_init(file_name):
    init()


commands = {
    'add': ctl_add,
    'delete': ctl_delete,
    'list': ctl_list,
    'init': ctl_init,
}
