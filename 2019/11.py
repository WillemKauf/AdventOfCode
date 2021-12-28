from Intcode import IntCode
from collections import defaultdict
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

def read_input():
    input_lst = []
    with open("input/input11.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    direc   = complex(0,1)
    pos     = complex(0,0)
    intcode = IntCode(input_lst)
    grid    = defaultdict(int, {pos:0})
    while intcode.status != "Halted":
        intcode.set_input([grid[pos]])
        color, ddir = [output for output in intcode.parse_tape_with_output()]
        grid[pos] = color
        direc *= (-1*(ddir == 1)+1*(ddir == 0))*complex(0,1)
        pos += direc
    return len(grid)

def part_2(input_lst):
    direc   = complex(0,1)
    pos     = complex(0,0)
    intcode = IntCode(input_lst)
    grid    = defaultdict(int, {pos:1})
    while intcode.status != "Halted":
        intcode.set_input([grid[pos]])
        color, ddir = [output for output in intcode.parse_tape_with_output()]
        grid[pos] = color
        direc *= (-1*(ddir == 1)+1*(ddir == 0))*complex(0,1)
        pos += direc
    arr = np.zeros((7,43),dtype=np.int8)
    for c, v in grid.items():
        i,j = int(c.real), int(c.imag)+5
        arr[j][i] = v
    arr = np.flip(arr, 0)
    for j in arr:
        print("".join(["⬛"*(int(i)==1)+"⬜"*(int(i)==0) for i in j]))


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
