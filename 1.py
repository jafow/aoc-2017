import unittest

"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

"""

def sum_all_matching_consecutive(digits):
    total = 0
    for num in range(0, len(digits) - 1):
        if digits[num] == digits[num + 1]:
            total += int(digits[num])
    if digits[0] == digits[len(digits) - 1]:
        total += int(digits[0])
    return total

def sum_matching (x, y):
    if x == y:
        return int(x)
    else:
        return 0

def sum_all_matching_consecutive(digits):
    """ take a string of digits and return the sum of all consecutive matching digits; it counts if digits[0] matches digits[len - 1] """
    return sum([int(digits[x]) for x in range(0, len(digits) - 1) if digits[x] == digits[x + 1]]) + sum_matching(digits[0], digits[len(digits) - 1])


# Tests
class TestSumOfAllMatchingNeighboringDigits(unittest.TestCase):
    def test_sums_all_matching_digits(self):
        self.assertEqual(sum_all_matching_consecutive('1122'), 3)
        self.assertEqual(sum_all_matching_consecutive('1111'), 4)
        self.assertEqual(sum_all_matching_consecutive('1234'), 0)

    def test_sums_all_digits_in_circular_list(self):
        self.assertEqual(sum_all_matching_consecutive('91212129'), 9)
        self.assertEqual(sum_all_matching_consecutive('123456891'), 1)
        self.assertEqual(sum_all_matching_consecutive('023456890'), 0)
        self.assertEqual(sum_all_matching_consecutive('11'), 2)

    def test_sums_zero_when_no_matches_exist(self):
        self.assertEqual(sum_all_matching_consecutive('0123456789876543212345678987654321'), 0)
        self.assertEqual(sum_all_matching_consecutive('01'), 0)

    def test_sums_short_digits(self):
        self.assertEqual(sum_all_matching_consecutive('110'), 1)


if __name__ == '__main__':
    unittest.main()


def output():
    f = open('./input/1.txt')
    digits = f.read().strip()
    print(sum_all_matching_consecutive(digits))
output()
