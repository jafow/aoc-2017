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


def all_unique(line):
    """ returns True if line contains all unique words, False if not """
    return len(list(line)) == len(set(line))


def list_lines(file_object):
    return map(split_strip, file_object)


def split_strip(line):
    """ map a line from a file object to a list of 'words' split on (not necessarily uniform!) spaces """
    return list(filter(lambda x: x != '', line.strip().split(' ')))


def valid_passphrases(f):
    """ return a sum of all unique words in a file object f """
    lines = f.readlines()
    xs = list(filter(all_unique, list_lines(lines)))
    f.close()
    return len(xs)

f = open('./input/4.txt')
v = valid_passphrases(f)
print('Result: {}'.format(v))

# Tests
class TestCountUniqueWords(unittest.TestCase):

    def test_should_count_all_when_every_line_is_unique(self):
        mock_2 = open('./test/4_0mock.txt')
        self.assertEqual(valid_passphrases(mock_2), 6)

    def test_only_counts_one_for_lines_with_filled_repeats(self):
        mock_1 = open('./test/4_1mock.txt')
        self.assertEqual(valid_passphrases(mock_1), 3)

    def test_only_counts_unique_words(self):
        mock = open('./test/4_2mock.txt')
        self.assertEqual(valid_passphrases(mock), 2)


if __name__ == '__main__':
    unittest.main()
