import unittest
from prime_count import count_primes


class TestPrimeCount(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(count_primes(10), 4)
    
    def test_example_2(self):
        self.assertEqual(count_primes(1), 0)
    
    def test_edge_cases(self):
        self.assertEqual(count_primes(0), 0)
        self.assertEqual(count_primes(2), 0)
        self.assertEqual(count_primes(3), 1)
    
    def test_small_numbers(self):
        self.assertEqual(count_primes(4), 2)
        self.assertEqual(count_primes(5), 2)
        self.assertEqual(count_primes(6), 3)
        self.assertEqual(count_primes(7), 3)
        self.assertEqual(count_primes(8), 4)
        self.assertEqual(count_primes(9), 4)
    
    def test_medium_numbers(self):
        self.assertEqual(count_primes(20), 8)
        self.assertEqual(count_primes(30), 10)
        self.assertEqual(count_primes(50), 15)
        self.assertEqual(count_primes(100), 25)
    
    def test_larger_numbers(self):
        self.assertEqual(count_primes(200), 46)
        self.assertEqual(count_primes(500), 95)
        self.assertEqual(count_primes(1000), 168)
    
    def test_boundary_values(self):
        self.assertEqual(count_primes(11), 4)
        self.assertEqual(count_primes(12), 5)
        self.assertEqual(count_primes(13), 5)
        self.assertEqual(count_primes(14), 6)
        self.assertEqual(count_primes(15), 6)
        self.assertEqual(count_primes(16), 6)
        self.assertEqual(count_primes(17), 6)
        self.assertEqual(count_primes(18), 7)
        self.assertEqual(count_primes(19), 7)
        self.assertEqual(count_primes(20), 8)


if __name__ == '__main__':
    unittest.main()
