def read_input():
    input_arr = []
    with open("input/input9.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append(line.split(" "))
    return input_arr

def sign(s):
    return -1 if s < 0 else 1

def mag(v):
    return abs(v[0])+abs(v[1])

def compute_new_tail(head, tail):
    dx = head[0]-tail[0]
    dy = head[1]-tail[1]
    m = mag([dx,dy])
    if dx != 0 and dy == 0: #horizontal
        if abs(dx) == 1:
            return tail
        else:
            tail[0] += sign(dx)
    elif dy != 0 and dx == 0: #vertical
        if abs(dy) == 1:
            return tail
        else:
            tail[1] += sign(dy)
    elif dx == 0 and dy == 0:
        return tail
    else: #diagonal
        m = mag([dx,dy])
        if m > 2:
            tail[0] += sign(dx)
            tail[1] += sign(dy)
        else:
            return tail

def part1(input_arr):
    head = [0,0]
    tail = [0,0]
    mp = {"L":(-1,0) , "R":(1,0) , "U":(0,1) , "D":(0,-1)}
    seen = set()
    for a, b in input_arr:
        b = int(b)
        ddir = mp[a]
        dx, dy = ddir
        for i in range(0, b):
            head[0] += dx
            head[1] += dy
            compute_new_tail(head, tail)
            seen.add((tail[0], tail[1]))
    return len(seen)

def part2(input_arr):
    head = [0,0]
    tails = [[0,0] for _ in range(0, 9)]
    mp = {"L":(-1,0) , "R":(1,0) , "U":(0,1) , "D":(0,-1)}
    seen = set()
    for a, b in input_arr:
        b = int(b)
        ddir = mp[a]
        dx, dy = ddir
        for i in range(0, b):
            head[0] += dx
            head[1] += dy
            compute_new_tail(head, tails[0])
            for i in range(0, len(tails)-1):
                compute_new_tail(tails[i], tails[i+1])
            seen.add((tails[-1][0], tails[-1][1]))
    return len(seen)

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
