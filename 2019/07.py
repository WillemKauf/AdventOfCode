from Intcode import IntCode, IntCodes
from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input7.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    perms = [perm for perm in itertools.permutations(range(0,5))]
    max_v = -1
    for perm in perms:
        input_val = 0
        for i in range(0, 5):
            ic = IntCode(deepcopy(input_lst))
            ic.set_input([perm[i], input_val])
            ic.parse_tape()
            input_val = ic.output[-1]
        max_v = max(max_v, ic.output[-1])
    return max_v

def part_2(input_lst):
    perms  = [perm for perm in itertools.permutations(range(5,10))]
    max_v  = -1
    for perm in perms:
        ic_lst       = [IntCode(deepcopy(input_lst)) for _ in range(0,5)]
        ics          = IntCodes(ic_lst)
        input_buffer = {n:[perm[n]] for n in range(0,5)}
        input_buffer[0].append(0)
        ics.set_input(input_buffer)
        outputs = ics.sync_run()
        max_v = max(max_v, outputs[-1][-1])
    return max_v


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
