from .helper import delete_from_names, delete_content


def delete(file_name):

    content_hash = delete_from_names(file_name)

    delete_content(content_hash, file_name)
