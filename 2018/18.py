from collections import defaultdict
from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(grid):
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) in [1,2]]

    for _ in range(0, 10):
        new_grid = deepcopy(grid)
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                neighbours = []
                for dd in ddir:
                    ii = i + dd[0]
                    jj = j + dd[1]
                    if 0 <= ii < len(grid[j]) and 0 <= jj < len(grid):
                        neighbours.append(grid[jj][ii])
                if grid[j][i] == "." and neighbours.count("|") >= 3:
                    new_grid[j][i] = "|"
                elif grid[j][i] == "|" and neighbours.count("#") >= 3:
                    new_grid[j][i] = "#"
                elif grid[j][i] == "#":
                    if neighbours.count("#") >= 1 and neighbours.count("|") >= 1:
                        new_grid[j][i] = "#"
                    else:
                        new_grid[j][i] = "."
        grid = new_grid
    n_acres = 0
    n_yards = 0
    for l in grid:
        n_acres += l.count("|")
        n_yards += l.count("#")
    return n_yards*n_acres

def part_2(grid):
    ddir    = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) in [1,2]]
    v_dct   = defaultdict(list)
    history = []
    n       = 3
    n_iters = 1000000000
    for it in range(0, n_iters):
        new_grid = deepcopy(grid)
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                neighbours = []
                for dd in ddir:
                    ii = i + dd[0]
                    jj = j + dd[1]
                    if 0 <= ii < len(grid[j]) and 0 <= jj < len(grid):
                        neighbours.append(grid[jj][ii])
                if grid[j][i] == "." and neighbours.count("|") >= 3:
                    new_grid[j][i] = "|"
                elif grid[j][i] == "|" and neighbours.count("#") >= 3:
                    new_grid[j][i] = "#"
                elif grid[j][i] == "#":
                    if neighbours.count("#") >= 1 and neighbours.count("|") >= 1:
                        new_grid[j][i] = "#"
                    else:
                        new_grid[j][i] = "."
        grid = new_grid
        n_acres = 0
        n_yards = 0
        for l in grid:
            n_acres += l.count("|")
            n_yards += l.count("#")
        res = n_yards*n_acres
        v_dct[res].append(it)
        history.append(res)
        if len(v_dct[res]) > 3:
            start_res = res
            break
    start_it = v_dct[start_res][-2]
    end_it   = v_dct[start_res][-1]
    d_it     = end_it - start_it
    return history[start_it+(n_iters-len(history))%d_it]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
