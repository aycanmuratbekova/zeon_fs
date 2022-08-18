import os
from .helper import zeon_path


def ls():
    files = os.listdir(zeon_path)
    for file in files:
        print(file)
