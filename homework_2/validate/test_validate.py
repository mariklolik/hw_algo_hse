import unittest
from validate import validate_stack_sequences

class TestValidateStackSequences(unittest.TestCase):
    def test_example_1(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_example_2(self):
        pushed = [1, 2, 3]
        popped = [3, 1, 2]
        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_empty_sequences(self):
        self.assertTrue(validate_stack_sequences([], []))

    def test_single_element_valid(self):
        self.assertTrue(validate_stack_sequences([1], [1]))

    def test_single_element_invalid(self):
        self.assertFalse(validate_stack_sequences([1], [2]))

    def test_all_pushed_then_popped(self):
        pushed = [1, 2, 3]
        popped = [3, 2, 1]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_reverse_order(self):
        pushed = [1, 2, 3, 4]
        popped = [4, 3, 2, 1]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_complex_case(self):
        pushed = [2, 1, 0, 3]
        popped = [0, 3, 2, 1]
        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_complex_valid_case(self):
        pushed = [0, 1, 2, 3]
        popped = [0, 2, 1, 3]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_different_lengths(self):
        pushed = [1, 2, 3]
        popped = [1, 2]
        # This should return False since lengths don't match
        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_large_input(self):
        # Test with input size close to the limit
        n = 1000
        pushed = list(range(n))
        popped = list(range(n))
        self.assertTrue(validate_stack_sequences(pushed, popped))

if __name__ == '__main__':
    unittest.main()
