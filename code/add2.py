import shutil

from .helper import root_path
from .helper import create_path, read_from, write_to, get_hash, add_hash_to_dict, rename


def copy(file_name):

    name_hash = get_hash(file_name)
    path_to_names = create_path(file_name)

    names = read_from(path_to_names)

    if name_hash in names:
        exit(f"\n File with name: '{file_name}' exists can't add : \n")

    names[name_hash] = file_name
    write_to(path_to_names, names)

    content_hash = get_hash(file_name, file=True)
    path_to_content = create_path(file_name, content=True)
    content_hashes = read_from(path_to_content)

    if content_hash not in content_hashes:
        shutil.copy(root_path / "home" / file_name, path_to_content.parent / rename(file_name, content_hash))

    hashes_dict = add_hash_to_dict(content_hashes, file_name, content_hash)

    write_to(path_to_content, hashes_dict)

    exit(f"\n File '{file_name}' was successfully added : \n")

