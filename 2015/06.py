def read_input():
    input_arr = []
    with open("input/input6.txt") as input_file:
        for line in input_file.readlines():
            line = line.rstrip().split()
            action = ""
            indices_A = []
            indices_B = []
            index_A = 0
            index_B = 0
            if line[0] == "toggle":
                action = line[0]
                index_A = 1
                index_B = 3
            if line[1] in ["on","off"]:
                action = line[1]
                index_A = 2
                index_B = 4
            index_A = [int(i) for i in line[index_A].split(",")]
            index_B = [int(i) for i in line[index_B].split(",")]
            input_arr.append([action, index_A, index_B])
    return input_arr

def part_1(input_arr):
    grid = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
    for (cmd, indices_A, indices_B) in input_arr:
        def func(val, cmd=cmd):
            if cmd == "toggle":
                return int(not(val))
            elif cmd == "on":
                return 1
            else:
                return 0
        for j in range(indices_A[1], indices_B[1]+1):
            for i in range(indices_A[0], indices_B[0]+1):
                grid[j][i] = func(grid[j][i])
    return sum([sum([i for i in j]) for j in grid])

def part_2(input_arr):
    grid = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
    for (cmd, indices_A, indices_B) in input_arr:
        def func(val, cmd=cmd):
            if cmd == "toggle":
                return val+2
            elif cmd == "on":
                return val+1
            else:
                return max(0, val-1)
        for j in range(indices_A[1], indices_B[1]+1):
            for i in range(indices_A[0], indices_B[0]+1):
                grid[j][i] = func(grid[j][i])
    return sum([sum([i for i in j]) for j in grid])

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
