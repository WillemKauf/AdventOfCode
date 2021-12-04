def read_input():
    grid_lst = []
    num_lst = []
    with open("input/input4.txt") as input_file:
        num_lst = input_file.readline().rstrip().split(",")
        curr_lst = []
        for line in input_file:
            line = line.rstrip()
            if line == "":
                grid_lst.append(curr_lst)
                curr_lst = []
                continue
            curr_lst.append(line.split())
        if len(curr_lst):
            grid_lst.append(curr_lst)
    return num_lst, grid_lst[1:]

def part_1(num_lst, grid_lst):
    for num in num_lst:
        for k in range(0, len(grid_lst)):
            for j in range(0, len(grid_lst[k])):
                for i in range(0, len(grid_lst[k][j])):
                    if grid_lst[k][j][i] == num:
                        grid_lst[k][j][i] = "X"
        for k, grid in enumerate(grid_lst):
            for j in range(0, len(grid)):
                row = grid[j]
                if all([q == "X" for q in row]):
                    res = 0
                    for j in range(0, len(grid)):
                        for i in range(0, len(grid[j])):
                            if grid[j][i] != "X":
                                res += int(grid[j][i])
                    return res*int(num)
                col = []
                for i in range(0, len(grid)):
                    col.append(grid[i][j])
                if all([i == "X" for i in col]):
                    res = 0
                    for j in range(0, len(grid)):
                        for i in range(0, len(grid[j])):
                            if grid[j][i] != "X":
                                res += int(grid[j][i])
                    return res*int(num)

def part_2(num_lst, grid_lst):
    won_lst = set()
    for index, num in enumerate(num_lst):
        for k in range(0, len(grid_lst)):
            for j in range(0, len(grid_lst[k])):
                for i in range(0, len(grid_lst[k][j])):
                    if grid_lst[k][j][i] == num:
                        grid_lst[k][j][i] = "X"
        for k, grid in enumerate(grid_lst):
            for j in range(0, len(grid)):
                row = grid[j]
                if all([q == "X" for q in row]):
                    won_lst.add(k)
                    if len(won_lst) == len(grid_lst):
                        last_grid = grid
                        res = 0
                        for j in range(0, len(last_grid)):
                            for i in range(0, len(last_grid[j])):
                                if last_grid[j][i] != "X":
                                    res += int(last_grid[j][i])
                        return res*int(num)
                col = []
                for i in range(0, len(grid)):
                    col.append(grid[i][j])
                if all([i == "X" for i in col]):
                    won_lst.add(k)
                    if len(won_lst) == len(grid_lst):
                        last_grid = grid
                        res = 0
                        for j in range(0, len(last_grid)):
                            for i in range(0, len(last_grid[j])):
                                if last_grid[j][i] != "X":
                                    res += int(last_grid[j][i])
                        return res*int(num)

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()

