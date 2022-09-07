import os
import pathlib
import pickle
import hashlib
from datetime import datetime


root_path = pathlib.Path(__file__).parent.parent


def create_path(file_name: str, content=False, fs_path=root_path) -> pathlib.Path:
    if content:
        hash_str = get_hash(str(fs_path/'home'/file_name), True)
        path_to = fs_path / 'fs' / '/'.join(str(hash_str[:4])) / 'content.pickle'
    else:
        hash_str = get_hash(file_name)
        path_to = fs_path / 'fs' / '/'.join(str(hash_str[:4])) / 'names.pickle'

    if not path_to.exists():
        os.makedirs(os.path.dirname(path_to), exist_ok=True)
        with open(path_to, 'wb') as file:
            pickle.dump({}, file)
    return path_to


def read_from(path_to: pathlib.Path) -> dict:
    with open(path_to, 'rb') as file:
        names = pickle.load(file)
    return names


def write_to(path_to: pathlib.Path, content: dict) -> str:
    with open(path_to, 'wb') as file:
        pickle.dump(content, file)
    return 'ok'


def get_hash(file_name: str, file=False) -> str:
    if file:
        filebytes = (root_path / "home" / file_name).read_bytes()
        hashed_text = hashlib.sha256(filebytes).hexdigest()
    else:
        hashed_text = hashlib.sha256(file_name.encode()).hexdigest()
    return hashed_text


def rename(file_name, content_hash):
    name_suffix = file_name.split('.')
    name = content_hash + "." + name_suffix[1]
    return name


def add_hash_to_dict(content_hashes, file_name, content_hash):
    content_hashes[content_hash] = content_hashes.setdefault(content_hash, []) +\
        [file_name, get_file_size(file_name), get_creation_date()]
    return content_hashes


def get_file_size(file_name: str) -> str:
    file_size = str((root_path / 'home' / file_name).stat().st_size)
    return file_size


def get_creation_date() -> str:
    dt = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return dt


dict_list = {}

