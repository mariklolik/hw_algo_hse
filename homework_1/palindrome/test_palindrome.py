import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_single_digit(self):
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(5))
        self.assertTrue(is_palindrome(9))
    
    def test_two_digit_palindromes(self):
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(22))
        self.assertTrue(is_palindrome(99))
    
    def test_two_digit_non_palindromes(self):
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(31))
        self.assertFalse(is_palindrome(45))
    
    def test_three_digit_palindromes(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(131))
        self.assertTrue(is_palindrome(999))
    
    def test_three_digit_non_palindromes(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(456))
        self.assertFalse(is_palindrome(789))
    
    def test_larger_palindromes(self):
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(1234321))
    
    def test_larger_non_palindromes(self):
        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome(5678))
        self.assertFalse(is_palindrome(12345))
    
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(0))
        self.assertFalse(is_palindrome(-1))
        self.assertFalse(is_palindrome(-121))
    
    def test_examples_from_task(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(31))


if __name__ == '__main__':
    unittest.main()
