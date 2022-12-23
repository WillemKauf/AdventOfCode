from collections import defaultdict
def read_input():
    input_arr = []
    input_instructs = []
    read_input_str = False
    with open("input/input22.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.strip('\n')
            if line == "":
                read_input_str = True
                continue
            if read_input_str:
                input_str = line
                curr_c = ""
                for i in range(0, len(input_str)):
                    c = input_str[i]
                    if c.isnumeric():
                        curr_c += c
                    else:
                        if len(curr_c):
                            input_instructs.append(int(curr_c))
                        input_instructs.append(c)
                        curr_c = ""
                input_instructs.append(int(curr_c))
            else:
                input_arr.append([c for c in line])

    return input_arr, input_instructs

def create_start_pos_and_grid_and_corner_mp_part1(input_arr):
    grid = {}
    start_pos = None
    corners = []
    for j, r in enumerate(input_arr):
        for i, c in enumerate(r):
            if c != " ":
                if start_pos == None:
                    start_pos = complex(i,j)
                grid[complex(i,j)] = c
                if c == "#":
                    continue
                left  = True if i == 0 else input_arr[j][i-1] == " "
                right = True if i == len(r)-1 else input_arr[j][i+1] == " "
                up    = True if j == 0 else input_arr[j-1][i] == " "
                down  = True if j == len(input_arr)-1 else input_arr[j+1][i] == " "
                if left or right or up or down:
                    corners.append(([i,j], left, right, up, down))
    corner_mp = {}
    for corner in corners:
        pos, left, right, up, down = corner
        c_pos = complex(pos[0], pos[1])
        if left:
            next_pos = max([p[0][0] for p in corners if p[0][1] == pos[1]])
            if grid[complex(next_pos, pos[1])] != "#":
                corner_mp[(c_pos, complex(-1,0))] = (complex(next_pos, pos[1]), complex(-1,0))
        if right:
            next_pos = min([p[0][0] for p in corners if p[0][1] == pos[1]])
            if grid[complex(next_pos, pos[1])] != "#":
                corner_mp[(c_pos, complex(1,0))] = (complex(next_pos, pos[1]), complex(1,0))
        if up:
            next_pos = max([p[0][1] for p in corners if p[0][0] == pos[0]])
            if grid[complex(pos[0], next_pos)] != "#":
                corner_mp[(c_pos, complex(0,-1))] = (complex(pos[0], next_pos), complex(0,-1))
        if down:
            next_pos = min([p[0][1] for p in corners if p[0][0] == pos[0]])
            if grid[complex(pos[0], next_pos)] != "#":
                corner_mp[(c_pos, complex(0,1))] = (complex(pos[0], next_pos), complex(0,1))
    return start_pos, grid, corner_mp

def vis(graph, curr_pos):
    print("-------------")
    min_x = min([int(p.real) for p in graph.keys()])
    max_x = max([int(p.real) for p in graph.keys()])
    min_y = min([int(p.imag) for p in graph.keys()])
    max_y = max([int(p.imag) for p in graph.keys()])
    dx    = max_x - min_x
    dy    = max_y - min_y
    grid = [["." for _ in range(0, dx+1)] for _ in range(0, dy+1)]
    for p, v in graph.items():
        p = (int(p.real), int(p.imag))
        grid[p[1]-min_y][p[0]-min_x] = v
    grid[int(curr_pos.imag)-min_y][int(curr_pos.real)-min_x] = "X"
    for line in grid:
        line = [c for c in line]
        print("".join(line))

def path_find(start_pos, grid, corner_mp, input_instructs):
    curr_dir = complex(1,0)
    curr_pos = start_pos
    direc_mp     = {"R":complex(0,-1), "L":complex(0,1)}
    direc_val_mp = {complex(1,0):0, complex(0,-1):1, complex(-1,0):2, complex(0,1):3}
    for instruct in input_instructs:
        if isinstance(instruct, int):
            begin_pos = curr_pos
            for _ in range(0, instruct):
                curr_pos += curr_dir
                if curr_pos in grid:
                    if grid[curr_pos] == "#":
                        curr_pos -= curr_dir
                        break
                else:
                    curr_pos -= curr_dir
                    if (curr_pos, curr_dir) not in corner_mp:
                        break
                    curr_pos, curr_dir = corner_mp[(curr_pos, curr_dir)]
        else:
            if curr_dir == complex(0,-1):
                curr_dir = complex(0,1)
            elif curr_dir == complex(0,1):
                curr_dir = complex(0,-1)
            curr_dir *= direc_mp[instruct]
            if curr_dir == complex(0,-1):
                curr_dir = complex(0,1)
            elif curr_dir == complex(0,1):
                curr_dir = complex(0,-1)
    return int(1000*(curr_pos.imag+1) + 4*(curr_pos.real+1) + direc_val_mp[curr_dir])

def part1(input_arr, input_instructs):
    start_pos, grid, corner_mp = create_start_pos_and_grid_and_corner_mp_part1(input_arr)
    return path_find(start_pos, grid, corner_mp, input_instructs)

def create_start_pos_and_grid_and_corner_mp_part2(input_arr):
    """
                                          1   2

                                          3

                                       5  4

                                       6

         |-------|                    |-------|                     |-------|
         |       |                    |   ^   |                     |   ^   |
         | <-6   |                    |   |   |                     |   |   |
         |       |                    |   6   |                     |   1   |
         |       |                    |       |                     |       |
         |-------|                    |-------|                     |-------|
|-------||-------||-------|  |-------||-------||-------|   |-------||-------||-------|
|       ||   ^   ||   ^   |  |   ^   ||   ^   ||       |   |       ||   ^   ||       |
|       ||   |   ||   |   |  |   |   ||   |   ||       |   |       ||   |   ||       |
|   5   ||   1   ||   2   |  |   1   ||   2   ||   4   |   |   5-> ||   3   ||   2-> |
|   |   ||       ||       |  |       ||       ||   |   |   |       ||       ||       |
|   v   ||       ||       |  |       ||       ||   v   |   |       ||       ||       |
|-------||-------||-------|  |-------||-------||-------|   |-------||-------||-------|
         |-------|                    |-------|                     |-------|
         |   ^   |                    |       |                     |   ^   |
         |   |   |                    | <-3   |                     |   |   |
         |   3   |                    |       |                     |   4   |
         |       |                    |       |                     |       |
         |-------|                    |-------|                     |-------|

         |-------|                    |-------|                     |-------|
         |   ^   |                    |       |                     |   ^   |
         |   |   |                    |       |                     |   |   |
         |   3   |                    | <-3   |                     |   5   |
         |       |                    |       |                     |       |
         |-------|                    |-------|                     |-------|
|-------||-------||-------|  |-------||-------||-------|   |-------||-------||-------|
|   ^   ||   ^   ||       |  |       ||   ^   ||   ^   |   |       ||   ^   ||       |
|   |   ||   |   ||       |  |       ||   |   ||   |   |   |       ||   |   ||       |
|   5   ||   4   ||   2   |  |   1   ||   5   ||   4   |   |   1-> ||   6   ||   4-> |
|       ||       ||   |   |  |   |   ||       ||       |   |       ||       ||       |
|       ||       ||   v   |  |   v   ||       ||       |   |       ||       ||       |
|-------||-------||-------|  |-------||-------||-------|   |-------||-------||-------|
         |-------|                    |-------|                     |-------|
         |       |                    |   ^   |                     |   ^   |
         |       |                    |   |   |                     |   |   |
         | <-6   |                    |   6   |                     |   2   |
         |       |                    |       |                     |       |
         |       |                    |-------|                     |-------|
         |-------|
    """

    def get_zone(pos):
        x,y = pos
        if 0 <= y < 50:
            if 50 <= x < 100:
                return 1
            elif 100 <= x < 150:
                return 2
        elif 50 <= y < 100:
            if 50 <= x < 100:
                return 3
        elif 100 <= y < 150:
            if 0 <= x < 50:
                return 5
            elif 50 <= x < 100:
                return 4
        elif 150 <= y < 200:
            if 0 <= x < 50:
                return 6

    def get_connections(grid, corner, zones):
        connections = []
        pos, left, right, up, down = corner
        r_pos = (pos[0]%50, pos[1]%50)
        zone = get_zone(pos)
        if zone == 1:
            if left:
                new_zone = 5
                rel_pos  = (0, 49 - r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(-1,0)))
            if up:
                new_zone = 6
                rel_pos  = (0, r_pos[0])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(0,-1)))
            if right:
                new_zone = 2
                rel_pos  = (0, r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(1,0)))
            if down:
                new_zone = 3
                rel_pos  = (r_pos[0], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,1), complex(0,1)))
        elif zone == 2:
            if left:
                new_zone = 1
                rel_pos  = (49, r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(-1,0)))
            if up:
                new_zone = 6
                rel_pos  = (r_pos[0], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(0,-1)))
            if right:
                new_zone = 4
                rel_pos  = (49, 49-r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(1,0)))
            if down:
                new_zone = 3
                rel_pos  = (49, r_pos[0])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(0,1)))
        elif zone == 3:
            if left:
                new_zone = 5
                rel_pos  = (r_pos[1], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,1), complex(-1,0)))
            if up:
                new_zone = 1
                rel_pos  = (r_pos[0], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(0,-1)))
            if right:
                new_zone = 2
                rel_pos  = (r_pos[1], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(1,0)))
            if down:
                new_zone = 4
                rel_pos  = (r_pos[0], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,1), complex(0,1)))
        elif zone == 4:
            if left:
                new_zone = 5
                rel_pos  = (49, r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(-1,0)))
            if up:
                new_zone = 3
                rel_pos  = (r_pos[0], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(0,-1)))
            if right:
                new_zone = 2
                rel_pos  = (49, 49-r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(1,0)))
            if down:
                new_zone = 6
                rel_pos  = (49, r_pos[0])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(-1,0), complex(0,1)))
        elif zone == 5:
            if left:
                new_zone = 1
                rel_pos  = (0, 49-r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(-1,0)))
            if up:
                new_zone = 3
                rel_pos  = (0, r_pos[0])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(0,-1)))
            if right:
                new_zone = 4
                rel_pos  = (0, r_pos[1])
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(1,0), complex(1,0)))
            if down:
                new_zone = 6
                rel_pos  = (r_pos[0], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[q1]), complex(0,1), complex(0,1)))
        elif zone == 6:
            if left:
                new_zone = 1
                rel_pos  = (r_pos[1], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,1), complex(-1,0)))
            if up:
                new_zone = 5
                rel_pos  = (r_pos[0], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(0,-1)))
            if right:
                new_zone = 4
                rel_pos  = (r_pos[1], 49)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,-1), complex(1,0)))
            if down:
                new_zone = 2
                rel_pos  = (r_pos[0], 0)
                new_pos  = zones[new_zone][rel_pos]
                if grid[complex(new_pos[0], new_pos[1])] != "#":
                    connections.append((complex(new_pos[0], new_pos[1]), complex(0,1), complex(0,1)))
        return connections

    grid = {}
    start_pos = None
    corners = []
    zones   = defaultdict(dict)
    for j, r in enumerate(input_arr):
        for i, c in enumerate(r):
            if c != " ":
                zones[get_zone((i,j))][(i%50,j%50)] = (i,j)
            if c != " ":
                if start_pos == None:
                    start_pos = complex(i,j)
                grid[complex(i,j)] = c
                if c == "#":
                    continue
                left  = True if i == 0 else input_arr[j][i-1] == " "
                right = True if i == len(r)-1 else input_arr[j][i+1] == " "
                up    = True if j == 0 else input_arr[j-1][i] == " "
                down  = True if j == len(input_arr)-1 else input_arr[j+1][i] == " "
                if left or right or up or down:
                    corners.append(([i,j], left, right, up, down))
    corner_mp = {}
    for corner in corners:
        pos = corner[0]
        c_pos = complex(pos[0], pos[1])
        for next_pos, next_dir, direc in get_connections(grid, corner, zones):
            corner_mp[(c_pos, direc)] = (next_pos, next_dir)
    return start_pos, grid, corner_mp

def part2(input_arr, input_instructs):
    start_pos, grid, corner_mp = create_start_pos_and_grid_and_corner_mp_part2(input_arr)
    return path_find(start_pos, grid, corner_mp, input_instructs)

def main():
    print(part1(*read_input()))
    print(part2(*read_input()))

if __name__ == "__main__":
    main()
