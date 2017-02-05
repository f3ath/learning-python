import unittest

from fibonacci import fibonacci, NumberLengthChecker

class TestFibonacci(unittest.TestCase):

    def test_first_7_numbers_match_expected(self):
        fibo = fibonacci()
        for n in [1, 1, 2, 3, 5, 8, 13]:
            self.assertEqual(n, next(fibo))

class TestNumberLengthChecker(unittest.TestCase):
    def test_can_create(self):
        length = NumberLengthChecker(1)

    def test_length_1_sufficient_for_all(self):
        checker = NumberLengthChecker(1)
        self.assertTrue(checker.is_long_enough(1))

    def test_length_2(self):
        checker = NumberLengthChecker(2)
        for n in [0, 1, 2, 8, 9]:
            self.assertFalse(checker.is_long_enough(n))
        for n in [10, 123, 99]:
            self.assertTrue(checker.is_long_enough(n))

if __name__ == '__main__':
    unittest.main()