import os
import shutil
from datetime import datetime

from .helper import root_path, add_to_list
from .helper import read_from_db, write_to_db, get_hash, make_path


def copy(file_name):

    name_hash = get_hash(file_name)
    names = read_from_db(make_path(name_hash)/'names.pickle')

    if name_hash in names:
        exit(f"\n File with name: '{file_name}' exists can't add : \n")

    content_hash = get_hash(file_name, file=True)
    contents = read_from_db(make_path(content_hash)/'contents.pickle')

    if content_hash not in contents:
        shutil.copy(root_path/"home"/file_name, make_path(content_hash)/'files'/content_hash)

    names[name_hash] = [file_name, content_hash]
    write_to_db(make_path(name_hash)/'names.pickle', names)

    contents[content_hash] = contents.setdefault(content_hash, {})
    contents[content_hash][file_name] = [os.path.getsize(root_path/"home"/file_name), str(datetime.now())]
    write_to_db(make_path(content_hash)/'contents.pickle', contents)
    print(f"\n File '{file_name}' was successfully added : \n\n{contents}\n")
    add_to_list(file_name)
