import pathlib
import pickle
import hashlib


root_path = pathlib.Path(__file__).parent.parent


def create_db(path_to: pathlib.Path) -> bool:
    if not path_to.exists():
        (path_to.parent/'files').mkdir(parents=True, exist_ok=True)
        with open(path_to, 'wb') as file:
            pickle.dump({}, file)
    return True


def read_from_db(path_to: pathlib.Path) -> dict:
    with open(path_to, 'rb') as file:
        names = pickle.load(file)
    return names


def write_to_db(path_to: pathlib.Path, content: dict) -> str:
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


def make_path(name_hash) -> pathlib.Path:
    path_to = root_path / 'fs' / '/'.join(str(name_hash[:4]))
    return path_to


def file_name_exists(file_name: str) -> bool:

    name_hash = get_hash(file_name)
    path_to_names = make_path(name_hash) / 'names.pickle'
    if not path_to_names.exists():
        return False
    names = read_from_db(path_to_names)
    return name_hash in names


def delete_from_names(file_name) -> str:
    name_hash = get_hash(file_name)
    path_to_names = make_path(name_hash) / 'names.pickle'

    names = read_from_db(path_to_names)
    content_hash = names[name_hash]
    del names[name_hash]

    write_to_db(path_to_names, names)

    return content_hash[1]


def delete_from_content(content_hash: str, file_name: str) -> bool:
    path_to_content = make_path(content_hash) / 'contents.pickle'
    content = read_from_db(path_to_content)

    hashes = content[content_hash]

    if len(hashes) == 1:
        content.pop(content_hash)
        write_to_db(path_to_content, content)
        return False

    hashes.pop(file_name)
    content[content_hash] = hashes
    write_to_db(path_to_content, content)
    return True


def delete_from_fs(content_hash: str) -> None:
    path_to_file = make_path(content_hash) / 'files' / content_hash
    path_to_file.unlink()



