from collections import deque

def read_input():
    input_arr = set()
    with open("input/input18.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.add(tuple([int(i) for i in line.split(",")]))
    return input_arr

def part1(input_arr):
    seen   = set()
    res    = 0
    ddir   = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
    points = set(input_arr)
    for point in points:
        for dd in ddir:
            neighbour_point = tuple([point[i] + dd[i] for i in range(0,3)])
            if neighbour_point not in points:
                res += 1
    return res

def part2(input_arr):
    min_x  = min([xyz[0]-1 for xyz in input_arr])
    max_x  = max([xyz[0]+1 for xyz in input_arr])
    min_y  = min([xyz[1]-1 for xyz in input_arr])
    max_y  = max([xyz[1]+1 for xyz in input_arr])
    min_z  = min([xyz[2]-1 for xyz in input_arr])
    max_z  = max([xyz[2]+1 for xyz in input_arr])
    is_valid = lambda n : ((min_x <= n[0] <= max_x) and (min_y <= n[1] <= max_y) and (min_z <= n[2] <= max_z))
    seen   = set()
    res    = 0
    ddir   = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
    points = set(input_arr)
    queue = deque([(min_x, min_y, min_z)])
    while len(queue):
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        for dd in ddir:
            neighbour_point = tuple([node[i] + dd[i] for i in range(0,3)])
            if not is_valid(neighbour_point):
                continue
            if neighbour_point not in points:
                queue.append(neighbour_point)
            else:
                res += 1
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
