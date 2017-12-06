import unittest
import pdb
import utils as u

"""
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory
reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any
number of blocks. The goal of the reallocation routine is to balance the
blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the
memory bank with the most blocks (ties won by the lowest-numbered memory bank)
and redistributes those blocks among the banks. To do this, it removes all of
the blocks from the selected bank, then moves to the next (by index) memory
bank and inserts one of the blocks. It continues doing this until it runs out
of blocks; if it reaches the last memory bank, it wraps around to the first
one.

The debugger would like to know how many redistributions can be done before a
blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most
blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first
bank, the second bank, and so on, the 7 blocks are spread out over the memory
banks. The fourth, first, and second banks get two blocks each, and the third
bank gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four).
Because there are four memory banks, each gets one block. The result is: 3 1 2
3.

Now, there is a tie between the first and fourth memory banks, both of which
have three blocks. The first bank wins the tie, and its three blocks are
distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each
of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was already
seen. The infinite loop is detected after the fifth block redistribution cycle,
and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution
cycles must be completed before a configuration is produced that has been seen
before?
"""

INPUT = '5  1   10  0   1   7   13  14  3   12  8   10  7   12  0   6'


def redist_cycles(B):
    """ take a list `B` of ints and return the sum of redist cycles """
    state = list(map(int, u.split_strip(B)))
    seen = set()
    L = len(state) - 1
    # pdb.set_trace()
    cycles = 0
    i = 0

    while True:
        print('hit')
        if str(state) in seen:
            return 1
        elif i == L:
            i = 0
            cycles += 1
            yield cycles
        else:
            # redistribute
            max_idx, max_val = max(enumerate(state), key=lambda x: x[1])
            state[max_idx] = 0

            # reset i if max_idx is at end of list
            if max_idx == L:
                i = 0
            else:
                i = max_idx + 1

            for j in range(0, max_val):
                if i == L:
                    i = 0

                state[i] += 1
                i += 1

            seen.add(str(state))
            cycles += 1
            yield cycles


class TestDay6(unittest.TestCase):
    def test_should_count_jumps(self):
        c = sum(x for x in redist_cycles('0  2   7  0'))
        self.assertEqual(c, 5)


if __name__ == '__main__':
    unittest.main()
