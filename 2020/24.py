def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            i = 0
            curr_lst = []
            while i < len(line):
                if line[i] in ["s", "n"]:
                    curr_lst.append(line[i]+line[i+1])
                    i += 2
                else:
                    curr_lst.append(line[i])
                    i += 1
            input_lst.append(curr_lst)
    return input_lst

def part_1(input_lst):
    #hexagonal grid uses r,q,s for coordinate system
    hsh_map = {}
    dir_map = {"e":(0,1,-1), "w":(0,-1,1), "se":(1,0,-1), "sw":(1,-1,0), "ne":(-1,1,0), "nw":(-1,0,1)}
    for line in input_lst:
        r,q,s = 0,0,0
        for d in line:
            dr,dq,ds = dir_map[d]
            r += dr
            q += dq
            s += ds
        if (r,q,s) not in hsh_map:
            hsh_map[(r,q,s)] = 1
        else:
            hsh_map[(r,q,s)] = int(not hsh_map[(r,q,s)])
    return sum([1 for v in hsh_map.values() if v == 1])

def part_2(input_lst):
    black_tiles = set()
    dir_map = {"e":(0,1,-1), "w":(0,-1,1), "se":(1,0,-1), "sw":(1,-1,0), "ne":(-1,1,0), "nw":(-1,0,1)}
    for line in input_lst:
        r,q,s = 0,0,0
        for d in line:
            dr,dq,ds = dir_map[d]
            r += dr
            q += dq
            s += ds
        if (r,q,s) not in black_tiles:
            black_tiles.add((r,q,s))
        else:
            black_tiles.remove((r,q,s))

    for _ in range(0, 100):
        to_check = set()
        for tile in black_tiles:
            to_check.add(tile)
            for dr, dq, ds in dir_map.values():
                neighbour_pos = (tile[0]+dr, tile[1]+dq, tile[2]+ds)
                to_check.add(neighbour_pos)

        new_black_tiles = set()
        for tile in to_check:
            sm = 0
            for dr, dq, ds in dir_map.values():
                neighbour_pos = (tile[0]+dr, tile[1]+dq, tile[2]+ds)
                if neighbour_pos in black_tiles:
                    sm += 1
            if tile in black_tiles:
                if not (sm == 0 or sm > 2):
                    new_black_tiles.add(tile)
            else:
                if sm == 2:
                    new_black_tiles.add(tile)
        black_tiles = new_black_tiles

    return len(black_tiles)

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

