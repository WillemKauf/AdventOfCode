import re

def read_input():
    input_arr = []
    with open("input/input15.txt", "r") as input_file:
        for line in input_file.readlines():
            regex = re.compile(r"[+-]?\d+")
            matches = regex.findall(line)
            input_arr.append([int(i) for i in matches])
    return input_arr

def vis(graph):
    min_x = min([p[0] for p in graph.keys()])
    max_x = max([p[0] for p in graph.keys()])
    min_y = min([p[1] for p in graph.keys()])
    max_y = max([p[1] for p in graph.keys()])
    dx    = max_x - min_x
    dy    = max_y - min_y
    grid = [["." for _ in range(0, dx+1)] for _ in range(0, dy+1)]
    for p, v in graph.items():
        grid[p[1]-min_y][p[0]-min_x] = v
    for line in grid:
        line = [str(c) for c in line]
        print("".join(line))

def part1(input_arr):
    res = 0
    y = 2000000
    ranges = []
    seen = set()
    for line in input_arr:
        sensor = (line[0], line[1])
        beacon = (line[2], line[3])
        dx     = abs(sensor[0]-beacon[0])
        dy     = abs(sensor[1]-beacon[1])
        if sensor[1] == y and sensor not in seen:
            res -= 1
            seen.add(sensor)
        if beacon[1] == y and beacon not in seen:
            res -= 1
            seen.add(beacon)
        max_dist = dx+dy
        max_allow_dx = max_dist - abs(sensor[1]-y)
        if max_allow_dx >= 0:
            start = sensor[0]-max_allow_dx
            end   = sensor[0]+max_allow_dx
            ranges.append(sorted([start, end]))
    ranges.sort()
    curr_range = ranges[0]
    new_ranges = []
    for i in range(1, len(ranges)):
        a,b = curr_range
        c,d = ranges[i]
        if b >= c:
            curr_range = [a, max(b,d)]
    res += curr_range[1]-curr_range[0]+1
    return res

def part2(input_arr):
    mn = 0
    mx = 4000000
    not_seen = set()
    graph = {}
    mp = {}
    slope_sets = [[(1,1), (1,-1)], [(-1,1), (-1,-1)]]
    for line in input_arr:
        sensor     = (line[0], line[1])
        beacon     = (line[2], line[3])
        dx         = abs(sensor[0]-beacon[0])
        dy         = abs(sensor[1]-beacon[1])
        max_dist   = dx+dy
        corners    = [(sensor[0]-max_dist-1, sensor[1]), (sensor[0]+max_dist+1, sensor[1])]
        mp[sensor] = (max_dist, corners)
    for sensor, (max_dist, corners) in mp.items():
        for corner, slopes in zip(corners, slope_sets):
            for slope in slopes:
                for i in range(0, max_dist+1):
                    new_x = corner[0]+i*slope[0]
                    new_y = corner[1]+i*slope[1]
                    seen = False
                    for sensor2, (max_dist2, _) in mp.items():
                        if sensor == sensor2:
                            continue
                        dx = abs(new_x-sensor2[0])
                        dy = abs(new_y-sensor2[1])
                        if dx+dy <= max_dist2:
                            seen = True
                            break
                    if not seen:
                        return new_x*mx+new_y
    return None

def main():
    input_arr = read_input()
    print(part1(input_arr[:]))
    print(part2(input_arr[:]))

if __name__ == "__main__":
    main()
