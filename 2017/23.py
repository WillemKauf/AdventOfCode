from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input23.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip().split())
    return input_lst

def part_1(input_lst):
    regs = defaultdict(int)
    i    = 0
    n    = len(input_lst)
    res  = 0
    while i < n:
        cmd = input_lst[i]
        op = cmd[0]
        if op == "set":
            a, b = cmd[1:]
            if b.islower():
                regs[a] = regs[b]
            else:
                regs[a] = int(b)
        elif op == "sub":
            a, b = cmd[1:]
            if b.islower():
                regs[a] -= regs[b]
            else:
                regs[a] -= int(b)
        elif op == "mul":
            res += 1
            a, b = cmd[1:]
            if b.islower():
                regs[a] *= regs[b]
            else:
                regs[a] *= int(b)
        elif op == "mod":
            a, b = cmd[1:]
            if b.islower():
                regs[a] = regs[a] % regs[b]
            else:
                regs[a] = regs[a] % int(b)
        elif op == "jnz":
            a, b = cmd[1:]
            if a.islower():
                if regs[a] != 0:
                    if b.islower():
                        i += regs[b]-1
                    else:
                        i += int(b)-1
            else:
                if int(a) != 0:
                    if b.islower():
                        i += regs[b]-1
                    else:
                        i += int(b)-1
        i += 1
    return res

def part_2(input_lst):
    h = 0
    b = 108100
    c = 125100
    for x in range(b, c+1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
