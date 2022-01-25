from collections import deque, defaultdict
import heapq
import itertools

class Graph:
    def __init__(self):
        self.nodes      = {}

    def add_node(self, node):
        self.nodes[node.name] = node

class Node:
    def __init__(self, name, neighbours):
        self.name        = name
        self.neighbours  = neighbours

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    def parse_graph(input_lst):
        graph = Graph()
        ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
        def bfs(start):
            seen        = set()
            queue       = deque([(start, 0, set())])
            start_c     = input_lst[start[1]][start[0]]
            neighbours  = {}
            while len(queue):
                curr_pos, num_steps, needed_keys = queue.popleft()
                c = input_lst[curr_pos[1]][curr_pos[0]]
                new_needed_keys = set(needed_keys)
                if c.isupper():
                    new_needed_keys.add(c.lower())
                elif c.islower():
                    if c != start_c:
                        neighbours[c] = tuple([num_steps, needed_keys])
                for dd in ddir:
                    new_pos = curr_pos[0] + dd[0], curr_pos[1] + dd[1]
                    if 0 <= new_pos[0] < len(input_lst[0]) and 0 <= new_pos[1] < len(input_lst):
                        if input_lst[new_pos[1]][new_pos[0]] != "#" and new_pos not in seen:
                            seen.add(new_pos)
                            queue.append((new_pos, num_steps+1, new_needed_keys))
            return Node(start_c, neighbours)

        unique_keys = set()
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                c = input_lst[j][i]
                if c not in ["#", "."]:
                    if c.islower():
                        unique_keys.add(c)
                    if c.islower() or c == "@":
                        node = bfs((i,j))
                        graph.add_node(node)

        return graph, unique_keys
    graph, unique_keys = parse_graph(input_lst)
    queue              = []
    num_needed_keys    = len(unique_keys)
    seen               = {}
    start              = "@"
    min_steps          = int(1e12)
    heapq.heappush(queue, (0, 0, start, set()))
    while len(queue):
        num_keys, num_steps, pos, keys = heapq.heappop(queue)
        num_keys   *= -1
        new_keys    = set(keys)
        if pos not in keys and pos != start:
            num_keys += 1
            new_keys.add(pos)
        if num_keys == num_needed_keys:
            min_steps = min(min_steps, num_steps)
            continue
        node = graph.nodes[pos]
        for new_pos in node.neighbours:
            dist, needed_keys = node.neighbours[new_pos]
            if needed_keys.issubset(new_keys):
                new_rep   = tuple([new_pos, tuple(sorted(new_keys | set([new_pos])))])
                new_steps = num_steps + dist
                if new_rep in seen:
                    if new_steps >= seen[new_rep]:
                        continue
                seen[new_rep] = new_steps
                if new_steps >= min_steps:
                    continue
                heapq.heappush(queue, (-num_keys, new_steps, new_pos, new_keys))
    return min_steps

def part_2(input_lst):
    def parse_graph(input_lst):
        graph = Graph()
        ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
        def bfs(start):
            seen        = set()
            queue       = deque([(start, 0, set())])
            start_c     = input_lst[start[1]][start[0]]
            neighbours  = {}
            while len(queue):
                curr_pos, num_steps, needed_keys = queue.popleft()
                c = input_lst[curr_pos[1]][curr_pos[0]]
                new_needed_keys = set(needed_keys)
                if c.isupper():
                    new_needed_keys.add(c.lower())
                elif c.islower():
                    if c != start_c:
                        neighbours[c] = tuple([num_steps, needed_keys])
                for dd in ddir:
                    new_pos = curr_pos[0] + dd[0], curr_pos[1] + dd[1]
                    if 0 <= new_pos[0] < len(input_lst[0]) and 0 <= new_pos[1] < len(input_lst):
                        if input_lst[new_pos[1]][new_pos[0]] != "#" and new_pos not in seen:
                            seen.add(new_pos)
                            queue.append((new_pos, num_steps+1, new_needed_keys))
            return Node(start_c, neighbours)

        unique_keys = set()
        cnt         = 1
        ddir_diag   = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 2]
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                if input_lst[j][i] == "@":
                    input_lst[j][i] = "#"
                    for di,dj in ddir:
                        input_lst[j+dj][i+di] = "#"
                    for di, dj in ddir_diag:
                        input_lst[j+dj][i+di] = str(cnt)
                        cnt += 1
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                c = input_lst[j][i]
                if c not in ["#", "."]:
                    if c.islower():
                        unique_keys.add(c)
                    if c.islower() or c in ["1","2","3","4"]:
                        node = bfs((i,j))
                        graph.add_node(node)

        return graph, unique_keys
    graph, unique_keys = parse_graph(input_lst)
    queue              = []
    num_needed_keys    = len(unique_keys)
    seen               = {}
    start              = ["1","2","3","4"]
    min_steps          = int(1e12)
    heapq.heappush(queue, (0, 0, start, set()))
    while len(queue):
        num_keys, num_steps, posses, keys = heapq.heappop(queue)
        num_keys   *= -1
        new_keys    = set(keys)
        for pos in posses:
            if pos not in keys and pos not in start:
                num_keys += 1
                new_keys.add(pos)
        if num_keys == num_needed_keys:
            min_steps = min(min_steps, num_steps)
            return min_steps
        for i, pos in enumerate(posses):
            node = graph.nodes[pos]
            for new_pos in node.neighbours:
                dist, needed_keys = node.neighbours[new_pos]
                if needed_keys.issubset(new_keys):
                    new_posses = posses[:i] + [new_pos] + posses[i+1:]
                    new_rep    = tuple([tuple(new_posses), tuple(sorted(new_keys | set([new_pos])))])
                    new_steps  = num_steps + dist
                    if new_rep in seen:
                        if new_steps >= seen[new_rep]:
                            continue
                    seen[new_rep] = new_steps
                    if new_steps >= min_steps:
                        continue
                    heapq.heappush(queue, (-num_keys, new_steps, new_posses, new_keys))
    return min_steps

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
