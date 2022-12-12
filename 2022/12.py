from collections import deque

def read_input():
    input_arr = []
    with open("input/input12.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append([c for c in line])
    return input_arr

def map_height(c):
    if c == "S":
        return "a"
    elif c == "E":
        return "z"
    else:
        return c

def part1(input_arr):
    start_pos = (None, None)
    for j in range(0, len(input_arr)):
        for i in range(0, len(input_arr[j])):
            if input_arr[j][i] == "S":
                start_pos = (i,j)
    queue = deque([(start_pos, 0)])
    ddir = [[-1,0],[1,0], [0,1],[0,-1]]
    seen = set([start_pos])
    min_steps = int(1e12)
    m = len(input_arr)
    n = len(input_arr[0])
    while len(queue):
        curr_pos, num_steps = queue.popleft()
        if num_steps >= min_steps:
            continue
        node = input_arr[curr_pos[1]][curr_pos[0]]
        if node == "E":
            min_steps = min(min_steps, num_steps)
            continue
        for dd in ddir:
            new_pos = (curr_pos[0]+dd[0], curr_pos[1]+dd[1])
            if new_pos in seen:
                continue
            if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                neighbour = input_arr[new_pos[1]][new_pos[0]]
                if ord(map_height(neighbour)) - ord(map_height(node)) <= 1:
                    seen.add(new_pos)
                    queue.append((new_pos, num_steps+1))
    return min_steps

def part2(input_arr):
    start_posses = []
    for j in range(0, len(input_arr)):
        for i in range(0, len(input_arr[j])):
            if input_arr[j][i] == "S" or input_arr[j][i] == "a":
                start_posses.append((i,j))

    min_steps = int(1e12)
    for start_pos in start_posses:
        queue = deque([(start_pos, 0)])
        ddir = [[-1,0],[1,0],[0,1],[0,-1]]
        seen = set([start_pos])
        m = len(input_arr)
        n = len(input_arr[0])
        while len(queue):
            curr_pos, num_steps = queue.popleft()
            if num_steps >= min_steps:
                continue
            node = input_arr[curr_pos[1]][curr_pos[0]]
            if node == "E":
                min_steps = min(min_steps, num_steps)
                continue
            for dd in ddir:
                new_pos = (curr_pos[0]+dd[0], curr_pos[1]+dd[1])
                if new_pos in seen:
                    continue
                if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                    neighbour = input_arr[new_pos[1]][new_pos[0]]
                    if ord(map_height(neighbour)) - ord(map_height(node)) <= 1:
                        seen.add(new_pos)
                        queue.append((new_pos, num_steps+1))
    return min_steps


def main():
    input_arr = read_input()
    print(part1(input_arr[:]))
    print(part2(input_arr[:]))

if __name__ == "__main__":
    main()
