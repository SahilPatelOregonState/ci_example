import unittest
from task import my_func


class Testcase(unittest.TestCase):
    def test1(self):
        expected = "Hello World!"
        self.assertEqual(expected, my_func())


if __name__ == '__main__':
    unittest.main()
