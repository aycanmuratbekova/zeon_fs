import shutil

from .helper import root_path, add_to_list
from .helper import update_names, update_contents, get_data_to_add


def copy(file_name: str):

    name_hash, path_to_names, names = get_data_to_add(file_name, 'names.pickle', file=False)

    if name_hash in names:
        exit(f"\n File with name: '{file_name}' exists can't add : \n")

    content_hash, path_to_contents, contents = get_data_to_add(file_name, 'names.pickle', file=True)

    if content_hash not in contents:
        shutil.copy(root_path / "home" / file_name, path_to_contents.parent/'files'/content_hash)

    update_names(content_hash, file_name, name_hash, names, path_to_names)
    update_contents(content_hash, contents, file_name, path_to_contents)
    print(f"\n File '{file_name}' was successfully added: \n")
    add_to_list(file_name)
