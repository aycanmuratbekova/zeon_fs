from datetime import datetime
import hashlib
import pickle
import shutil

from .helper import root_path


def copy(file_name):

    name_hash = hashlib.sha256(file_name.encode()).hexdigest()

    content = open(root_path / 'home' / file_name, 'rb').read()
    content_hash = hashlib.sha256(content).hexdigest()

    path_to_names = root_path / 'fs' / '/'.join(str(name_hash[:4])) / 'names.pickle'
    path_to_content = root_path / 'fs' / '/'.join(str(content_hash[:4])) / 'content.pickle'

    with open(path_to_names, 'rb') as file:
        names = pickle.load(file)

    if name_hash in names:
        exit(f"\n File with name: '{file_name}' exists can't add : \n")

    content_hashes = pickle.load(open(path_to_content, 'rb'))

    if content_hash not in content_hashes:
        name_suffix = file_name.split('.')
        name = content_hash + "." + name_suffix[1]
        shutil.copy(root_path / "home" / file_name, path_to_content.parent / name)

    content_hashes[content_hash] = content_hashes.setdefault(content_hash, []) +\
        [file_name, (root_path/'home'/file_name).stat().st_size, datetime.now().strftime("%m/%d/%Y, %H:%M:%S")]
    with open(path_to_content, 'wb') as file:
        pickle.dump(content_hashes, file)

    names[name_hash] = file_name
    with open(path_to_names, 'wb') as file:
        pickle.dump(names, file)

    exit(f"\n File '{file_name}' was successfully added : \n")


