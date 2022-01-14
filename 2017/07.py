from collections import defaultdict, Counter

def part_1():
    def read_input():
        v_dct = {}
        c_dct = {}
        with open("input/input7.txt") as input_file:
            for line in input_file:
                line        = line.rstrip().split(" -> ")
                v           = line[0].split()
                v_dct[v[0]] = int(v[1][1:-1])
                if len(line) > 1:
                    for c in line[1].split(", "):
                        c_dct[c] = v[0]
        return v_dct, c_dct

    def recursive_search(node, d):
        if node not in c_dct:
            return node, d
        return recursive_search(c_dct[node], d+1)

    v_dct, c_dct = read_input()
    max_depth   = -1
    bottom_node = None
    for node in c_dct:
        parent_node, depth = recursive_search(node, 0)
        if depth > max_depth:
            max_depth   = depth
            bottom_node = parent_node
    return bottom_node

def part_2(bottom_node):
    def read_input():
        v_dct = {}
        c_dct = defaultdict(list)
        with open("input/input7.txt") as input_file:
            for line in input_file:
                line        = line.rstrip().split(" -> ")
                v           = line[0].split()
                v_dct[v[0]] = int(v[1][1:-1])
                if len(line) > 1:
                    for c in line[1].split(", "):
                        c_dct[v[0]].append(c)
        return v_dct, c_dct

    def recursive_search(node, s):
        c_sums = {c:v_dct[c] for c in c_dct[node]}
        for c in c_dct[node]:
            res, flag = recursive_search(c, s)
            if flag == True:
                return res, flag
            c_sums[c] += res
        counter = Counter(c_sums.values())
        if len(counter) not in [0, 1]:
            d = 0
            for v, n in counter.items():
                if n == 1:
                    d += v
                else:
                    d -= v
            for c in c_dct[node]:
                v = c_sums[c]
                if counter[v] == 1:
                    return v_dct[c]-d, True
        return sum(c_sums.values()), False
    v_dct, c_dct = read_input()
    return recursive_search(bottom_node, 0)[0]

def main():
    bottom_node = part_1()
    print(bottom_node)
    print(part_2(bottom_node))

if __name__ == "__main__":
    main()
