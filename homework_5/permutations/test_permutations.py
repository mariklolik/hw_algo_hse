import unittest

from homework_5.permutations import permute


class TestPermutations(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(permute([1]), [[1]])

    def test_two_elements(self):
        expected = [[0, 1], [1, 0]]
        self.assertCountEqual(permute([0, 1]), expected)

    def test_three_elements(self):
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        self.assertCountEqual(permute([1, 2, 3]), expected)

    def test_non_numeric(self):
        values = ["a", "b"]
        expected = [["a", "b"], ["b", "a"]]
        self.assertCountEqual(permute(values), expected)

    def test_empty(self):
        self.assertEqual(permute([]), [[]])


if __name__ == "__main__":
    unittest.main()

