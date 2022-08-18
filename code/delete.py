import pathlib
import shutil
from .helper import get_existing_files, zeon_path


def move(args):

    dst_path = pathlib.Path.cwd() / 'deleted'

    existing_files = get_existing_files(args)

    if len(existing_files) == 0:
        exit(f'\nNo files to Delete :\n  {args}\n')

    for file_name in existing_files:
        shutil.move(zeon_path/file_name, dst_path/file_name)
        print(file_name)

    print('Was successfully Deleted:')
