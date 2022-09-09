import os
import shutil
from datetime import datetime

from .helper import root_path
from .helper import read_from_db, write_to_db, get_hash, make_path


def copy(file_name):

    name_hash = get_hash(file_name)

    path_to_names = make_path(name_hash)/'names.pickle'

    names = read_from_db(path_to_names)
    if name_hash in names:
        exit(f"\n File with name: '{file_name}' exists can't add : \n")

    content_hash = get_hash(file_name, file=True)

    path_to_contents = make_path(content_hash)/'contents.pickle'

    contents = read_from_db(path_to_contents)

    if content_hash not in contents:
        print(f"\ncontent_hash not in contents : {content_hash not in contents}\n")
        shutil.copy(root_path / "home" / file_name, path_to_contents.parent/'files'/content_hash)

    names[name_hash] = [file_name, content_hash]
    write_to_db(path_to_names, names)

    contents[content_hash] = contents.setdefault(content_hash, {})
    contents[content_hash][file_name] = [os.path.getsize(root_path/"home"/file_name), str(datetime.now())]
    write_to_db(path_to_contents, contents)

    print(f"\n File '{file_name}' was successfully added : \n\n{contents}\n")
