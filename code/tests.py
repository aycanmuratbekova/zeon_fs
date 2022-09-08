from pathlib import Path
import unittest
import hashlib

from helper import root_path, create_path, get_hash


class HelperTestCase(unittest.TestCase):

    def test_get_hash(self):
        self.assertEqual(hashlib.sha256('index.html'.encode()).hexdigest(), get_hash('index.html'))


if __name__ == '__main__':
    unittest.main()
# python -m unittest tests.py
