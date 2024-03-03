import sys
import unittest
from tests import data_tests
from floydwarshall.floyd_warshall import floyd_recursive

NO_PATH = sys.maxsize


class TestDatasets(unittest.TestCase):
    """Running unit tests. """

    def test_original(self):
        """Tests the original graph matrix. """
        self.assertEqual(floyd_recursive(data_tests.original_graph), data_tests.original_expected)

    def test_a(self):
        """test_a - 5x5 adjacency matrix. """
        self.assertEqual(floyd_recursive(data_tests.test_a), data_tests.a_expected)

    def test_b(self):
        """test_b - 8x8 adjacency matrix. """
        self.assertEqual(floyd_recursive(data_tests.test_b), data_tests.b_expected)

    def test_c(self):
        """test_c - float values. """
        self.assertEqual(floyd_recursive(data_tests.test_c), data_tests.c_expected)

    def test_d(self):
        """test_d - non-square adjacency matrix, expected error. """
        self.assertRaises(IndexError, floyd_recursive, data_tests.test_d)

    def test_e(self):
        """test_e - 16x16 adjacency matrix. """
        self.assertEqual(floyd_recursive(data_tests.test_e), data_tests.e_expected)


if __name__ == '__main__':
    unittest.main()
