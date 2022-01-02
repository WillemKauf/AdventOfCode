from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input12.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip().split()])
    return input_lst

def part_1(input_lst):
    regs = defaultdict(int)
    i = 0
    while i < len(input_lst):
        cmd = input_lst[i]
        if len(cmd) == 3:
            op, a, b = cmd
            if op == "cpy":
                if a in ["a", "b", "c", "d"]:
                    regs[b] = regs[a]
                else:
                    regs[b] = int(a)
            else:
                if a in ["a", "b", "c", "d"]:
                    v = regs[a]
                else:
                    v = int(a)
                if v != 0:
                    i += int(b)
                    continue
        else:
            op, r = cmd
            v = 1 if op == "inc" else -1
            regs[r] += v
        i += 1
    return regs["a"]

def part_2(input_lst):
    regs = defaultdict(int)
    regs["c"] = 1
    i = 0
    while i < len(input_lst):
        cmd = input_lst[i]
        if len(cmd) == 3:
            op, a, b = cmd
            if op == "cpy":
                if a in ["a", "b", "c", "d"]:
                    regs[b] = regs[a]
                else:
                    regs[b] = int(a)
            else:
                if a in ["a", "b", "c", "d"]:
                    v = regs[a]
                else:
                    v = int(a)
                if v != 0:
                    i += int(b)
                    continue
        else:
            op, r = cmd
            v = 1 if op == "inc" else -1
            regs[r] += v
        i += 1
    return regs["a"]


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
