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


def main():
    f = open('./input/7.txt')
    P_TABLE = dict()
    C_SET = dict()

    def node_weight(node):
        """ return the weight of a node and its child nodes (if any) """
        if node not in C_SET:
            # has no children so return node weight from lookup table
            return P_TABLE.get(node)
        else:
            return sum(
                    (node_weight(x) for x in C_SET[node]['children'])
                    )

    for line in f.readlines():
        split_line = list(sstrip(line))
        name = split_line[0]
        weight = deparen(split_line[1])
        P_TABLE.setdefault(name, weight)

        if len(split_line) > 2:
            # has children so add to TABLE and C_SET
            c = map(decomma, split_line[3:])
            C_SET[name] = {'weight': weight, 'children': c}

    k = [
            {
                'name': key,
                'weight': sum([node_weight(c) for c in node['children']])
                }
            for key, node in C_SET.items()
            ]

    xx = max(k, key=lambda x: x['weight'])
    return xx


# main()


""" part 2: """


from collections import OrderedDict


def main2():
    f = open('./input/7_mock.txt')
    lines = f.readlines()
    f.close()
    P_TABLE = OrderedDict()
    C_SET = OrderedDict()

    def not_balanced(node):
        if node not in C_SET:
            # has no children so return node weight from lookup table
            return False
        else:
            C = {P_TABLE[x] for x in C_SET[node]['children']}
            L = len(C)
            if L > 1:
                w = [(c, P_TABLE[c]) for c in C]
                print(w)
                return True

            return False

    def node_weight(node):
        """ return the weight of a node and its child nodes (if any) """
        if node not in C_SET:
            # has no children so return node weight from lookup table
            return P_TABLE.get(node)
        elif not_balanced(node):
            print('PPP: ', node)
            return P_TABLE.get(node)
        else:
            # cc = {P_TABLE.get(c) for c in C_SET[node]['children']}
            return sum(
                    (node_weight(x) for x in C_SET[node]['children'])
                    )

    for line in lines:
        split_line = list(sstrip(line))
        name = split_line[0]
        weight = deparen(split_line[1])
        P_TABLE.setdefault(name, weight)

        if len(split_line) > 2:
            # has children so add to TABLE and C_SET
            c = map(decomma, split_line[3:])
            C_SET[name] = {'weight': weight, 'children': c}

    k = [
            {
                'name': key,
                'weight': ([node_weight(c) for c in node['children']])
                }
            for key, node in C_SET.items()
            ]

    xx = max(k, key=lambda x: x['weight'])
    print('K: ', xx)
    # return xx


main2()
