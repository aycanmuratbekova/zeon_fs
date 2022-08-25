import os
import pathlib
import hashlib
import csv


zeon_path = pathlib.Path(__file__).parent.parent / 'zeon_fs'
from_path = pathlib.Path(__file__).parent.parent / 'home'


def add_file_hash(file_name: str) -> bool:
    such_hash_exists = False
    file_path = zeon_path.parent / 'home' / file_name
    with open(file_path, 'rb') as opened_file:
        content = opened_file.read()
    md5 = hashlib.md5()
    md5.update(content)

    file_hash = md5.hexdigest()

    with open(zeon_path.parent / "code" / "file_list.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if len(row) == 0:
                break
            if file_hash == row[1]:
                such_hash_exists = True
                break

    file_hash = [file_name, str(md5.hexdigest())]
    with open(zeon_path.parent / "code" / "file_list.csv", 'a') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(file_hash)

    if such_hash_exists:
        os.symlink(from_path/file_name, zeon_path / file_name)

    return such_hash_exists
