import os
import hashlib
import csv
import shutil

from .helper import root_path


def copy(file_name):

    if not file_name:
        exit("\n Needs more arguments \n")

    file_name = file_name[0]
    name_hash = hashlib.sha256(file_name.encode()).hexdigest()
    csv_fname = name_hash[:4] + '.csv'
    with open(root_path / 'home' / file_name, 'rb') as opened_file:
        content = opened_file.read()
        content_hash = hashlib.sha256(content).hexdigest()

    if (root_path/'db'/csv_fname).exists():
        with open(root_path/'db'/csv_fname, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == file_name:
                    exit(f"\n File with name: '{file_name}' exists can't add : \n")

        with open(root_path/'db'/csv_fname, 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([file_name, content_hash, os.path.getsize(root_path/'home'/file_name)])

    (root_path / 'db' / csv_fname).touch()
    with open(root_path / 'db' / csv_fname, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([file_name, content_hash, os.path.getsize(root_path/'home'/file_name)])

    file_path = root_path/'mydb'/content_hash[0]/content_hash[1]/content_hash[2]/content_hash[3]

    if not file_path.exists():
        file_path.mkdir(parents=True, exist_ok=True)
        name_suffix = file_name.split('.')
        name = content_hash + '__0__.' + name_suffix[1]
        shutil.copy(root_path / "home" / file_name, file_path/name)
        exit(f"\n File was successfully added : \n")

    files = os.listdir(file_path)
    for file in files:
        file_text = str(file).split('__')
        if file_text[0] == content_hash:
            old_name = file_path/str(file)
            new_name = file_path/str(file_text[0]+"__"+str(int(file_text[1])+1)+"__"+file_text[2])
            os.rename(old_name, new_name)
            exit(f"\n File was successfully added : \n")

    name_suffix = file_name.split('.')
    name = content_hash + '__0__.' + name_suffix[1]
    shutil.copy(root_path / "home" / file_name, file_path/name)
    exit(f"\n File was successfully added : \n")
