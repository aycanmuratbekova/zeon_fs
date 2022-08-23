import pathlib
import hashlib
import csv


zeon_path = pathlib.Path(__file__).parent.parent / 'zeon_fs'


def add_file_hash(file_name: str) -> bool:
    added = False
    file_path = zeon_path.parent / 'home' / file_name
    with open(file_path, 'rb') as opened_file:
        content = opened_file.read()
    md5 = hashlib.md5()
    md5.update(content)

    file_hash = md5.hexdigest()

    with open(zeon_path.parent / "code" / "file_list.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row, "   =>  ", md5.hexdigest())
            if file_hash == row[1]:
                print("ISSOYO")
                added = True
                break

    file_hash = [file_name, str(md5.hexdigest())]
    with open(zeon_path.parent / "code" / "file_list.csv", 'a') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(file_hash)

    return added
