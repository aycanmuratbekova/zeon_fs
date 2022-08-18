from .helper import get_existing_files, zeon_path


def create(args):

    existing_files = get_existing_files(args)
    created_files = []

    if len(existing_files) == len(args):
        exit(f"\nAll files Exists, can't rewrite :\n  {args}\n")

    for file in args:
        if file not in existing_files:
            file_path = zeon_path / file
            file_path.touch()
            created_files.append(file)

    if len(existing_files) != 0:
        print(existing_files, " : \n  This files Exists, can't rewrite :\n ")
    if len(created_files) != 0:
        print(created_files, " : \n  This files was successfully Created :\n ")

