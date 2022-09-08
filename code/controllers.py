from .init import init
from .list import ls
from .add import copy
from .delete import delete
from .helper import root_path, file_name_exists


def ctl_add(file_name):
    file_name = file_name[0]
    if not file_name:
        exit(f"\n Needs more arguments \n")

    if not (root_path / 'home' / file_name).exists():
        exit(f"\nNo such file '{file_name}' in the system, therefore we can't add it:\n")

    copy(file_name)


def ctl_delete(file_name):
    if not file_name:
        exit("\n Needs more arguments \n")

    if not file_name_exists(file_name[0]):
        exit(f"\nNo file to delete: \n")

    delete(file_name[0])


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
