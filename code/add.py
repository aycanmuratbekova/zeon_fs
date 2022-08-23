import shutil

from .helper import add_file_hash, zeon_path


def copy(file_name):

    if not file_name:
        exit("\n Needs more arguments \n")

    home_path = zeon_path.parent / 'home' / file_name[0]
    file_path = zeon_path / file_name[0]

    if not home_path.exists():
        exit("\n No file to add : \n")

    if file_path.exists():
        exit("\n can't add - file already exists  : \n")

    if add_file_hash(file_name[0]):
        exit("\n File was successfully added : \n")

    shutil.copy(home_path, zeon_path/file_name[0])
    print("\n File was successfully added : \n")
