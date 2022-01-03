from collections import defaultdict, deque
import itertools
import heapq

def read_input():
    input_lst = []
    with open("input/input20.txt") as input_file:
        for line in input_file:
            line = [i for i in line][:-1]
            input_lst.append(line)
    return input_lst

def parse_graph(input_lst):
    offset       = 2
    nodes        = {}
    unique_nodes = {}
    seen_nodes   = set()
    for j in range(offset, len(input_lst)-offset):
        for i in range(offset, len(input_lst[j])-offset):
            c = input_lst[j][i]
            if c == ".":
                pos = (i-offset, j-offset)
                if input_lst[j-1][i].isupper():
                    c = input_lst[j-2][i]+input_lst[j-1][i]
                elif input_lst[j+1][i].isupper():
                    c = input_lst[j+1][i]+input_lst[j+2][i]
                if input_lst[j][i-1].isupper():
                    c = input_lst[j][i-2]+input_lst[j][i-1]
                elif input_lst[j][i+1].isupper():
                    c = input_lst[j][i+1]+input_lst[j][i+2]
                if c != ".":
                    if c not in ["AA", "ZZ"]:
                        num = "2" if (j == offset or j == len(input_lst)-offset-1 or i == offset or i == len(input_lst[j])-offset-1) else "1"
                        c += num
                    unique_nodes[pos] = c
                nodes[pos] = c

    graph = defaultdict(dict)
    for node in unique_nodes.values():
        if node not in ["AA", "ZZ"]:
            if node[-1] == "1":
                comp_node = node[:-1]+"2"
            elif node[-1] == "2":
                comp_node = node[:-1]+"1"
            graph[node][comp_node] = 1

    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    for start in unique_nodes:
        queue   = deque([(start, set(), 0)])
        c_start = nodes[start]
        while len(queue):
            pos, seen, num_steps = queue.popleft()
            seen.add(pos)
            c = nodes[pos]
            if c != "." and c not in [c_start, "AA"]:
                graph[c_start][c] = num_steps
            for dd in ddir:
                new_pos = pos[0]+dd[0], pos[1]+dd[1]
                if new_pos in nodes:
                    if new_pos not in seen:
                        queue.appendleft((new_pos, seen, num_steps+1))
    return graph

def part_1(input_lst):
    graph     = parse_graph(input_lst)
    queue     = deque([("AA", set(), 0)])
    min_steps = int(1e12)
    while len(queue):
        pos, seen, num_steps = queue.popleft()
        new_seen = seen | set([pos])
        if num_steps > min_steps:
            continue
        if pos == "ZZ":
            min_steps = min(num_steps, min_steps)
        for n, dist in graph[pos].items():
            if n not in new_seen:
                queue.appendleft((n, new_seen, num_steps+dist))
    return min_steps

def part_2(input_lst):
    graph = parse_graph(input_lst)
    queue = []
    heapq.heappush(queue, (0, 0, "AA", []))
    min_steps   = int(1e12)
    seen_states = {}
    while len(queue):
        num_steps, level, pos, seen = heapq.heappop(queue)
        if num_steps > min_steps:
            continue
        pos_rep  = pos + str(level)
        new_seen = seen + [pos_rep]
        if pos_rep == "ZZ0":
            min_steps = min(num_steps, min_steps)
        rep = (level, pos)
        if rep in seen_states:
            if num_steps < seen_states[rep]:
                seen_states[rep] = num_steps
            else:
                continue
        else:
            seen_states[rep] = num_steps
        for n, dist in graph[pos].items():
            n_rep = n + str(level)
            if n_rep not in new_seen:
                if pos[:-1] == n[:-1]:
                    continue
                if n[-1] == "1":
                    new_seen = new_seen + [n_rep]
                    n = n[:-1]+"2"
                    heapq.heappush(queue, ((num_steps + 1 + dist), level+1, n, new_seen))
                elif n[-1] == "2":
                    if level != 0:
                        new_seen = new_seen + [n_rep]
                        n = n[:-1]+"1"
                        heapq.heappush(queue, ((num_steps + 1 + dist), level-1, n, new_seen))
                else:
                    heapq.heappush(queue, ((num_steps+dist), level, n, new_seen))
    return min_steps

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
