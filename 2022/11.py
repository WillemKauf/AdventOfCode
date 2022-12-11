import re
from collections import deque

class Monkey():
    def __init__(self, n, items, op, test, true, false):
        self.n = n
        self.items = deque(items)
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.n_inspects = 0

def read_input():
    input_arr = []
    with open("input/input11.txt", "r") as input_file:
        curr_info = []
        for line in input_file.readlines():
            line = line.rstrip()
            if line == "":
                continue
            elif line[0] == "M":
                if len(curr_info):
                    input_arr.append(Monkey(*curr_info))
                curr_info = [int(line[-2])]
            else:
                if line[2] == "S":
                    n = re.findall(r'\d+', line)
                    curr_info.append([int(i) for i in n])
                elif line[2] == "T":
                    line = line.split(" ")
                    curr_info.append(int(line[-1]))
                else:
                    line = line.split(": ")
                    curr_info.append(line[-1])
    if len(curr_info):
        input_arr.append(Monkey(*curr_info))
    return input_arr

def process_op(old, op):
    op, v = op.split(" = ")[1][4:].split(" ")
    if v != "old":
        v = int(v)
    else:
        v = old
    if op == "*":
        return old*v
    elif op == "+":
        return old+v
    else:
        return old

def test_op(item, test, true, false):
    m_true = int(true[-1])
    m_false = int(false[-1])
    if item % test == 0:
        return m_true
    else:
        return m_false

def part1(input_arr):
    for i in range(0, 20):
        for m in input_arr:
            while len(m.items):
                item = m.items.popleft()
                item = process_op(item, m.op)
                item //= 3
                m_throw = test_op(item, m.test, m.true, m.false)
                input_arr[m_throw].items.append(item)
                m.n_inspects += 1
    input_arr = sorted(input_arr, key = lambda m : m.n_inspects, reverse=True)

    return input_arr[0].n_inspects*input_arr[1].n_inspects

def part2(input_arr):
    BIGNUM = 1
    for m in input_arr:
        BIGNUM *= m.test
    for i in range(0, 10000):
        for m in input_arr:
            while len(m.items):
                item = m.items.popleft()
                item = process_op(item, m.op)
                item %= BIGNUM
                m_throw = test_op(item, m.test, m.true, m.false)
                input_arr[m_throw].items.append(item)
                m.n_inspects += 1
    input_arr = sorted(input_arr, key = lambda m : m.n_inspects, reverse=True)

    return input_arr[0].n_inspects*input_arr[1].n_inspects

def main():
    print(part1(read_input()))
    print(part2(read_input()))

if __name__ == "__main__":
    main()
