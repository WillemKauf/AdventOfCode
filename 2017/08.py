from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(" if ")
            cmd  = line[0].split()
            a    = cmd[0]
            op   = cmd[1]
            v    = int(cmd[2])
            cond = line[1].split()
            b    = cond[0]
            op2  = cond[1]
            v2   = int(cond[2])
            input_lst.append([a, op, v, b, op2, v2])
    return input_lst

def part_1(input_lst):
    regs = defaultdict(int)
    for l in input_lst:
        a, op, v, b, op2, v2 = l
        flag = False
        if op2 == ">":
            if regs[b] > v2:
                flag = True
        elif op2 == ">=":
            if regs[b] >= v2:
                flag = True
        elif op2 == "<":
            if regs[b] < v2:
                flag = True
        elif op2 == "<=":
            if regs[b] <= v2:
                flag = True
        elif op2 == "==":
            if regs[b] == v2:
                flag = True
        elif op2 == "!=":
            if regs[b] != v2:
                flag = True
        if flag:
            if op == "inc":
                regs[a] += v
            elif op == "dec":
                regs[a] -= v

    return max(regs.values())

def part_2(input_lst):
    regs = defaultdict(int)
    max_val = -1
    for l in input_lst:
        a, op, v, b, op2, v2 = l
        flag = False
        if op2 == ">":
            if regs[b] > v2:
                flag = True
        elif op2 == ">=":
            if regs[b] >= v2:
                flag = True
        elif op2 == "<":
            if regs[b] < v2:
                flag = True
        elif op2 == "<=":
            if regs[b] <= v2:
                flag = True
        elif op2 == "==":
            if regs[b] == v2:
                flag = True
        elif op2 == "!=":
            if regs[b] != v2:
                flag = True
        if flag:
            if op == "inc":
                regs[a] += v
            elif op == "dec":
                regs[a] -= v
        max_val = max(max_val, max(regs.values()))
    return max_val

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
