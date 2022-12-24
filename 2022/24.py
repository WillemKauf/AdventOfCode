from collections import defaultdict
import heapq

def read_input():
    input_arr = []
    with open("input/input24.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append([c for c in line])
    return input_arr

class Blizzard():
    def __init__(self, pos, v):
        self.pos = pos
        self.v   = v

def get_grid(input_arr):
    grid = []
    blizz_mp = set([">", "v", "^", "<"])
    for j, r in enumerate(input_arr):
        for i, c in enumerate(r):
            if c in blizz_mp:
                grid.append(Blizzard((i,j), c))
    height = len(input_arr)
    width = len(input_arr[0])
    return grid, height, width

def vis(pos, taken_spots, height, width):
    grid = [["." for _ in range(0, width)] for _ in range(0, height)]
    for i in range(0, width):
        if i != 1:
            grid[0][i] = "#"
        if i != width-2:
            grid[height-1][i] = "#"
    for j in range(0, height):
        grid[j][0] = "#"
        grid[j][width-1] = "#"
    grid[pos[1]][pos[0]] = "E"
    for t_pos in taken_spots:
        grid[t_pos[1]][t_pos[0]] = "X"
    for l in grid:
        print("".join([str(c) for c in l]))
    print()

def get_taken_spots(grid, height, width):
    blizz_mp = {">":(1,0), "v":(0,1), "^":(0,-1), "<":(-1,0)}
    taken_spots = defaultdict(set)
    seen        = set()
    it          = 0
    while True:
        for item in grid:
            new_x = item.pos[0] + blizz_mp[item.v][0]
            new_y = item.pos[1] + blizz_mp[item.v][1]
            if new_x == width-1:
                new_x = 1
            elif new_x == 0:
                new_x = width-2
            if new_y == 0:
                new_y = height-2
            elif new_y == height-1:
                new_y = 1
            new_pos = (new_x, new_y)
            item.pos = new_pos
        blizz_locs = tuple([(item.pos,item.v) for item in grid])
        if blizz_locs in seen:
            break
        for item in grid:
            taken_spots[it].add(item.pos)
        seen.add(blizz_locs)
        it += 1
    return taken_spots

def A_star(start, goal, height, width, taken_spots, blizz_it_start=0):
    distance_to_exit    = lambda p: abs(goal[0]-p[0])+abs(goal[1]-p[1])
    queue               = [(distance_to_exit(start), 0, start)]
    min_steps           = int(1e12)
    ddir                = [[1,0],[0,1],[-1,0],[0,-1],[0,0]]
    seen                = {}
    last_blizz_it       = None
    while len(queue):
        _, num_steps, curr_pos = heapq.heappop(queue)
        blizz_it = (blizz_it_start+num_steps)%len(taken_spots.keys())
        state    = (curr_pos, blizz_it)
        if state in seen:
            if seen[state] <= num_steps:
                continue
        seen[state] = num_steps
        if num_steps >= min_steps:
            continue
        if curr_pos == goal:
            if num_steps < min_steps:
                min_steps = num_steps
                last_blizz_it = blizz_it
            continue
        for dd in ddir:
            new_pos = (curr_pos[0]+dd[0], curr_pos[1]+dd[1])
            if new_pos in taken_spots[blizz_it]:
                continue
            if (0 < new_pos[0] < width-1 and 0 < new_pos[1] < height-1) or new_pos == goal or new_pos == start:
                heapq.heappush(queue, (distance_to_exit(new_pos), num_steps+1, new_pos))
    return min_steps, last_blizz_it

def part1(input_arr):
    grid, height, width = get_grid(input_arr)
    taken_spots         = get_taken_spots(grid, height, width)
    start               = (1,0)
    goal                = (width-2, height-1)
    return A_star(start, goal, height, width, taken_spots)[0]

def part2(input_arr):
    grid, height, width = get_grid(input_arr)
    taken_spots         = get_taken_spots(grid, height, width)
    start               = (1,0)
    goal                = (width-2, height-1)
    first_trip, blizz_it  = A_star(start, goal, height, width, taken_spots)
    second_trip, blizz_it = A_star(goal, start, height, width, taken_spots, blizz_it)
    third_trip, _         = A_star(start, goal, height, width, taken_spots, blizz_it)
    return first_trip+second_trip+third_trip

def main():
    input_arr = read_input()
    #print(part1(input_arr[:]))
    print(part2(input_arr[:]))

if __name__ == "__main__":
    main()
