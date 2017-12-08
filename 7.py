"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower
of programs that have gotten themselves into a bit of trouble. A recursive
algorithm has gotten out of hand, and now they're balanced precariously in a
large tower.

One program at the bottom supports the entire tower. It's holding a large
disc, and on the disc are balanced several more sub-towers. At the bottom of
these sub-towers, standing on the bottom disc, are other programs, each
holding their own disc, and so on. At the very tops of these
sub-sub-sub-...-towers, many programs stand simply keeping the disc below them
balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these
towers. You ask each program to yell out their name, their weight, and (if
they're holding a disc) the names of the programs immediately above them
balancing on that disc. You write this information down (your puzzle input).
Unfortunately, in their panic, they don't do this in an orderly fashion; by
the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers that looks
like this:

                gyxo
              /     
         ugml - ebii
       /      \     
      |         jptl
      |        
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |             
      |         ktlj
       \      /     
         fwft - cntj
              \     
                xhth

In this example, tknk is at the bottom of the tower (the bottom program), and
is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower
balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is
correct. What is the name of the bottom program?
"""
import unittest
from utils import split_strip as sstrip

# build dict of all program names P and their weights we will use to do lookup
# build a list of dict for all P with children


def deparen(s):
    """ remove parens from a string and cast as int """
    return int(s.replace('(', '').replace(')', ''))


def decomma(s):
    """ remove comma from a string and cast as int """
    return s.replace(',', '')


def lowest_tower(t):
    return 'b'


def node_weight(node):
    """ return the weight of a node and its child nodes (if any) """
    w = node.get('weight')
    if 'children' not in node:
        return w
    else:
        w += sum(node_weight(child) for child in node['children'])
        return w


def main():
    f = open('./input/7_mock.txt')
    P_TABLE = dict()
    C_SET = set()

    for line in f.readlines():
        split_line = list(sstrip(line))
        name = split_line[0]
        weight = deparen(split_line[1])
        P_TABLE.setdefault(name, weight)

        if len(split_line) > 2:
            # has children so add to TABLE and C_SET
            c = map(decomma, split_line[3:])
            node = (name,  weight, c)
            C_SET.add(node)


class TestDay7(unittest.TestCase):
    def test_returns_weight_of_self_and_children(self):
        x = {'name': 'x', 'weight': 1}
        y = {'name': 'y', 'weight': 0}
        z = {'name': 'z', 'weight': 2}
        a = {'name': 'a', 'weight': -4}
        c = {'name': 'c', 'weight': 7, 'children': [a]}
        k = {'name': 'k', 'weight': 6, 'children': [c]}
        j = {'name': 'j', 'weight': 4, 'children': [k, z, y, x]}
        self.assertEqual(node_weight(k), 9)
        self.assertEqual(node_weight(j), 16)

    def test_returns_weight_for_mulitple_levels(self):
        x = {'name': 'x', 'weight': 1}
        y = {'name': 'y', 'weight': 0}
        z = {'name': 'z', 'weight': 2}
        a = {'name': 'a', 'weight': -4}
        c = {'name': 'c', 'weight': 7, 'children': [a]}
        k = {'name': 'k', 'weight': 6, 'children': [c]}
        j = {'name': 'j', 'weight': 4, 'children': [k, z, y, x]}

        self.assertEqual(node_weight(j), 16)


if __name__ == '__main__':
    unittest.main()
