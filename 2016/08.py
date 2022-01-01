import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

def read_input():
    input_lst = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_lst.append([i for i in line])
    return input_lst

def visualize(dct):
    arr = np.zeros((6,50))
    for (i,j),v in dct.items():
        arr[j][i] = v
    for j in arr:
        print("".join(["⬛"*(int(i)==1)+"⬜"*(int(i)==0) for i in j]))

def part_1(input_lst):
    width  = 50
    height = 6
    grid = {}
    for cmd in input_lst:
        new_grid = {}
        if cmd[0] == "rect":
            new_grid = grid
            max_i, max_j = [int(i) for i in cmd[1].split("x")]
            for j in range(0, max_j):
                for i in range(0, max_i):
                    new_grid[(i, j)] = 1
        elif cmd[0] == "rotate":
            rc = int(cmd[2].split("=")[-1])
            dd = int(cmd[-1])
            if cmd[1] == "row":
                for (i,j), v in grid.items():
                    if j == rc:
                        new_grid[(i+dd)%width,j] = v
                    else:
                        new_grid[i,j] = v
            elif cmd[1] == "column":
                for (i,j), v in grid.items():
                    if i == rc:
                        new_grid[i,(j+dd)%height] = v
                    else:
                        new_grid[i,j] = v
        grid = new_grid
    visualize(grid)
    return sum(grid.values())

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
