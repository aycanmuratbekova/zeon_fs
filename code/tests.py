from pathlib import Path
import unittest
import hashlib

from helper import root_path, create_path, get_hash


class HelperTestCase(unittest.TestCase):
    def test_create_path(self):
        path_content = create_path('index.html', content=True,
                                   fs_path=Path('/Users/aijanmuratbekova/pycharm_projects/fs/zeon_fs/test_fs'))
        self.assertEqual((root_path/'test_fs/fs/5/9/4/a/content.pickle').exists(), path_content.exists())

    def test_get_hash(self):
        self.assertEqual(hashlib.sha256('index.html'.encode()).hexdigest(), get_hash('index.html'))


if __name__ == '__main__':
    unittest.main()
# python -m unittest tests.py
