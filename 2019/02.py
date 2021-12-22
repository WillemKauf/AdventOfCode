from Intcode import IntCode
from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    input_lst[1] = 12
    input_lst[2] = 2
    ic = IntCode(input_lst)
    ic.parse_tape()
    return ic.tape[0]

def part_2(input_lst):
    for i in range(0, 99+1):
        for j in range(0, 99+1):
            input_lst[1] = i
            input_lst[2] = j
            ic = IntCode(deepcopy(input_lst))
            ic.parse_tape()
            if ic.tape[0] == 19690720:
                return 100*i+j

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
