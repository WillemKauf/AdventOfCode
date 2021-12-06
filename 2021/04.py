def read_input():
    grid_lst = []
    num_lst = []
    with open("input/input4.txt") as input_file:
        num_lst = input_file.readline().rstrip().split(",")
        curr_lst = []
        line = input_file.readline()
        for line in input_file:
            line = line.rstrip()
            if line == "":
                grid_lst.append(curr_lst)
                curr_lst = []
                continue
            curr_lst.append(line.split())
        if len(curr_lst):
            grid_lst.append(curr_lst)
    return num_lst, grid_lst

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
                    for jj in range(0, len(grid)):
                        for ii in range(0, len(grid[jj])):
                            if grid[jj][ii] != "X":
                                res += int(grid[jj][ii])
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
                        for jj in range(0, len(last_grid)):
                            for ii in range(0, len(last_grid[jj])):
                                if last_grid[jj][ii] != "X":
                                    res += int(last_grid[jj][ii])
                        return res*int(num)
                col = []
                for i in range(0, len(grid)):
                    col.append(grid[i][j])
                if all([i == "X" for i in col]):
                    won_lst.add(k)
                    if len(won_lst) == len(grid_lst):
                        last_grid = grid
                        res = 0
                        for jj in range(0, len(last_grid)):
                            for ii in range(0, len(last_grid[jj])):
                                if last_grid[jj][ii] != "X":
                                    res += int(last_grid[jj][ii])
                        return res*int(num)

def main():
    input_lsts = read_input()
    print(part_1(*input_lsts))
    print(part_2(*input_lsts))

if __name__ == "__main__":
    main()

