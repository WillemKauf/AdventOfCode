from collections import deque
import itertools

def read_input():
    input_num = []
    with open("input/input13.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num

def part_1(input_num):
    grid = {}
    def f(x,y):
        h_w = 0
        v   = x*x + 3*x + 2*x*y + y + y*y + input_num
        while v:
            v &= v - 1
            h_w += 1
        grid[x,y] = h_w % 2 == 0
        return grid[x,y]

    width  = 31
    height = 39
    for j in range(0, height+1):
        for i in range(0, width+1):
            _ = f(i,j)
    queue = deque([((1,1),0,set())])
    ddir  = [prod for prod in itertools.product([-1,0,1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    min_steps = 99999999
    while len(queue):
        curr_pos, num_steps, seen = queue.popleft()
        if num_steps > min_steps:
            continue
        if curr_pos == (width, height):
            min_steps = min(min_steps, num_steps)
        for dd in ddir:
            new_pos = (curr_pos[0]+dd[0], curr_pos[1]+dd[1])
            if 0 <= new_pos[0] < width+1 and 0 <= new_pos[1] < height+1:
                if grid[new_pos[0], new_pos[1]] == 1 and new_pos not in seen:
                    queue.appendleft((new_pos, num_steps+1, seen | set([curr_pos])))
    return min_steps

def part_2(input_num):
    grid = {}
    def f(x,y):
        h_w = 0
        v   = x*x + 3*x + 2*x*y + y + y*y + input_num
        while v:
            v &= v - 1
            h_w += 1
        grid[x,y] = h_w % 2 == 0
        return grid[x,y]

    size = 50
    for j in range(0, size):
        for i in range(0, size):
            _ = f(i,j)
    queue = deque([((1,1),0,set())])
    ddir  = [prod for prod in itertools.product([-1,0,1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    res_seen = set()
    while len(queue):
        curr_pos, num_steps, seen = queue.popleft()
        res_seen.add(curr_pos)
        if num_steps == 50:
            continue
        for dd in ddir:
            new_pos = (curr_pos[0]+dd[0], curr_pos[1]+dd[1])
            if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size:
                if grid[new_pos[0], new_pos[1]] == 1 and new_pos not in seen:
                    queue.appendleft((new_pos, num_steps+1, seen | set([curr_pos])))
    return len(res_seen)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
