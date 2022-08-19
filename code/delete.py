from .helper import zeon_path


def delete(file_name):

    if not file_name:
        exit("\n Needs more arguments \n")

    file_path = zeon_path / file_name[0]

    if not file_path.exists():
        exit("\n No file to delete : \n")

    file_path.unlink()
    print(f"\n File '{file_name[0]}' was successfully Deleted : \n")
