from collections import defaultdict
def read_input():
    input_lst = []
    with open("input/input3.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            ID   = int(line[0][1:])
            x,y  = [int(i) for i in line[2][:-1].split(",")]
            w,l  = [int(i) for i in line[3].split("x")]
            input_lst.append([ID, x,y, w,l])
    return input_lst

def part_1(input_lst):
    grid = defaultdict(list)
    for (ID, x,y, w,l) in input_lst:
        for dx in range(0, w):
            for dy in range(0, l):
                grid[(x+dx,y+dy)].append(ID)
    return len([l for l in grid.values() if len(l) > 1])

def part_2(input_lst):
    grid = defaultdict(list)
    for (ID, x,y, w,l) in input_lst:
        for dx in range(0, w):
            for dy in range(0, l):
                grid[(x+dx,y+dy)].append(ID)

    seen = set()
    for k,l in grid.items():
        if len(l) > 1:
            for p in l:
                seen.add(p)
    return (set([l[0] for l in input_lst])-seen).pop()

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
