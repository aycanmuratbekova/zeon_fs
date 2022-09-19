import pathlib
import pickle
import hashlib
import os
from datetime import datetime

from .btree import add, delete


root_path = pathlib.Path(__file__).parent.parent


def get_data_to_add(file_name, db_name, file=False):
    hash_text = get_hash(file_name, file)
    path_to_db = make_path(hash_text) / db_name
    db_data = read_from_db(path_to_db)
    return hash_text, path_to_db, db_data


def update_names(content_hash, file_name, name_hash, names, path_to_names):
    names[name_hash] = [file_name, content_hash]
    write_to_db(path_to_names, names)


def update_contents(content_hash, contents, file_name, path_to_contents):
    contents[content_hash] = contents.setdefault(content_hash, {})
    contents[content_hash][file_name] = [os.path.getsize(root_path / "home" / file_name), str(datetime.now())]
    write_to_db(path_to_contents, contents)


def file_name_exists(file_name: str) -> bool:
    name_hash = get_hash(file_name)
    path_to_names = make_path(name_hash) / 'names.pickle'
    if not path_to_names.exists():
        return False
    names = read_from_db(path_to_names)
    return name_hash in names


def get_data_for_del(hash_text, db_name):
    path_to_db = make_path(hash_text) / db_name
    data_dict = read_from_db(path_to_db)
    searched_data = data_dict[hash_text]
    return path_to_db, data_dict, searched_data


def delete_from_names(names, name_hash, path_to_names):
    del names[name_hash]
    write_to_db(path_to_names, names)


def delete_content(content, content_hash, path_to_content):
    content.pop(content_hash)
    write_to_db(path_to_content, content)
    path_to_file = make_path(content_hash) / 'files' / content_hash
    path_to_file.unlink()


def delete_copies(hashes, file_name, content, content_hash, path_to_content):
    hashes.pop(file_name)
    content[content_hash] = hashes
    write_to_db(path_to_content, content)


def make_path(name_hash) -> pathlib.Path:
    path_to = root_path / 'fs' / '/'.join(str(name_hash[:4]))
    return path_to


def get_hash(file_name: str, file=False) -> str:
    if file:
        filebytes = (root_path / "home" / file_name).read_bytes()
        hashed_text = hashlib.sha256(filebytes).hexdigest()
    else:
        hashed_text = hashlib.sha256(file_name.encode()).hexdigest()
    return hashed_text


def write_to_db(path_to: pathlib.Path, content: dict):
    if not path_to.exists():
        (path_to.parent/'files').mkdir(parents=True, exist_ok=True)
        with open(path_to, 'wb') as file:
            pickle.dump({}, file)
    with open(path_to, 'wb') as file:
        pickle.dump(content, file)


def read_from_db(path_to: pathlib.Path) -> dict:
    if not path_to.exists():
        (path_to.parent/'files').mkdir(parents=True, exist_ok=True)
        with open(path_to, 'wb') as file:
            pickle.dump({}, file)
    with open(path_to, 'rb') as file:
        names = pickle.load(file)
    return names


def add_to_list(file_name):
    path_to_list = root_path/'btree/list.pickle'
    if not path_to_list.exists():
        #path_to_list.parent.mkdir(parents=True, exist_ok=True)
        with open(path_to_list, 'wb') as file:
            pickle.dump([], file)

    with open(path_to_list, 'rb') as file:
        names_list = pickle.load(file)

    names_list.append(file_name)
    with open(path_to_list, 'wb') as file:
        pickle.dump(names_list, file)


def delete_from_list(file_name):
    path_to_list = root_path/'btree/list.pickle'

    with open(path_to_list, 'rb') as file:
        names_list = pickle.load(file)
    new_list = []
    for fname in names_list:
        if fname != file_name:
            new_list.append(fname)

    with open(path_to_list, 'wb') as file:
        pickle.dump(new_list, file)


def add_to_tree(file_name):
    path_to = pathlib.Path('/Users/aijanmuratbekova/pycharm_projects/fs/zeon_fs/code/btree.pickle')
    if not path_to.exists():
        with open(path_to, 'wb') as file:
            pickle.dump({}, file)

    with open(path_to, 'rb') as file:
        btree = pickle.load(file)

    add(file_name, btree)

    with open(path_to, 'wb') as file:
        pickle.dump(btree, file)


def delete_from_tree(file_name):
    path_to = pathlib.Path('/Users/aijanmuratbekova/pycharm_projects/fs/zeon_fs/code/btree.pickle')

    with open(path_to, 'rb') as file:
        btree = pickle.load(file)

    delete(file_name, btree)

    with open(path_to, 'wb') as file:
        pickle.dump(btree, file)







