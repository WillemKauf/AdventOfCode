def read_input():
    input_lst = []
    with open("input/input3.txt") as input_file:
        for line in input_file:
            input_lst.append([(l[0], int(l[1:])) for l in line.rstrip().split(",")])
    return input_lst

def part_1(input_lst):
    paths = []
    dir_map = {"R":1, "U":1, "L":-1, "D":-1}
    for wire_path in input_lst:
        seen = set()
        pos = (0,0)
        for d, v in wire_path:
            dx = v*dir_map[d]*(d in ["L", "R"])
            dy = v*dir_map[d]*(d in ["U", "D"])
            new_pos = (pos[0]+dx, pos[1]+dy)
            for i in range(1, abs(dx)+1):
                seen.add((pos[0]+dir_map[d]*i, pos[1]))
            for i in range(1, abs(dy)+1):
                seen.add((pos[0], pos[1]+dir_map[d]*i))
            pos = new_pos
        paths.append(seen)
    ints  = list(paths[0] & paths[1])
    c_int = sorted(ints, key=lambda p: abs(p[0])+abs(p[1]))[0]
    return abs(c_int[0])+abs(c_int[1])

def part_2(input_lst):
    paths = []
    dir_map = {"R":1, "U":1, "L":-1, "D":-1}
    for wire_path in input_lst:
        seen = {}
        pos = (0,0)
        steps = 0
        for (d, v) in wire_path:
            dx = v*dir_map[d]*(d in ["L", "R"])
            dy = v*dir_map[d]*(d in ["U", "D"])
            new_pos = (pos[0]+dx, pos[1]+dy)
            for i in range(1, abs(dx)+1):
                seen[(pos[0]+dir_map[d]*i, pos[1])] = steps+i
            for i in range(1, abs(dy)+1):
                seen[(pos[0], pos[1]+dir_map[d]*i)] = steps+i
            pos = new_pos
            steps += v
        paths.append(seen)
    ints = paths[0].keys() & paths[1].keys()
    return min([paths[0][v] + paths[1][v] for v in ints])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
