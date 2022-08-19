import pathlib


zeon_path = pathlib.Path(__file__).parent.parent / 'zeon_fs'


def get_existing_files(args):
    existing_files = []
    for arg in args:
        file_path = zeon_path / arg
        if file_path.exists():
            existing_files.append(file_path.name)

    return existing_files





