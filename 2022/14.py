from collections import deque

def read_input():
    input_arr = []
    max_y = -1
    with open("input/input14.txt", "r") as input_file:
        for line in input_file.readlines():
            curr_arr = []
            line = line.rstrip()
            line = line.split(" -> ")
            for p in line:
                p = p.split(",")
                curr_arr.append([int(xy) for xy in p])
                max_y = max(max_y, int(p[1]))
            input_arr.append(curr_arr)
    return max_y, input_arr

def sign(s):
    return -1 if s < 0 else 1

def get_graph(input_arr):
    graph = {}
    for l in input_arr:
        for k in range(0, len(l)-1):
            p1 = l[k]
            p2 = l[k+1]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                for j in range(0, dy+sign(dy), sign(dy)):
                    graph[(p1[0],p1[1]+j)] = "#"
            elif dy == 0:
                for i in range(0, dx+sign(dx), sign(dx)):
                    graph[(p1[0]+i,p1[1])] = "#"
    return graph

def vis(pos, new_pos, graph):
    if pos in graph:
        c_pos = graph[pos]
    else:
        c_pos = None
    if new_pos in graph:
        c_npos = graph[new_pos]
    else:
        c_npos = None
    print(pos, new_pos, c_pos, c_npos)
    min_x = min([p[0] for p in graph.keys()])
    max_x = max([p[0] for p in graph.keys()])
    min_y = min([p[1] for p in graph.keys()])
    max_y = max([p[1] for p in graph.keys()])
    dx = max_x - min_x
    dy = max_y - min_y
    grid = [["." for _ in range(0, dx+1)] for _ in range(0, dy+1)]
    for p, v in graph.items():
        grid[p[1]-min_y][p[0]-min_x] = v
    for line in grid:
        print("".join(line))

def part1(max_y, input_arr):
    graph = get_graph(input_arr)
    origin = (500,0)
    while True:
        queue = deque([origin])
        breakFlag = False
        while len(queue):
            pos = queue.popleft()
            new_pos = (pos[0],pos[1]+1)
            if new_pos[1] > max_y:
                breakFlag = True
                break
            if new_pos not in graph or graph[new_pos] == ".":
                queue.append(new_pos)
            else:
                if graph[new_pos] != ".":
                    left_pos = (new_pos[0]-1, new_pos[1])
                    if left_pos not in graph or graph[left_pos] == ".":
                        queue.append(left_pos)
                    else: #Something at left position
                        right_pos = (new_pos[0]+1, new_pos[1])
                        if right_pos not in graph or graph[right_pos] == ".":
                            queue.append(right_pos)
                        else: #Something at right position
                            graph[pos] = "o"
                elif graph[new_pos] == ".":
                    queue.append(new_pos)
        if breakFlag:
            break
    return sum([1 for v in graph.values() if v == "o"])

def part2(max_y, input_arr):
    floor = max_y + 2
    graph = get_graph(input_arr)
    origin = (500,0)
    while True:
        queue = deque([origin])
        breakFlag = False
        while len(queue):
            if origin in graph:
                if graph[origin] == "o":
                    breakFlag = True
                    break
            pos = queue.popleft()
            new_pos = (pos[0], pos[1]+1)
            if new_pos[1] == floor:
                graph[new_pos] = "#"
            if new_pos not in graph or graph[new_pos] == ".":
                queue.append(new_pos)
            else:
                if graph[new_pos] != ".":
                    left_pos = (new_pos[0]-1, new_pos[1])
                    if left_pos[1] == floor:
                        graph[left_pos] = "#"
                    if left_pos not in graph or graph[left_pos] == ".":
                        queue.append(left_pos)
                    else: #Something at left position
                        right_pos = (new_pos[0]+1, new_pos[1])
                        if right_pos[1] == floor:
                            graph[right_pos] = "#"
                        if right_pos not in graph or graph[right_pos] == ".":
                            queue.append(right_pos)
                        else: #Something at right position
                            graph[pos] = "o"
                else:
                    queue.append(new_pos)
        if breakFlag:
            break
    return sum([1 for v in graph.values() if v == "o"])

def main():
    max_y, input_arr = read_input()
    print(part1(max_y, input_arr[:]))
    print(part2(max_y, input_arr[:]))

if __name__ == "__main__":
    main()
