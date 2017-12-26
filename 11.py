"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a
program comes up to you, clearly in distress. "It's my child process," she
says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need
to determine the fewest number of steps required to reach him. (A "step" means
to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""

coords = dict(
            n=(0, -1), ne=(1, 0),
            se=(1, 1), s=(0, 1),
            sw=(-1, 0), nw=(-1, -1)
        )


def sum_tup(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def abs_sum_tup(t):
    x, y = t
    return abs(x) + abs(y)


def hex_path(line):
    """ string of directions => coordinates for destination """
    path = line.split(',')
    v = (0, 0)
    m = 0
    for p in path:
        v = sum_tup(coords[p], v)
        m = max(m, axial_to_cube(v))

    return m


def cube_distance(coord):
    """ https://www.redblobgames.com/grids/hexagons/#distances-cube """
    x, y, z = coord
    return (abs(x) + abs(y) + abs(z)) / 2


def axial_to_cube(coord):
    """ https://www.redblobgames.com/grids/hexagons/#conversions """
    x = coord[0]
    z = coord[1] - (x - (x & 1)) / 2
    y = -x - z
    return cube_distance(tuple((x, y, z)))


f = open('./input/11.txt').readline().strip()
pt1 = axial_to_cube(hex_path(f))
pt2 = hex_path(f)
print(pt2)
