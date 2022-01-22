import itertools
import heapq

def read_input():
    input_lst = []
    with open("input/input22.txt") as input_file:
        input_lst.append(int(input_file.readline().rstrip().split(": ")[1]))
        input_lst.append(tuple(int(i) for i in input_file.readline().rstrip().split(": ")[1].split(",")))
    return input_lst

def part_1(input_lst):
    erosion_levels = {}
    def erosion_level(x,y, depth, target):
        if (x,y) in erosion_levels:
            return erosion_levels[(x,y)]
        geo_index = geologic_index(x,y,depth,target)
        ero_level = (geo_index+depth)%20183
        erosion_levels[(x,y)] = ero_level
        return erosion_levels[(x,y)]

    def geologic_index(x,y, depth, target):
        if (x,y) == (0,0) or (x,y) == target:
            return 0
        if y == 0:
            return x*16807
        elif x == 0:
            return y*48271
        else:
            return erosion_level(x-1,y, depth, target)*erosion_level(x,y-1, depth, target)
    depth, target = input_lst
    grid          = {}
    type_mp       = {0:"R", 1:"W", 2:"N"}
    val_mp        = {v:k for k,v in type_mp.items()}
    res           = 0
    ext           = 50
    for j in range(0, target[1]+1+ext):
        for i in range(0, target[0]+1+ext):
            ero_level   = erosion_level(i,j,depth,target)
            n_type      = ero_level % 3
            r_type      = type_mp[n_type]
            grid[(i,j)] = r_type
            if i <= target[0] and j <= target[1]:
                res += val_mp[r_type]
    return res, grid

def part_2(input_lst, grid):
    def dist(x,y):
        return abs(target[0]-x) + abs(target[1]-y)
    depth, target = input_lst
    ddir          = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    queue         = []
    cnt           = 0
    heapq.heappush(queue, (0, dist(0,0), cnt, (0,0), "T"))
    min_steps     = int(1e12)
    r_map         = {"R":["C", "T"], "W":["C", None], "N":["T", None]}
    seen          = {}
    while len(queue):
        num_steps, _, _, curr_pos, curr_item = heapq.heappop(queue)
        if num_steps > min_steps:
            continue
        if curr_pos == target:
            if curr_item != "T":
                num_steps += 7
            min_steps = min(min_steps, num_steps)
            continue
        for dd in ddir:
            new_pos = curr_pos[0] + dd[0], curr_pos[1] + dd[1]
            if new_pos in grid:
                new_region = grid[new_pos]
                if curr_item in r_map[new_region]:
                    new_rep   = (new_pos, curr_item)
                    new_steps = num_steps+1
                    if new_rep not in seen or new_steps < seen[new_rep]:
                        seen[new_rep] = new_steps
                        cnt += 1
                        heapq.heappush(queue, (new_steps, dist(*new_pos), cnt, new_pos, curr_item))
                for new_item in r_map[new_region]:
                    curr_region = grid[curr_pos]
                    if new_item in r_map[curr_region]:
                        new_rep = (new_pos, new_item)
                        new_steps = num_steps+8
                        if new_rep not in seen or new_steps < seen[new_rep]:
                            seen[new_rep] = new_steps
                            cnt += 1
                            heapq.heappush(queue, (new_steps, dist(*new_pos), cnt, new_pos, new_item))
    return min_steps

def main():
    p1, grid = part_1(read_input())
    print(p1)
    print(part_2(read_input(), grid))

if __name__ == "__main__":
    main()
