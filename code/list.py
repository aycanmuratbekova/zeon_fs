from btree.btree import TrieNode
from .helper import root_path, read_from_db


def ls(arg):

    names = read_from_db(root_path/'btree/list.pickle')
    tree_node = TrieNode(names)
    files = tree_node.search(arg)
    if len(files) == 0:
        print("\nNot fount any files: \n")
    else:
        for f in files:
            print(f)

