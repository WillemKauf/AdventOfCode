from Intcode import IntCode
import numpy as np

def read_input():
    input_lst = []
    with open("input/input13.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    intcode = IntCode(input_lst)
    grid    = {}
    while intcode.status != "Halted":
        output_lst = [output for output in intcode.parse_tape_with_output()]
        for i in range(0, len(output_lst), 3):
            x, y, tile_id = output_lst[i:i+3]
            grid[(x,y)]   = tile_id
    return len([i for i in grid.values() if i == 2])

def part_2(input_lst):
    input_lst[0] = 2
    intcode = IntCode(input_lst)
    paddle  = 0
    ball    = 0
    score   = 0
    while intcode.status != "Halted":
        if intcode.index == len(intcode.tape):
            intcode.index = 0
        x, y, s = intcode.parse_tape_with_n_output(3)
        if all([x == None, y == None, s == None]):
            return score
        if (x, y) == (-1, 0):
            score = s
        if s == 3:
            paddle = x
        elif s == 4:
            ball = x
        if paddle < ball:
            intcode.set_input([1])
        elif paddle > ball:
            intcode.set_input([-1])
        else:
            intcode.set_input([0])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
