import BinarySearch
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(BinarySearch.binary_search(
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
