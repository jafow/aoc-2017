"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series of
unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions
look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1
    (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the registers
are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in
your puzzle input?
"""


def gt(a, b): return a > b


def lt(a, b): return a < b


def eq(a, b): return a == b


def neq(a, b): return a != b


def gte(a, b): return a >= b


def lte(a, b): return a <= b


def inc(a, b): return a + b


def dec(a, b): return a - b


# table of comparison operators & methods to perform those comparisons
oper_table = {
        '>': gt,
        '<': lt,
        '==': eq,
        '!=': neq,
        '>=': gte,
        '<=': lte,
        'inc': inc,
        'dec': dec
        }


def parse_cond(pieces, regs):

    """ parse a condition from pieces; return result of applying the condition
    to pieces """

    reg, op, val = pieces
    if reg not in regs:
        regs[reg] = 0

    return oper_table[op](regs[reg], int(val))


def modify(regs, targ, op, A):

    """ modify a target targ in regs by amount A using operator op """

    if targ not in regs:
        regs[targ] = 0

    action = oper_table[op]
    regs[targ] = action(regs[targ], A)
    return regs[targ]


def main(lines):
    regs = {}
    highest = -10000

    for line in lines:
        targ_reg, op, val, *cond = line.split(' ')

        if targ_reg not in regs:
            regs[targ_reg] = 0

        if parse_cond(cond[1:], regs):
            highest = max(highest, modify(regs, targ_reg, op, int(val)))

    m = max(regs.values())
    print(highest)
    return m


main(open('./input/8.txt'))
