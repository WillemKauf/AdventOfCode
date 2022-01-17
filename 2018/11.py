def read_input():
    input_num = []
    with open("input/input11.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num


def create_grids(num, n):
    grid = [[0 for i in range(0, n)] for j in range(0, n)]
    for j in range(0, n):
        for i in range(0, n):
            r_ID       = i+10
            pwr_level  = ((((r_ID*j + num)*r_ID)%1000)//100)-5
            grid[j][i] = pwr_level
    sum_grid = [[0 for i in range(0, n)] for j in range(0, n)]

    for j in range(0, n):
        for i in range(0, n):
            sum_grid[j][i] = grid[j][i]
            if j > 0:
                sum_grid[j][i] += sum_grid[j-1][i]
            if i > 0:
                sum_grid[j][i] += sum_grid[j][i-1]
            if i > 0 and j > 0:
                sum_grid[j][i] -= sum_grid[j-1][i-1]
    return grid, sum_grid

def part_1(input_num):
    n              = 300
    grid, sum_grid = create_grids(input_num, n)
    n_s            = 3
    max_res        = -1
    max_pos        = None
    for j in range(0, n-n_s):
        for i in range(0, n-n_s):
            A   = sum_grid[j][i]
            B   = sum_grid[j][i+n_s]
            C   = sum_grid[j+n_s][i]
            D   = sum_grid[j+n_s][i+n_s]
            res = D+A-B-C
            if res > max_res:
                max_res = res
                max_pos = (i+1,j+1)

    return f"{max_pos[0]},{max_pos[1]}"

def part_2(input_num):
    max_res = -1
    max_str = None
    n       = 300
    for n_s in range(1, n):
        grid, sum_grid = create_grids(input_num, n)
        for j in range(0, n-n_s):
            for i in range(0, n-n_s):
                A   = sum_grid[j][i]
                B   = sum_grid[j][i+n_s]
                C   = sum_grid[j+n_s][i]
                D   = sum_grid[j+n_s][i+n_s]
                res = D+A-B-C
                if res > max_res:
                    max_res = res
                    max_str = (i+1,j+1,n_s)

    return f"{max_str[0]},{max_str[1]},{max_str[2]}"

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
