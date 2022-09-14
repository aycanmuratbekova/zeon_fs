from .helper import file_name_exists, delete_from_list
from .helper import get_data_for_del, get_hash, delete_from_names, delete_copies, delete_content


def delete(file_name):

    if not file_name_exists(file_name):
        exit(f"\nNo file to delete: \n")

    name_hash = get_hash(file_name)
    path_to_names, names, content_hash = get_data_for_del(name_hash, 'names.pickle')

    delete_from_names(names, name_hash, path_to_names)
    delete_from_list(file_name)

    content_hash = content_hash[1]
    path_to_content, content, hashes = get_data_for_del(content_hash, 'contents.pickle')

    if len(hashes) > 1:
        delete_copies(hashes, file_name, content, content_hash, path_to_content)
        exit(f" File was successfully deleted :")

    delete_content(content, content_hash, path_to_content)
    print(f" File was successfully deleted :")
