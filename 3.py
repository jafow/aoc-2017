import unittest

"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data
must be carried back to square 1 (the location of the only access port for this
memory system) by programs that can only move up, down, left, or right. They
always take the shortest path: the Manhattan Distance between the location of
the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?
"""


N = 368078

def turn_corner(x, y, term):
    """
    return coordinates based off of relationship of both x & y to each
    other and to the termination point
    """
    assert abs(x) == term and abs(y) == term, '''Absolute value of both coords
    must equal the terminating point'''

    if x >= 0:
        if y > 0:
            # move left
            return (x - 1, y, term)
        else:
            # we are at the bottom right corner, so start a new loop
            return (x + 1, y, term + 1)
    else:
        if y > 0:
            # move down
            return (x, y - 1, term)
        else:
            # move right
            return (x + 1, y, term)


def turn_corner2(x, y, term):
    """
    iterative version!
    return coordinates based off of relationship of both x & y to each
    other and to the termination point
    """
    assert abs(x) == term and abs(y) == term, '''Absolute value of both coords
    must equal the terminating point'''

    if x >= 0:
        if y > 0:
            # move left
            return (x - 1, y, term)
        else:
            # we are at the bottom right corner, so start a new loop
            return (x + 1, y, term + 1)
    else:
        if y > 0:
            # move down
            return (x, y - 1, term)
        else:
            # move right
            return (x + 1, y, term)


def take_step(base, idx, x, y, term):
    if base == idx:
        res = manhattan_distance(x, y)
        print('Result: ', res)
        return res

    # we aren't to the base case so increment the counter
    next_idx = idx + 1
    if abs(x) == term and abs(y) == term:
        # we are at a corner
        (ax, ay, aterm) = turn_corner(x, y, term)
        return take_step(base, next_idx, ax, ay, aterm)
    if x == term:
        # we are on the right side, so move up
        return take_step(base, next_idx, x, y + 1, term)

    elif x == -term:
        # we are on the left side, so move down
        return take_step(base, next_idx, x, y - 1, term)

    elif y == term:
        # we are on the top side, so step left
        return take_step(base, next_idx, x - 1, y, term)
    else:
        # we are on the bottom, step right
        return take_step(base, next_idx, x + 1, y, term)


def manhattan_distance(x, y, dest_x=0, dest_y=0):
    """
    return the manhattan distance (rectilinear distance) from
    points (x, y) to (dest_x, dest_y). Destination coords default to the origin
    """
    return abs(x - dest_x) + abs(y - dest_y)


def spiral(stop_val, start, x, y):
    i = start
    t = 0

    while i != stop_val:
        # make a loop around the spiral
        i += 1
        if at_corner(x, y, t):
            # turn the corner
            if x >= 0:
                if y > 0:
                    # move left
                    x -= 1
                else:
                    # we are at the bottom right corner, so start a new loop
                    x += 1
                    t += 1
            else:
                if y > 0:
                    # move down
                    y -= 1
                else:
                    # move right
                    x += 1
        elif x == t:
            y += 1
        elif x == -t:
            y -= 1
        elif y == t:
            x -= 1
        else:
            x += 1

    res = manhattan_distance(x, y)
    print('res: {0} x: {1}, y: {2}'.format(res, x, y))
    return res


def at_corner(x, y, term):
    return abs(x) == term and abs(y) == term


# Tests
class TestSpiralOut(unittest.TestCase):
    def test_square_one_to_itself(self):
        self.assertEqual(spiral(1, 1, 0, 0, 0),  0)

    def test_counts_from_point_around_a_corner(self):
        self.assertEqual(spiral(12, 1, 0, 0, 0),  3)
        self.assertEqual(spiral(23, 1, 0, 0, 0), 2)
        self.assertEqual(spiral(24, 1, 0, 0, 0), 3)
        self.assertEqual(spiral(26, 1, 0, 0, 0), 5)

    def test_counts_from_diagonal(self):
        self.assertEqual(spiral(13, 1, 0, 0, 0), 4)
        self.assertEqual(spiral(49, 1, 0, 0, 0), 6)

    def test_large_distance(self):
        self.assertEqual(spiral(1024, 1, 0, 0, 0), 31)
        self.assertEqual(spiral(368078, 1, 0, 0, 0), 371)


if __name__ == '__main__':
    unittest.main()
