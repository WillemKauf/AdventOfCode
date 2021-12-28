from Intcode import IntCode
from collections import deque
from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input15.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    ddir_map = {1:complex(0,1), 2:complex(0,-1), 3:complex(1,0), 4:complex(-1,0)}
    queue    = deque([(IntCode(input_lst), complex(0,0), 0)])
    seen     = set()
    while len(queue):
        ic, curr_pos, num_steps = queue.popleft()
        num_steps += 1
        seen.add(curr_pos)
        for dd in [1,2,3,4]:
            curr_ic = deepcopy(ic)
            curr_ic.set_input([dd])
            ddir    = ddir_map[dd]
            new_pos = curr_pos + ddir
            if new_pos in seen:
                continue
            output = curr_ic.parse_tape_with_n_output(1)[0]
            if output == 1:
                queue.append((curr_ic, new_pos, num_steps))
            if output == 2:
                return num_steps
    return None

def part_2(input_lst):
    ddir_map = {1:complex(0,1), 2:complex(0,-1), 3:complex(1,0), 4:complex(-1,0)}
    queue    = deque([(IntCode(input_lst), complex(0,0), 0)])
    grid     = {}
    while len(queue):
        ic, curr_pos, num_steps = queue.popleft()
        num_steps += 1
        grid[curr_pos] = "."
        for dd in [1,2,3,4]:
            curr_ic = deepcopy(ic)
            curr_ic.set_input([dd])
            ddir    = ddir_map[dd]
            new_pos = curr_pos + ddir
            if new_pos in grid:
                continue
            output = curr_ic.parse_tape_with_n_output(1)[0]
            if output == 1:
                queue.append((curr_ic, new_pos, num_steps))
            if output == 2:
                grid[new_pos] = "O"
                break

    start_pos = None
    for pos, v in grid.items():
        if v == "O":
            start_pos = pos
            break

    def dfs(pos, num_steps, seen):
        max_steps = num_steps
        num_steps += 1
        seen.add(pos)
        for dd in ddir_map.values():
            new_pos = pos+dd
            if new_pos in grid and new_pos not in seen:
                max_steps = max(max_steps, dfs(new_pos, num_steps, seen))
        return max_steps
    return dfs(start_pos, 0, set())

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
