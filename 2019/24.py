from collections import defaultdict
from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]

def part_1(grid):
    seen = []
    while True:
        if grid in seen:
            cnt = 1
            res = 0
            for j in range(0, len(grid)):
                for i in range(0, len(grid[j])):
                    if grid[j][i] == "#":
                        res += cnt
                    cnt *= 2
            return res
        seen.append(deepcopy(grid))
        new_grid = deepcopy(grid)
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                c = grid[j][i]
                neighbours = []
                for dd in ddir:
                    new_i, new_j = i+dd[0], j+dd[1]
                    if 0 <= new_j < len(grid) and 0 <= new_i < len(grid[j]):
                        neighbours.append(int(grid[new_j][new_i] == "#"))
                if c == "#":
                    if sum(neighbours) != 1:
                        new_grid[j][i] = "."
                else:
                    if sum(neighbours) in [1,2]:
                        new_grid[j][i] = "#"
        grid = new_grid

def vis(grid):
    max_depth = max(grid, key=lambda k: k[0])[0]
    mp   = {0:".", 1:"#"}
    for i in range(-max_depth, max_depth+1):
        lst = [["." for _ in range(0, 5)] for _ in range(0,5)]
        for k,v in grid.items():
            d,x,y = k
            if d == i:
                lst[y][x] = mp[v]
        print(i)
        for l in lst:
            print("".join(l))
        print()

def part_2(input_lst):
    n    = 5
    grid = {}
    mp   = {".":0, "#":1}
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            grid[(0,i,j)] = mp[input_lst[j][i]]
    grid[(0,2,2)] = 0
    depth = 0
    for _ in range(0, 200):
        depth += 1
        for jj in range(0, n):
            for ii in range(0, n):
                grid[(-depth,ii,jj)] = 0
                grid[(depth,ii,jj)]  = 0
        new_grid = deepcopy(grid)
        for pos, v in grid.items():
            d,i,j = pos
            neighbours = []
            for dd in ddir:
                new_i, new_j = i+dd[0], j+dd[1]
                if (d, new_i, new_j) in grid:
                    neighbours.append(grid[(d, new_i, new_j)])
            if i == 0: #Append neighbour from d-1, i=1,j=2
                rep = (d-1, 1, 2)
                if rep in grid:
                    neighbours.append(grid[rep])
            elif i == n-1: #Append neighbours from d-1, i=3,j=2
                rep = (d-1, 3, 2)
                if rep in grid:
                    neighbours.append(grid[rep])
            if j == 0: #Append neighbours from d-1, i=2,j=1
                rep = (d-1, 2, 1)
                if rep in grid:
                    neighbours.append(grid[rep])
            elif j == n-1: #Append neighbours from d-1, i=2,j=3
                rep = (d-1, 2, 3)
                if rep in grid:
                    neighbours.append(grid[rep])
            if (i,j) == (1,2): #Append neighbours from d+1, all values from left hand side.
                for k in range(0, n):
                    rep = (d+1, 0, k)
                    if rep in grid:
                        neighbours.append(grid[rep])
            elif (i,j) == (3,2): #Append neighbours from d+1, all values from right hand side.
                for k in range(0, n):
                    rep = (d+1, n-1, k)
                    if rep in grid:
                        neighbours.append(grid[rep])
            elif (i,j) == (2,1): #Append neighbours from d+1, all values from bottom side.
                for k in range(0, n):
                    rep = (d+1, k, 0)
                    if rep in grid:
                        neighbours.append(grid[rep])
            elif (i,j) == (2,3):#Append neighbours from d+1, all values from top side.
                for k in range(0, n):
                    rep = (d+1, k, n-1)
                    if rep in grid:
                        neighbours.append(grid[rep])
            if v == 1:
                if sum(neighbours) != 1:
                    new_grid[(d,i,j)] = 0
            else:
                if sum(neighbours) in [1,2]:
                    new_grid[(d,i,j)] = 1
            if (i,j) == (2,2):
                new_grid[(d,i,j)] = 0
        grid = new_grid
    return sum(grid.values())

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
