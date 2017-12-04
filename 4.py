import unittest

"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many
passphrases are valid?
"""


# read each line

# make a trie!

# brute force?
# read each line in as a set
# split on the word, sort
# return uniq(list)

# Tests
class TestSpiralOut(unittest.TestCase):
    def test_square_one_to_itself(self):
        self.assertEqual()

    def test_counts_from_point_around_a_corner(self):
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()

    def test_counts_from_diagonal(self):
        self.assertEqual()
        self.assertEqual()

    def test_large_distance(self):
        self.assertEqual()
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
