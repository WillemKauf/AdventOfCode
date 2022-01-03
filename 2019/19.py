from Intcode import IntCode
from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input19.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    res = 0
    for j in range(0, 50):
        for i in range(0, 50):
            intcode = IntCode(deepcopy(input_lst))
            intcode.set_input([i,j])
            output = intcode.parse_tape_with_n_output(1)[0]
            if output != None:
                res += output
    return res

def part_2(input_lst):
    def check_grid(i,j):
        intcode = IntCode(deepcopy(input_lst))
        intcode.set_input([i,j])
        output = intcode.parse_tape_with_n_output(1)[0]
        return output

    grid       = {}
    bound      = int(1e6)
    sqr_coords = lambda p: [(p[0],p[1]-99),(p[0]+99,p[1]),(p[0]+99,p[1]-99)]
    i          = 0
    for j in range(100, bound):
        while check_grid(i,j) != 1:
            i += 1
        coords = sqr_coords((i,j))
        if all([check_grid(c[0], c[1]) for c in coords]):
            return 10000*coords[0][0]+coords[0][1]
    return None


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
