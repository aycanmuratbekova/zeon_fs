import csv

from .helper import zeon_path


def delete(file_name):

    if not file_name:
        exit("\n Needs more arguments \n")

    file_path = zeon_path / file_name[0]

    if not file_path.exists():
        exit("\n No file to delete : \n")

    file_path.unlink()

    file_list = []

    with open(zeon_path.parent / "code" / "file_list.csv", 'r') as source:
        reader = csv.reader(source)
        for row in reader:
            if file_name[0] not in row:
                file_list.append(row)

    with open(zeon_path.parent / "code" / "file_list.csv", 'w') as result:
        writer = csv.writer(result)
        for row in file_list:
            writer.writerow(row)

    print(f"\n File '{file_name[0]}' was successfully Deleted : \n")

