import numpy as np
import math

def read_input():
    input_lst = None
    with open("input/input16.txt") as input_file:
        for line in input_file:
            input_lst = np.array([int(i) for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    base_pattern = np.array([0, 1, 0, -1])
    curr_lst     = input_lst
    for _ in range(0, 100):
        new_lst = []
        for i in range(0, len(curr_lst)):
            ith_pattern = np.repeat(base_pattern, i+1)
            pattern     = np.tile(ith_pattern, math.ceil(len(curr_lst)/len(ith_pattern))+1)[1:len(curr_lst)+1]
            res         = pattern.dot(curr_lst)
            new_lst.append(abs(res) % 10)
        curr_lst = np.array(new_lst)
    return "".join([str(s) for s in curr_lst[:8]])

def part_2(input_lst):
    base_pattern = np.array([0, 1, 0, -1])
    offset       = int("".join([str(s) for s in input_lst[:7]]))
    curr_lst     = np.tile(input_lst, 10000)[offset:]
    for _ in range(0, 100):
        new_lst = []
        sm = sum(curr_lst)
        for i in range(0, len(curr_lst)):
            new_lst.append(abs(sm) % 10)
            sm -= curr_lst[i]
        curr_lst = np.array(new_lst)
    return "".join([str(s) for s in curr_lst[:8]])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
