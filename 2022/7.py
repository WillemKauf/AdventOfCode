from collections import defaultdict

def read_input():
    input_arr = []
    with open("input/input7.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append(line)
    return input_arr

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return repr(f"{self.name}, {self.size}")

def create_graph(input_arr):
    graph    = defaultdict(set)
    curr_dir = ""
    seen     = defaultdict(int)
    for cmd in input_arr:
        if cmd[0] == "$":
            if cmd[2:4] == "cd":
                dr = cmd[5:]
                if dr == "..":
                    for p, cs in graph.items():
                        if curr_dir in cs:
                            curr_dir = p
                elif curr_dir == "":
                    dr = cmd[5:]
                    if dr != "/":
                        dr += str(seen[cmd[5:]])
                        seen[cmd[5:]] += 1
                    graph[dr] = set()
                    curr_dir = dr
                else:
                    dr = cmd[5:]
                    if dr != "/":
                        dr += str(seen[cmd[5:]])
                        seen[cmd[5:]] += 1
                    graph[curr_dir].add(dr)
                    curr_dir = dr
        else:
            if cmd[0:3] == "dir":
                dr = cmd[0:3]
                dr += str(seen[cmd[4:]])
                seen[cmd[4:]] += 1
                graph[curr_dir].add(dr)
            else:
                size, name = cmd.split(" ")
                graph[curr_dir].add(File(name, size))
    return graph

def recurse(node, graph, graph_vals):
    curr_val = 0
    for neighbour in graph[node]:
        if isinstance(neighbour, File):
            curr_val += int(neighbour.size)
        else:
            curr_val += recurse(neighbour, graph, graph_vals)
    graph_vals[node] = curr_val
    return curr_val

def part1(input_arr):
    graph = create_graph(input_arr)
    graph_vals = defaultdict(int)
    recurse("/", graph, graph_vals)
    res = 0
    for d in graph_vals.values():
        if d <= 100000:
            res += d
    return res

def part2(input_arr):
    graph = create_graph(input_arr)
    graph_vals = defaultdict(int)
    recurse("/", graph, graph_vals)
    required_space = 30000000
    total_space    = 70000000
    used_space = graph_vals["/"]
    min_d = int(1e120)
    for d in graph_vals.values():
        new_space = total_space - used_space + d
        if new_space >= required_space:
            min_d = min(min_d, d)
    return min_d

def main():
    print(part1(read_input()))
    print(part2(read_input()))

if __name__ == "__main__":
    main()
