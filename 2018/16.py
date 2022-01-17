from collections import defaultdict

class Sample:
    def __init__(self, before, cmd, after):
        self.before = before
        self.cmd    = cmd
        self.after  = after

def read_input():
    sample_lst = []
    test_lst   = []
    with open("input/input16.txt") as input_file:
        curr_lst = []
        for line in input_file:
            line = line.rstrip()
            if line == "":
                if not len(curr_lst):
                    break
                sample_lst.append(Sample(*curr_lst))
                curr_lst = []
            elif line[0] == "B":
                curr_lst.append([int(i) for i in line.split(": ")[1][1:-1].split(", ")])
            elif line[0] == "A":
                curr_lst.append([int(i) for i in line.split(":  ")[1][1:-1].split(", ")])
            else:
                curr_lst.append([int(i) for i in line.split()])
        for line in input_file:
            line = line.rstrip()
            if line == "":
                continue
            test_lst.append([int(i) for i in line.split()])
    return sample_lst, test_lst

def addr(a,b,c,r):
    r[c] = r[a] + r[b]
    return r

def addi(a,b,c,r):
    r[c] = r[a] + b
    return r

def mulr(a,b,c,r):
    r[c] = r[a]*r[b]
    return r

def muli(a,b,c,r):
    r[c] = r[a]*b
    return r

def banr(a,b,c,r):
    r[c] = r[a] & r[b]
    return r

def bani(a,b,c,r):
    r[c] = r[a] & b
    return r

def borr(a,b,c,r):
    r[c] = r[a] | r[b]
    return r

def bori(a,b,c,r):
    r[c] = r[a] | b
    return r

def setr(a,b,c,r):
    r[c] = r[a]
    return r

def seti(a,b,c,r):
    r[c] = a
    return r

def gtir(a,b,c,r):
    r[c] = 1 if a > r[b] else 0
    return r

def gtri(a,b,c,r):
    r[c] = 1 if r[a] > b else 0
    return r

def gtrr(a,b,c,r):
    r[c] = 1 if r[a] > r[b] else 0
    return r

def eqir(a,b,c,r):
    r[c] = 1 if a == r[b] else 0
    return r

def eqri(a,b,c,r):
    r[c] = 1 if r[a] == b else 0
    return r

def eqrr(a,b,c,r):
    r[c] = 1 if r[a] == r[b] else 0
    return r

def part_1(sample_lst, _):
    opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    res     = 0
    for l in sample_lst:
        _,a,b,c = l.cmd
        ops = 0
        for opcode in opcodes:
            new_r = opcode(a,b,c, list(l.before))
            if new_r == l.after:
                ops += 1
                if ops >= 3:
                    res += 1
                    break
    return res

def part_2(sample_lst, test_lst):
    def recursive_solve(remove_n, dct):
        to_remove = []
        for k in dct:
            if remove_n in dct[k] and len(dct[k]) > 1:
                dct[k].remove(remove_n)
                if len(dct[k]) == 1:
                    to_remove.append(tuple(dct[k])[0])
        for n in to_remove:
            dct = recursive_solve(n, dct)
        return dct

    opcode_lst = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    seen       = defaultdict(set)
    for l in sample_lst:
        n,a,b,c = l.cmd
        ops = 0
        for opcode in opcode_lst:
            new_r = opcode(a,b,c, list(l.before))
            if new_r == l.after:
                seen[opcode].add(n)

    for k, v in seen.items():
        if len(v) == 1:
            seen = recursive_solve(tuple(v)[0], seen)
    opcode_dct = {tuple(v)[0]:k for k,v in seen.items()}

    regs = [0]*4
    for l in test_lst:
        n_op,a,b,c = l
        regs       = opcode_dct[n_op](a, b, c, regs)
    return regs[0]

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
