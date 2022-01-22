from collections import deque
import hashlib

def read_input():
    input_str = []
    with open("input/input17.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    queue     = deque([((0,0), 0, "")])
    open_lst  = ["b", "c", "d", "e", "f"]
    ddir_mp   = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
    min_steps = int(1e12)
    path      = None
    while len(queue):
        pos, num_steps, seen = queue.popleft()
        if num_steps > min_steps:
            continue
        if pos == (3,3):
            if num_steps < min_steps:
                path = seen
                min_steps = num_steps
        for ind, n in enumerate(["U", "D", "L", "R"]):
            dd      = ddir_mp[n]
            new_pos = (pos[0] + dd[0], pos[1] + dd[1])
            if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                hsh = hashlib.md5((input_str + seen).encode()).hexdigest()
                if hsh[ind] in open_lst:
                    queue.append((new_pos, num_steps+1, seen+n))
    return path

def part_2(input_str):
    queue     = deque([((0,0), 0, "")])
    open_lst  = ["b", "c", "d", "e", "f"]
    ddir_mp   = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
    max_steps = -1
    path      = None
    while len(queue):
        pos, num_steps, seen = queue.popleft()
        if pos == (3,3):
            max_steps = max(max_steps, num_steps)
            continue
        for ind, n in enumerate(["U", "D", "L", "R"]):
            dd      = ddir_mp[n]
            new_pos = (pos[0] + dd[0], pos[1] + dd[1])
            if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                hsh = hashlib.md5((input_str + seen).encode()).hexdigest()
                if hsh[ind] in open_lst:
                    queue.append((new_pos, num_steps+1, seen+n))
    return max_steps


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
