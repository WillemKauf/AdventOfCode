from collections import defaultdict, deque

def read_input():
    grid = defaultdict(lambda: ".")
    with open("input/input17.txt") as input_file:
        for line in input_file:
            line  = line.rstrip().split(", ")
            a, va = [i for i in line[0].split("=")]
            b, bs = line[1].split("=")
            b1, b2 = [int(i) for i in bs.split("..")]
            if a == "x":
                i = int(va)
                for j in range(b1, b2+1):
                    grid[(i,j)] = "#"
            elif a == "y":
                j = int(va)
                for i in range(b1, b2+1):
                    grid[(i,j)] = "#"
    return grid


def part_1(grid):
    lr     = [[-1,0],[1,0]]
    source = (500,1)
    def recursive_bound(pos, dd, seen):
        seen.add(pos)
        pos = pos[0] + dd[0], pos[1] + dd[1]
        if grid[pos] == "#":
            #Yes, bounded
            return True, seen
        below = pos[0], pos[1]+1
        if grid[below] not in ["~", "#"]:
            #No, not bounded
            return False, seen | set([pos])
        else:
            #Need to continue checking until we hit a wall
            return recursive_bound(pos, dd, seen)

    seen       = deque([source])
    to_revisit = deque([])
    it = 0
    min_y = min(grid, key=lambda c:c[1])[1]
    max_y = max(grid, key=lambda c:c[1])[1]+1
    while True:
        while seen:
            curr_pos = seen.popleft()
            below    = curr_pos[0], curr_pos[1] + 1
            c_below  = grid[below]
            if c_below in ["~", "#"]:
                bounded_left, lst_left   = recursive_bound(curr_pos, lr[0], set())
                bounded_right, lst_right = recursive_bound(curr_pos, lr[1], set())
                if bounded_left and bounded_right:
                    for p in lst_left | lst_right:
                        grid[p] = "~"
                else:
                    for p in lst_left | lst_right:
                        grid[p] = "|"
                        p_below = p[0], p[1] + 1
                        if grid[p_below] == ".":
                            if p_below[1] <= max_y:
                                seen.appendleft((p_below))
                                to_revisit.appendleft((p))
            elif c_below in [".", "|"]:
                if below[1] <= max_y:
                    seen.appendleft((below))
                    grid[curr_pos] = "|"
                    to_revisit.appendleft((curr_pos))
        while to_revisit:
            curr_pos = to_revisit.popleft()
            below    = curr_pos[0], curr_pos[1] + 1
            c_below  = grid[below]
            if c_below in ["~", "#"]:
                bounded_left, lst_left   = recursive_bound(curr_pos, lr[0], set())
                bounded_right, lst_right = recursive_bound(curr_pos, lr[1], set())
                if bounded_left and bounded_right:
                    for p in lst_left | lst_right:
                        grid[p] = "~"
                else:
                    for p in lst_left | lst_right:
                        grid[p] = "|"
                        if p[1] <= max_y:
                            seen.appendleft((p))
                    break
        if not seen:
            break
    return sum([v in ["~", "|"] for k, v in grid.items() if min_y <= k[1] <= max_y]), sum([v in ["~"] for k, v in grid.items() if min_y <= k[1] <= max_y])

def main():
    p1, p2 = part_1(read_input())
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
