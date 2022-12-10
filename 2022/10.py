from collections import deque
def read_input():
    input_arr = []
    with open("input/input10.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            line = line.split(" ")
            if len(line) == 1:
                input_arr.append([line[0], None])
            else:
                input_arr.append(line)
    return input_arr

class CMD():
    def __init__(self, val, timer):
        self.val   = val
        self.timer = timer

def part1(input_arr):
    x = 1
    c = 0
    res = 0
    s = [20, 60, 100, 140, 180, 220]
    cmds = deque([])
    for a, b in input_arr:
        if b != None:
            b = int(b)
        if a == "addx":
            cmds.append(CMD(b,2))
        elif a == "noop":
            cmds.append(CMD(0,1))
        c += 1
        if c in s:
            res += c*x
        if len(cmds):
            cmd = cmds[0]
            cmd.timer -= 1
            if cmd.timer == 0:
                x += cmd.val
                cmds.popleft()
    while len(cmds):
        c += 1
        cmd = cmds[0]
        cmd.timer -= 1
        if c in s:
            res += c*x
        if cmd.timer == 0:
            x += cmd.val
            cmds.popleft()
    for i in range(c, 221):
        if i in s:
            res += i*x
    return res

def part2(input_arr):
    w = 40
    h = 6
    grid = [["." for _ in range(0, w)] for _ in range(0, h)]
    s = [40, 80, 120, 160, 200, 240]
    x = 1
    c = 0
    j = 0
    cmds = deque([])
    for a, b in input_arr:
        if b != None:
            b = int(b)
        if a == "addx":
            cmds.append(CMD(b,2))
        elif a == "noop":
            cmds.append(CMD(0,1))
        if c%40 in [x-1, x, x+1]:
            grid[j][c%40] = "#"
        c += 1
        if c in s:
            j += 1
        if len(cmds):
            cmd = cmds[0]
            cmd.timer -= 1
            if cmd.timer == 0:
                x += cmd.val
                cmds.popleft()
    while len(cmds):
        cmd = cmds[0]
        cmd.timer -= 1
        if c in s:
            j += 1
        if c%40 in [x-1, x, x+1]:
            grid[j][c%40] = "#"
        c += 1
        if cmd.timer == 0:
            x += cmd.val
            cmds.popleft()
    for i in range(c, 221):
        if i in s:
            j += 1
        if i in [x-1, x, x+1]:
            grid[j][i] = "#"
    for l in grid:
        print("".join(l))

def main():
    input_arr = read_input()
    print(part1(input_arr))
    part2(input_arr)

if __name__ == "__main__":
    main()
