from collections import deque

def read_input():
    input_str = []
    with open("input/input20.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    input_str = input_str[1:-1]
    ddir      = {"N":(0,1), "S":(0,-1), "W":(-1,0), "E":(1,0)}
    grid      = {}
    queue     = deque([])
    max_steps = -1
    num_steps = 0
    pos       = (0,0)
    for c in input_str:
        if c == "(":
            queue.appendleft((pos, num_steps))
        elif c == ")":
            pos, num_steps = queue.popleft()
        elif c == "|":
            pos, num_steps = queue[0]
        else:
            num_steps += 1
            dd  = ddir[c]
            pos = pos[0] + dd[0], pos[1] + dd[1]
            if pos in grid:
                grid[pos] = min(grid[pos], num_steps)
            else:
                grid[pos] = num_steps
    return max(grid.values()), len([v for v in grid.values() if v >= 1000])

def main():
    p1, p2 = part_1(read_input())
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
