from collections import deque, defaultdict
import itertools

"""
   Another TSP problem. Go look at 2015 day 9 for an interesting implementation of ant colony optimization for TSP.
   Here I'm going to use BFS -> brute force (all permutations) because I don't feel like re-coding ant colony
   optimization for the given input.
"""

def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def parse_graph(input_lst):
    ddir = [prod for prod in itertools.product([-1,0,1], repeat=2) if abs(prod[0]) + abs(prod[1]) == 1]
    def bfs(x, y, goal):
        queue     = deque([((x,y),0)])
        seen      = set()
        c         = input_lst[y][x]
        min_steps = int(1e12)
        while len(queue):
            curr_pos, num_steps = queue.popleft()
            curr_c              = input_lst[curr_pos[1]][curr_pos[0]]
            if curr_pos in seen:
                continue
            seen.add(curr_pos)
            if curr_c == goal:
                min_steps = min(min_steps, num_steps)
            for dd in ddir:
                new_x, new_y = curr_pos[0]+dd[0], curr_pos[1]+dd[1]
                if 0 <= new_x < len(input_lst[y]) and 0 <= new_y < len(input_lst):
                    if input_lst[new_y][new_x] != "#" and (new_x, new_y) not in seen:
                        queue.append(((new_x, new_y), num_steps+1))
        return min_steps

    nums  = {}
    graph = defaultdict(dict)
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            c = input_lst[j][i]
            if c not in ["#", "."]:
                nums[c] = (i,j)

    for n in nums:
        for n2 in nums:
            if n == n2:
                continue
            if n2 in graph[n] or n in graph[n2]:
                continue
            graph[n][n2] = bfs(*nums[n], n2)
            graph[n2][n] = graph[n][n2]
    return nums, graph

def part_1(input_lst, add_zero=False):
    nums, graph = parse_graph(input_lst)
    min_cost    = int(1e12)
    perms       = [perm+tuple(int(add_zero)*["0"]) for perm in itertools.permutations(nums) if perm[0] == "0"]
    for perm in perms:
        cost = 0
        for i in range(1, len(perm)):
            cost += graph[perm[i-1]][perm[i]]
        min_cost = min(min_cost, cost)
    return min_cost

def main():
    print(part_1(read_input()))
    print(part_1(read_input(), True))

if __name__ == "__main__":
    main()
