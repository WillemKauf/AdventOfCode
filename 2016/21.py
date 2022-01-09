import itertools

def read_input():
    input_lst = []
    with open("input/input21.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            if line[0] == "rotate":
                if line[1] == "based":
                    input_lst.append([line[0], line[1], line[-1]])
                else:
                    input_lst.append([line[0], line[1], int(line[2])])
            elif line[0] == "move":
                input_lst.append([line[0], int(line[2]), int(line[-1])])
            elif line[0] == "swap":
                input_lst.append([line[0], line[1], line[2], line[-1]])
            elif line[0] == "reverse":
                input_lst.append([line[0], int(line[2]), int(line[-1])])
    return input_lst

def to_string(dct):
    s = [None]*len(dct)
    for k in dct:
        s[dct[k]] = k
    return "".join(s)

def part_1(input_lst, st="abcdefgh"):
    d = {c:i for i,c in enumerate(st)}
    n = len(d)
    for cmd in input_lst:
        if cmd[0] == "rotate":
            if cmd[1] == "based":
                c     = cmd[2]
                ind   = d[c]
                n_rot = ind+1 if ind < 4 else ind+2
            else:
                mul_fac = 1 if cmd[1] == "right" else -1
                n_rot   = mul_fac*cmd[2]
            for k in d:
                d[k] = (d[k]+n_rot)%n
        elif cmd[0] == "move":
            a, b = cmd[1:]
            for k in d:
                if d[k] == a:
                    to_move = k
            for k in d:
                if d[to_move] < d[k]:
                    if d[k] <= b:
                        d[k] -= 1
                elif d[to_move] > d[k]:
                    if d[k] >= b:
                        d[k] += 1
            d[to_move] = b
        elif cmd[0] == "swap":
            if cmd[1] == "position":
                a, b = [int(i) for i in cmd[2:]]
                for k in d:
                    if d[k] == a:
                        swap_a = k
                    elif d[k] == b:
                        swap_b = k
                d[swap_a], d[swap_b] = d[swap_b], d[swap_a]
            elif cmd[1] == "letter":
                a, b = cmd[2:]
                d[a], d[b] = d[b], d[a]
        elif cmd[0] == "reverse":
            a, b = cmd[1:]
            for k in d:
                if a <= d[k] <= b:
                    d[k] = b - d[k] + a
    return to_string(d)

def part_2(input_lst):
    perms = [perm for perm in itertools.permutations("abcdefgh")]
    for perm in perms:
        st = "".join(perm)
        res = part_1(input_lst, st)
        if res == "fbgdceah":
            return st
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
