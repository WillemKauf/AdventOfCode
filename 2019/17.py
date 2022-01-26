from Intcode import IntCode
from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input17.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    intcode = IntCode(input_lst)
    grid    = []
    while intcode.status != "Halted":
        output = intcode.parse_tape()
    curr_lst = []
    for c in output:
        if c == 10:
            if len(curr_lst):
                grid.append(curr_lst)
            curr_lst = []
        else:
            curr_lst.append(chr(c))
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    res = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            neighbours = []
            if grid[j][i] == "^":
                start_pos = (i,j)
            if grid[j][i] != "#":
                continue
            for dd in ddir:
                ii, jj = i+dd[0], j+dd[1]
                if 0 <= ii < len(grid[j]) and 0 <= jj < len(grid):
                    neighbours.append(grid[jj][ii])
            if all([s == "#" for s in neighbours]):
                res += i*j
    return res, grid, start_pos

def part_2(input_lst, grid, start_pos):
    ddir         = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    history      = ""
    pos          = start_pos
    direc        = "U"
    mp           = {"D":(0,1),"U":(0,-1),"L":(-1,0),"R":(1,0)}
    rot_mp       = {"UL":"L", "UR":"R",
                    "RU":"L", "RD":"R",
                    "DR":"L", "DL":"R",
                    "LD":"L", "LU":"R"}
    curr_counter  = 0
    num_scaffolds = sum([sum([i != "." for i in j]) for j in grid])
    seen = set()
    while True:
        dd             = mp[direc]
        test_pos       = pos[0] + dd[0], pos[1] + dd[1]
        test_x, test_y = test_pos
        must_turn      = False
        if 0 <= test_x < len(grid[0]) and 0 <= test_y < len(grid):
            if grid[test_y][test_x] == ".":
                must_turn = True
        else:
            must_turn = True
        if must_turn:
            if direc in ["U", "D"]:
                for new_direc, new_dd in [(k,v) for k,v in mp.items() if k not in ["U", "D"]]:
                    new_pos = pos[0] + new_dd[0], pos[1] + new_dd[1]
                    new_x, new_y = new_pos
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        if grid[new_y][new_x] != ".":
                            break
            elif direc in ["L", "R"]:
                for new_direc, new_dd in [(k,v) for k,v in mp.items() if k not in ["L", "R"]]:
                    new_pos = pos[0] + new_dd[0], pos[1] + new_dd[1]
                    new_x, new_y = new_pos
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        if grid[new_y][new_x] != ".":
                            break
        else:
            curr_counter += 1
            new_direc = direc
            new_pos   = test_pos
        if direc != new_direc:
            rot = rot_mp[direc+new_direc]
            if curr_counter == 0:
                add_str = rot + ","
            else:
                add_str = str(curr_counter+1) + "," + rot + ","
                curr_counter = 0
            history += add_str
        seen.add(pos)
        if len(seen) == num_scaffolds:
            break
        pos   = new_pos
        direc = new_direc

    history = history[:-3]
    """
    Need to reduce history by hand.
    R6,L12,R6,R6,L12,R6,L12,R6,L8,L12,R12,L10,L10,L12,R6,L8,L12,R12,L10,L10,L12,R6,L8,L12,R12,L10,L10,L12,R6,L8,L12,R6,L12,R6
    A = R6,L12,R6
    B = L12,R6,L8,L12
    C = R12,L10,L10
    Routine: A,A,B,C,B,C,B,C,B,A
    """

    A    = "R,6,L,12,R,6"
    B    = "L,12,R,6,L,8,L,12"
    C    = "R,12,L,10,L,10"
    R    = "A,A,B,C,B,C,B,C,B,A"
    A_in = [ord(c) for c in A]+[10]
    B_in = [ord(c) for c in B]+[10]
    C_in = [ord(c) for c in C]+[10]
    R_in = [ord(c) for c in R]+[10]

    input_lst[0] = 2
    intcode      = IntCode(input_lst)
    intcode.set_input(R_in + A_in + B_in + C_in + [str(ord("n")), 10])
    intcode.parse_tape()
    return intcode.output[-1]

def main():
    p1, grid, start_pos = part_1(read_input())
    print(p1)
    print(part_2(read_input(), grid, start_pos))

if __name__ == "__main__":
    main()
