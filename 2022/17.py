from collections import deque

def read_input():
    input_arr = []
    with open("input/input17.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            for c in line:
                input_arr.append(c)
    return input_arr

class Rock():
    def __init__(self, ID, shape, width, height):
        self.ID     = ID
        self.shape  = shape
        self.width  = width
        self.height = height

ROCKS = [Rock(0, [["#", "#", "#", "#"]], 4, 1),

         Rock(1, [[None, "#", None],
                  ["#",  "#", "#"],
                  [None, "#", None]], 3, 3),

         Rock(2, [[None, None, "#"],
                  [None, None, "#"],
                  ["#",  "#",  "#"]], 3, 3),

         Rock(3, [["#"],
                  ["#"],
                  ["#"],
                  ["#"]], 1, 4),

         Rock(4, [["#", "#"],
                  ["#", "#"]], 2, 2)]

WIDTH = 7

def vis(graph):
    min_x = min([p[0] for p in graph.keys()])
    max_x = max([p[0] for p in graph.keys()])
    min_y = min([p[1] for p in graph.keys()])
    max_y = max([p[1] for p in graph.keys()])
    dx    = max_x - min_x
    dy    = max_y - min_y
    grid = [["." for _ in range(0, dx+1)] for _ in range(0, dy+1)]
    for p, v in graph.items():
        grid[max_y-p[1]][p[0]-min_x] = v
    for line in grid:
        line = ["⬛" if c == "#" else "⬜" for c in line ]
        print("".join(line))

def get_new_x_pos(rock, grid, curr_pos, shift):
    curr_x, curr_y = curr_pos
    new_x = curr_x+shift
    if new_x + rock.width > WIDTH:
        return curr_x
    if new_x < 0:
        return curr_x
    for j, r in enumerate(rock.shape):
        for i, c in enumerate(r):
            if c == None:
                continue
            test_pos = (new_x+i, curr_y-j)
            if test_pos in grid:
                return curr_x
    return new_x

def get_new_y_pos(rock, grid, curr_pos):
    curr_x, curr_y = curr_pos
    new_y = curr_y - 1
    for j, r in enumerate(rock.shape):
        for i, c in enumerate(r):
            if c == None:
                continue
            test_pos = (curr_x+i, new_y-j)
            if test_pos in grid:
                return curr_y
    return new_y

def part1(input_arr, N_ITER):
    dx         = 2
    dy         = 3
    jt         = 0
    n_jt       = len(input_arr)
    n_rock     = len(ROCKS)
    grid       = {(i,0):"#" for i in range(0, WIDTH)}
    jt_mp      = {"<":-1, ">":1}
    max_height = 0
    for it in range(0, N_ITER):
        rock    = ROCKS[it%n_rock]
        start_x = dx
        start_y = dy+rock.height+max_height
        queue   = deque([(start_x, start_y)])
        while len(queue):
            curr_pos = queue.popleft()
            jt_char  = input_arr[jt%n_jt]
            new_x    = get_new_x_pos(rock, grid, curr_pos, jt_mp[jt_char])
            new_y    = get_new_y_pos(rock, grid, (new_x, curr_pos[1]))
            jt += 1
            if curr_pos[1] == new_y: #Couldn't move down
                for j, r in enumerate(rock.shape):
                    for i, c in enumerate(r):
                        if c == None:
                            continue
                        pos = (new_x+i, new_y-j)
                        grid[pos] = c
                max_height = max(max_height, new_y)
                break
            else:
                queue.append((new_x, new_y))
    return max_height

def encode_state(rock, grid, curr_pos, shift):
    dy = 50 #Arbitrary?
    offset = rock.height+3
    part_of_grid = []
    for j in range(offset, dy+offset):
        curr_row = []
        for i in range(0, WIDTH):
            pos = (i, curr_pos[1]-j)
            if pos in grid:
                curr_row.append(grid[pos])
            else:
                curr_row.append('.')
        part_of_grid.append(tuple(curr_row))
    return (rock.ID, tuple(part_of_grid), shift)

def part2(input_arr, N_ITER):
    dx         = 2
    dy         = 3
    jt         = 0
    n_jt       = len(input_arr)
    n_rock     = len(ROCKS)
    grid       = {(i,0):"#" for i in range(0, WIDTH)}
    jt_mp      = {"<":-1, ">":1}
    max_height = 0
    seen       = {}
    dys        = {}
    for it in range(0, N_ITER):
        rock    = ROCKS[it%n_rock]
        start_x = dx
        start_y = dy+rock.height+max_height
        queue   = deque([(start_x, start_y)])
        state   = encode_state(rock, grid, (start_x, start_y), jt_mp[input_arr[jt%n_jt]])
        if state in seen:
            cycle_begin     = seen[state][0]
            cycle_length    = it - seen[state][0]
            cycle_height    = max_height - seen[state][1]
            num_full_cycles = (N_ITER-cycle_begin)//cycle_length
            num_rem_cycles  = (N_ITER-cycle_begin)%cycle_length
            res = seen[state][1] + cycle_height*num_full_cycles
            for i in range(0, num_rem_cycles):
                res += dys[i+cycle_begin]
            return res
        seen[state] = (it, max_height)
        while len(queue):
            curr_pos = queue.popleft()
            jt_char  = input_arr[jt%n_jt]
            new_x    = get_new_x_pos(rock, grid, curr_pos, jt_mp[jt_char])
            new_y    = get_new_y_pos(rock, grid, (new_x, curr_pos[1]))
            jt += 1
            if curr_pos[1] == new_y: #Couldn't move down
                for j, r in enumerate(rock.shape):
                    for i, c in enumerate(r):
                        if c == None:
                            continue
                        pos = (new_x+i, new_y-j)
                        grid[pos] = c
                curr_dy = new_y-max_height
                dys[it] = max(0, curr_dy)
                max_height = max(max_height, new_y)
                break
            else:
                queue.append((new_x, new_y))

def main():
    input_arr = read_input()
    print(part1(input_arr[:], 2022))
    print(part2(input_arr[:], 1000000000000))

if __name__ == "__main__":
    main()
