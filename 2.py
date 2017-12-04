import unittest

"""
For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
"""


def checksums(rows):
    # read each row
    # difference between min & max
    # sum differences
    res = [list(map(int, row)) for row in rows]
    return sum(max(row) - min(row) for row in res)

def setup():
    f = open('input2.txt', 'r')
    rows = [row.rstrip().split('\t') for row in f.readlines()]
    print(checksums(rows))


setup()
# Tests
class TestCheckSums(unittest.TestCase):
    def test_sums_row_min_max_differences(self):
        self.assertEqual(checksums([[1, 2, 3], [5, 2, 4]]), 5)
        self.assertEqual(checksums([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]), 18)

if __name__ == '__main__':
    unittest.main()
