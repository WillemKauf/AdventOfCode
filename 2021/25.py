from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            curr_lst = [i for i in line.rstrip()]
            input_lst.append(curr_lst)
    return input_lst

def part_1(grid):
    it = 0
    while True:
        new_grid = deepcopy(grid)
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                if grid[j][i] == ">":
                    if grid[j][(i+1)%len(grid[j])] == ".":
                        new_grid[j][i] = "."
                        new_grid[j][(i+1)%len(grid[j])] = ">"
        to_update = []
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                if grid[j][i] == "v":
                    if new_grid[(j+1)%len(grid)][i] == ".":
                        to_update.append((i,j))
                        new_grid[(j+1)%len(grid)][i] = "v"

        for i,j in to_update:
            new_grid[j][i] = "."
        it += 1
        if new_grid == grid:
            return it
        grid = new_grid

def part_2(input_lst):
    pass

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
