import os
import pathlib
import itertools
import pickle


fs_path = '/Users/aijanmuratbekova/pycharm_projects/fs/zeon_fs/fs/'
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
permutations = [p for p in itertools.product(x, repeat=4)]


def init():

    for i in permutations:

        names = fs_path + '/'.join(i) + '/names.pickle'
        os.makedirs(os.path.dirname(names), exist_ok=True)
        with open(names, 'wb') as file:
            pickle.dump({}, file)

        content = fs_path + '/'.join(i) + '/content.pickle'
        with open(content, 'wb') as file:
            pickle.dump({}, file)

