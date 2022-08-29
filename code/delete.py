import os
import csv
import hashlib
import pathlib

from .helper import root_path


def delete(file_name):

    if not file_name:
        exit("\n Needs more arguments \n")

    file_name = file_name[0]

    name_hash = hashlib.sha256(file_name.encode()).hexdigest()
    content_hash = []
    csv_fname = name_hash[:4] + '.csv'
    in_file = []
    files = os.listdir(root_path/'db')
    for file in files:
        if csv_fname == file:
            with open(root_path/'db'/csv_fname, 'r') as source:
                reader = csv.reader(source)
                for row in reader:
                    if row[0] == file_name:
                        content_hash = row[1]
                        in_file = file
                        break

    if len(content_hash) == 0:
        exit(f"\nNo file to delete: \n")

    csv_content = []
    with open(root_path/'db'/in_file, 'r') as source:
        reader = csv.reader(source)
        for row in reader:
            if row[0] != file_name:
                csv_content.append(row)
    if len(csv_content) != 1:
        with open(root_path/'db'/in_file, 'w') as source:
            csv_writer = csv.writer(source)
            for row in csv_content:
                csv_writer.writerow(row)

    pathlib.Path(root_path/'db'/in_file).unlink()

    content_path = root_path/'mydb'/content_hash[0]/content_hash[1]/content_hash[2]/content_hash[3]
    contents = os.listdir(content_path)
    for content in contents:
        splited_content = content.split('__')
        if content_hash == splited_content[0]:
            if int(splited_content[1]) != 0:
                old_name = content_path / str(content)
                new_name = content_path / str(
                splited_content[0] + "__" + str(int(splited_content[1]) - 1) + "__" + splited_content[2])
                os.rename(old_name, new_name)
                exit(f"\n File was successfully deleted : \n")
            (content_path / str(content)).unlink()
            exit(f"\n File was successfully deleted : \n")
