from .helper import delete_from_names, delete_from_content, delete_from_fs


def delete(file_name):

    content_hash = delete_from_names(file_name)

    has_copies = delete_from_content(content_hash, file_name)
    
    if not has_copies:
        delete_from_fs(content_hash)
        
    print(f" File was successfully deleted :")
