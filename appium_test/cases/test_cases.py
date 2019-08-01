# coding:utf-8
import unittest

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass--------")

    @classmethod
    def tearDownClass(cls):
        print(teardownclass-----)

    def test_user(self):
        print("test_user--------")

    def test_password(self):
        print(test_password--------")


if __name__ == '__main__':
    test = TestCase()
    test.run()

