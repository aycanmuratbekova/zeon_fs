import pickle
from pathlib import Path as p
from .btree import search


def ls(arg):
    path_to = p('/Users/aijanmuratbekova/pycharm_projects/fs/zeon_fs/code/btree.pickle')
    with open(path_to, 'rb') as file:
        trie = pickle.load(file)
    names = search(arg, trie)
    if len(names) == 0:
        exit(f"\nEmpty\n")
    for name in names:
        print(name)

