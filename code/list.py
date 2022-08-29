import csv
import os
from .helper import root_path


def ls():

    files = os.listdir(root_path/'db')
    for file in files:
        with open(root_path/'db'/file, 'r') as source:
            reader = csv.reader(source)
            for row in reader:
                print(row[0], row[2])

    """
    files = os.listdir(zeon_path)
    for file in files:
        print(file, "  -  ", os.path.getsize(zeon_path/file))
    """
