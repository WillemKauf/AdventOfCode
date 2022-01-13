def read_input():
    input_lst = []
    with open("input/input11.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(",")
            input_lst = line
    return input_lst

def part_1(input_lst):
    #hexagonal grid uses r,q,s for coordinate system
    dir_map = {"n":(-1,0,1), "s":(1,0,-1), "se":(0,1,-1), "sw":(1,-1,0), "ne":(-1,1,0), "nw":(0,-1,1)}
    r,q,s    = 0,0,0
    for d in input_lst:
        dr,dq,ds = dir_map[d]
        r += dr
        q += dq
        s += ds
    return (abs(r)+abs(q)+abs(s))//2

def part_2(input_lst):
    max_dist = -1
    dir_map  = {"n":(-1,0,1), "s":(1,0,-1), "se":(0,1,-1), "sw":(1,-1,0), "ne":(-1,1,0), "nw":(0,-1,1)}
    r,q,s    = 0,0,0
    for d in input_lst:
        dr,dq,ds = dir_map[d]
        r += dr
        q += dq
        s += ds
        curr_dist = (abs(r)+abs(q)+abs(s))//2
        max_dist  = max(max_dist, curr_dist)
    return max_dist

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

