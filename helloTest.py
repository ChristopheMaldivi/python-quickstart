"""
    python -m unittest helloTest.py
    python -m unittest helloTest.HelloTest.test_env
"""
import unittest

from hello import Hello


class HelloTest(unittest.TestCase):

    def test_env(self):
        self.assertEqual(Hello().hello(), "hello python")


if __name__ == '__main__':
    unittest.main()
