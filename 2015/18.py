from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            input_lst.append([c for c in line])
    return input_lst

def part_1(input_lst):
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0]) + abs(prod[1]) in [1, 2]]
    num_steps = 100
    for _ in range(0, num_steps):
        new_lst = deepcopy(input_lst)
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                light         = input_lst[j][i]
                neighbours    = [input_lst[j+jj][i+ii] for jj,ii in ddir if 0 <= j+jj < len(input_lst) and 0 <= i+ii < len(input_lst[j])]
                sm_neighbours = sum([1 for neighbour in neighbours if neighbour == "#"])
                if light == "#":
                    if sm_neighbours not in [2,3]:
                        new_lst[j][i] = "."
                else:
                    if sm_neighbours == 3:
                        new_lst[j][i] = "#"
        input_lst = new_lst
    return sum([row.count("#") for row in input_lst])

def part_2(input_lst):
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0]) + abs(prod[1]) in [1, 2]]
    num_steps = 100
    ny, nx = len(input_lst), len(input_lst[0])
    input_lst[0][0]       = "#"
    input_lst[0][nx-1]    = "#"
    input_lst[ny-1][0]    = "#"
    input_lst[ny-1][nx-1] = "#"
    for _ in range(0, num_steps):
        new_lst = deepcopy(input_lst)
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                light         = input_lst[j][i]
                neighbours    = [input_lst[j+jj][i+ii] for jj,ii in ddir if 0 <= j+jj < len(input_lst) and 0 <= i+ii < len(input_lst[j])]
                sm_neighbours = sum([1 for neighbour in neighbours if neighbour == "#"])
                if light == "#":
                    if sm_neighbours not in [2,3]:
                        new_lst[j][i] = "."
                else:
                    if sm_neighbours == 3:
                        new_lst[j][i] = "#"

        input_lst = new_lst
        input_lst[0][0]       = "#"
        input_lst[0][nx-1]    = "#"
        input_lst[ny-1][0]    = "#"
        input_lst[ny-1][nx-1] = "#"
    return sum([row.count("#") for row in input_lst])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
