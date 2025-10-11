import unittest
from .anagrams import group_anagrams

class TestGroupAnagrams(unittest.TestCase):
    def test_example_1(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = group_anagrams(input_strs)
        self.assertEqual(sorted([sorted(group) for group in result]), sorted([sorted(group) for group in expected]))

    def test_empty_list(self):
        self.assertEqual(group_anagrams([]), [])

    def test_no_anagrams(self):
        input_strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = group_anagrams(input_strs)
        self.assertEqual(sorted([sorted(group) for group in result]), sorted([sorted(group) for group in expected]))
        
    def test_all_anagrams(self):
        input_strs = ["listen", "silent", "enlist"]
        expected = [["listen", "silent", "enlist"]]
        result = group_anagrams(input_strs)
        self.assertEqual(sorted([sorted(group) for group in result]), sorted([sorted(group) for group in expected]))

if __name__ == '__main__':
    unittest.main()
