import csv
import os
from .helper import zeon_path


def ls():
    with open(zeon_path.parent / "code" / "file_list.csv", 'r') as source:
        reader = csv.reader(source)
        for row in reader:
            print(row[0], "  -  ", os.path.getsize(zeon_path / row[0]))

"""
    files = os.listdir(zeon_path)
    for file in files:
        print(file, "  -  ", os.path.getsize(zeon_path/file))
"""
