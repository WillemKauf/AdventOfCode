from collections import defaultdict
import copy
class Elf():
    def __init__(self):
        self.proposed = None

def read_input():
    input_arr = []
    with open("input/input23.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append([c for c in line])
    grid = {}
    for j, r in enumerate(input_arr):
        for i, c in enumerate(r):
            if c == "#":
                grid[(i,len(input_arr)-1-j)] = Elf()
            else:
                grid[(i,len(input_arr)-1-j)] = c
    return grid

def vis(graph):
    print("-------------")
    min_x = min([p[0] for p in graph.keys()])
    max_x = max([p[0] for p in graph.keys()])
    min_y = min([p[1] for p in graph.keys()])
    max_y = max([p[1] for p in graph.keys()])
    dx    = max_x - min_x
    dy    = max_y - min_y
    grid = [["." for _ in range(0, dx+1)] for _ in range(0, dy+1)]
    print(min_x, max_x, min_y, max_y)
    for p, v in graph.items():
        grid[max_y-p[1]][p[0]-min_x] = v
    for line in grid:
        line = [c if c == "." else "#" for c in line]
        print("".join(line))

def part1(grid):
    ddir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
    steps = [[ddir[1],ddir[4],ddir[7], ddir[1]],
             [ddir[3],ddir[5],ddir[6], ddir[3]],
             [ddir[2],ddir[6],ddir[7], ddir[2]],
             [ddir[0],ddir[4],ddir[5], ddir[0]]]
    N_ITER = 10
    elf_index = 0
    for _ in range(0, N_ITER):
        seen_proposed = defaultdict(int)
        for pos, elf in grid.items():
            if isinstance(elf, Elf):
                has_neighbour = False
                for dd in ddir:
                    new_pos = (pos[0]+dd[0],pos[1]+dd[1])
                    if new_pos in grid:
                        if isinstance(grid[new_pos], Elf):
                            has_neighbour = True
                            break
                if not has_neighbour:
                    continue
                for i in range(0, 4):
                    step = steps[(i+elf_index)%4]
                    is_valid = True
                    for dd in step[:-1]:
                        new_pos = (pos[0]+dd[0], pos[1]+dd[1])
                        if new_pos in grid:
                            if isinstance(grid[new_pos], Elf):
                                is_valid = False
                                break
                    if is_valid:
                        proposed_pos = (pos[0] + step[-1][0], pos[1] + step[-1][1])
                        seen_proposed[proposed_pos] += 1
                        elf.proposed = proposed_pos
                        break
        new_grid = copy.deepcopy(grid)
        for pos, elf in grid.items():
            if isinstance(elf, Elf):
                proposed_pos = elf.proposed
                if proposed_pos == None or seen_proposed[proposed_pos] != 1:
                    new_grid[pos] = Elf()
                else:
                    new_grid[proposed_pos] = Elf()
                    new_grid[pos] = "."
        grid = new_grid
        elf_index += 1

    min_x = min([pos_elf[0][0] for pos_elf in grid.items() if isinstance(pos_elf[1], Elf)])
    max_x = max([pos_elf[0][0] for pos_elf in grid.items() if isinstance(pos_elf[1], Elf)])
    min_y = min([pos_elf[0][1] for pos_elf in grid.items() if isinstance(pos_elf[1], Elf)])
    max_y = max([pos_elf[0][1] for pos_elf in grid.items() if isinstance(pos_elf[1], Elf)])
    res = 0
    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x+1):
            p = (i,j)
            if p not in grid or grid[p] == ".":
                res += 1
    return res

def part2(grid):
    ddir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
    steps = [[ddir[1],ddir[4],ddir[7], ddir[1]],
             [ddir[3],ddir[5],ddir[6], ddir[3]],
             [ddir[2],ddir[6],ddir[7], ddir[2]],
             [ddir[0],ddir[4],ddir[5], ddir[0]]]
    it = 0
    elf_index = 0
    while True:
        it += 1
        seen_proposed = defaultdict(int)
        for pos, elf in grid.items():
            if isinstance(elf, Elf):
                has_neighbour = False
                for dd in ddir:
                    new_pos = (pos[0]+dd[0],pos[1]+dd[1])
                    if new_pos in grid:
                        if isinstance(grid[new_pos], Elf):
                            has_neighbour = True
                            break
                if not has_neighbour:
                    continue
                for i in range(0, 4):
                    step = steps[(i+elf_index)%4]
                    is_valid = True
                    for dd in step[:-1]:
                        new_pos = (pos[0]+dd[0], pos[1]+dd[1])
                        if new_pos in grid:
                            if isinstance(grid[new_pos], Elf):
                                is_valid = False
                                break
                    if is_valid:
                        proposed_pos = (pos[0] + step[-1][0], pos[1] + step[-1][1])
                        seen_proposed[proposed_pos] += 1
                        elf.proposed = proposed_pos
                        break
        new_grid = copy.deepcopy(grid)
        move = False
        for pos, elf in grid.items():
            if isinstance(elf, Elf):
                proposed_pos = elf.proposed
                if proposed_pos == None or seen_proposed[proposed_pos] != 1:
                    new_grid[pos] = Elf()
                else:
                    new_grid[proposed_pos] = Elf()
                    new_grid[pos] = "."
                    move = True
        if(move == False):
            return it
        grid = new_grid
        elf_index += 1

def main():
    grid = read_input()
    print(part1(grid))
    print(part2(grid))

if __name__ == "__main__":
    main()
