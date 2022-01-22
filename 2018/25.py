from collections import deque, defaultdict

def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            input_lst.append([int(i) for i in line.rstrip().split(",")])
    return input_lst

def part_1(input_lst):
    res  = 0
    seen = set()
    graph = defaultdict(set)
    for i, p1 in enumerate(input_lst):
        for j, p2 in enumerate(input_lst):
            sorted_rep = tuple(sorted([i,j]))
            if i == j or sorted_rep in seen:
                continue
            seen.add(sorted_rep)
            d = 0
            for k in range(0, 4):
                d += abs(p1[k]-p2[k])
            if d <= 3:
                graph[i].add(j)
                graph[j].add(i)

    seen = set()
    for i in range(0, len(input_lst)):
        queue = deque([i])
        if i in seen:
            continue
        res += 1
        while len(queue):
            curr_i = queue.popleft()
            if curr_i in seen:
                continue
            seen.add(curr_i)
            for n in graph[curr_i]:
                queue.append(n)
    return res

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
