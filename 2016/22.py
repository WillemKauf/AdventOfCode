from collections import namedtuple
from copy import deepcopy
import heapq
import itertools

class Data:
    def __init__(self, size, used, avail, want):
        self.size  = size
        self.used  = used
        self.avail = avail
        self.want  = want

    def __str__(self):
        s = f"{self.used}/{self.size} {self.avail}"
        if self.want:
            return s+"Y"
        return s

def read_input():
    input_lst = []
    with open("input/input22.txt") as input_file:
        tupNode = namedtuple("Node", ["x", "y", "size", "used", "avail"])
        input_file.readline()
        input_file.readline()
        for line in input_file:
            line  = line.rstrip().split()
            xy    = line[0].split('-')
            x     = int(xy[1][1:])
            y     = int(xy[2][1:])
            size  = int(line[1][:-1])
            used  = int(line[2][:-1])
            avail = int(line[3][:-1])
            input_lst.append(tupNode(x,y,size,used,avail))
    return input_lst

def read_input_as_grid():
    with open("input/input22.txt") as input_file:
        max_x = int(input_file.read().splitlines()[-1].split()[0].split("-")[1][1:])
    max_y = 0
    input_dct = {}
    with open("input/input22.txt") as input_file:
        input_file.readline()
        input_file.readline()
        for line in input_file:
            line  = line.rstrip().split()
            xy    = line[0].split('-')
            x     = int(xy[1][1:])
            y     = int(xy[2][1:])
            size  = int(line[1][:-1])
            used  = int(line[2][:-1])
            avail = int(line[3][:-1])
            max_y = max(max_y, y)
            want  = False
            if (x,y) == (max_x, 0):
                want = True
            if used == 0:
                empty_pos = (x,y)
            input_dct[(x,y)] = Data(size, used, avail, want)
    return input_dct, (max_x, 0), empty_pos, max_x, max_y

def part_1(input_lst):
    res = 0
    for node_a in input_lst:
        for node_b in input_lst:
            if node_a == node_b:
                continue
            if node_a.used != 0:
                if node_a.used <= node_b.avail:
                    res += 1
    return res

def part_2(input_dct, d_pos, e_pos, max_x, max_y):
    ddir        = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    seen_states = {}
    queue       = []
    min_steps   = int(1e12)
    cnt         = 0
    heapq.heappush(queue, (0, 0, 0, cnt, d_pos, e_pos, deepcopy(input_dct)))
    while len(queue):
        _, _, num_steps, _, data_pos, empty_pos, state = heapq.heappop(queue)
        if num_steps > min_steps:
            continue
        if data_pos == (0,0):
            min_steps = min(num_steps, min_steps)
            return min_steps
        rep = (data_pos, empty_pos)
        if rep in seen_states:
            continue
        seen_states[rep] = num_steps
        for dd in ddir: #Move data, swap data pos with empty (new) pos
            new_pos = (data_pos[0] + dd[0], data_pos[1] + dd[1])
            if 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] <= max_y:
                if new_pos == empty_pos:
                    new_state = deepcopy(state)
                    new_state[data_pos].used, new_state[new_pos].used = new_state[new_pos].used, new_state[data_pos].used
                    new_state[data_pos].avail = new_state[data_pos].size - new_state[data_pos].used
                    new_state[new_pos].avail  = new_state[new_pos].size - new_state[new_pos].used
                    goal_dist  = new_pos[0] + new_pos[1]
                    empty_dist = abs(new_pos[0]-data_pos[0]) + abs(new_pos[1]-data_pos[1])
                    cnt += 1
                    heapq.heappush(queue, (goal_dist, empty_dist, num_steps+1, cnt, new_pos, data_pos, new_state))

        for dd in ddir: #Move empty, swap empty pos with new pos.
            new_pos = (empty_pos[0] + dd[0], empty_pos[1] + dd[1])
            if 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] <= max_y:
                if new_pos == data_pos:
                    continue
                if state[new_pos].used <= state[empty_pos].avail:
                    new_state = deepcopy(state)
                    new_state[empty_pos].used, new_state[new_pos].used = new_state[new_pos].used, new_state[empty_pos].used
                    new_state[empty_pos].avail = new_state[empty_pos].size - new_state[empty_pos].used
                    new_state[new_pos].avail   = new_state[new_pos].size - new_state[new_pos].used
                    goal_dist  = data_pos[0] + data_pos[1]
                    empty_dist = abs(new_pos[0]-data_pos[0]) + abs(new_pos[1]-data_pos[1])
                    cnt += 1
                    heapq.heappush(queue, (goal_dist, empty_dist, num_steps+1, cnt, data_pos, new_pos, new_state))
    return min_steps

def main():
    print(part_1(read_input()))
    print(part_2(*read_input_as_grid()))

if __name__ == "__main__":
    main()
