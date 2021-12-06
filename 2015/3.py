def read_input():
    input_arr = []
    with open("input/input3.txt") as input_file:
        for line in input_file.readlines():
            input_arr = [c for c in line.rstrip()]
    return input_arr

def part_1(input_arr):
    pos          = [0,0]
    seen         = set((0,0))
    direc        = {"v":(0,-1),"^":(0,1),">":(1,0),"<":(-1,0)}
    num_presents = 1
    for c in input_arr:
        d_pos = direc[c]
        pos[0] += d_pos[0]
        pos[1] += d_pos[1]
        pos_tup = (pos[0], pos[1])
        if pos_tup not in seen:
            num_presents += 1
            seen.add(pos_tup)
    return num_presents

def part_2(input_arr):
    pos          = [0,0]
    r_pos        = [0,0]
    seen         = set([(0,0)])
    direc        = {"v":(0,-1),"^":(0,1),">":(1,0),"<":(-1,0)}
    num_presents = 1
    for i, c in enumerate(input_arr):
        d_pos = direc[c]
        if(i % 2 == 0):
            pos[0] += d_pos[0]
            pos[1] += d_pos[1]
            pos_tup = (pos[0], pos[1])
        else:
            r_pos[0] += d_pos[0]
            r_pos[1] += d_pos[1]
            pos_tup = (r_pos[0], r_pos[1])
        if pos_tup not in seen:
            num_presents += 1
            seen.add(pos_tup)
    return num_presents

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

main()
