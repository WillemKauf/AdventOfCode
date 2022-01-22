from collections import defaultdict
from itertools import chain

def read_input():
    input_lst   = []
    with open("input/input19.txt") as input_file:
        reg_a = int(input_file.readline().rstrip().split(" ")[1])
        for line in input_file:
            input_lst.append([i for i in line.rstrip().split()])
    return reg_a, input_lst

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

def part_1(reg_a, input_lst):
    opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    opcode_dct = {opcode.__name__:opcode for opcode in opcodes}
    regs    = [0]*6
    ip      = 0
    while ip < len(input_lst):
        cmd, a, b, c = input_lst[ip]
        regs[reg_a]  = ip
        regs         = opcode_dct[cmd](int(a), int(b), int(c), regs)
        ip           = regs[reg_a]+1
    return regs[0]

def part_2(reg_a, input_lst):
    n   = 10551350
    res = 0
    for i in range(1, n+1):
        if n % i == 0:
            res += i
    return res

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
