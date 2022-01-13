from functools import reduce
from collections import deque

def hsh(input_lst, lst=[i for i in range(0, 255+1)], i=0, ss=0):
    n = len(lst)
    for l in input_lst:
        if i+l >= n:
            l1 = n-i
            l2 = l-l1
            to_reverse = deque(lst[i:] + lst[:l2])
            to_reverse.reverse()
            to_reverse = list(to_reverse)
            lst = to_reverse[l1:] + lst[l2:i] + to_reverse[:l1]
        else:
            to_reverse = deque(lst[i:i+l])
            to_reverse.reverse()
            lst = lst[:i] + list(to_reverse) + lst[i+l:]
        i = (i+l+ss)%n
        ss += 1
    return lst, i, ss


def knot_hsh(ord_lst):
    n_iter    = 64
    n         = len(ord_lst)
    ind       = 0
    ss        = 0
    lst       = [i for i in range(0, 255+1)]
    for i in range(0, n_iter):
        lst, ind, ss = hsh(ord_lst, lst, ind, ss)
    dense_hsh = []
    for i in range(0, 256, 16):
        dense_hsh.append(reduce(lambda j, k: int(j) ^ int(k), lst[i:i+16]))
    hsh_str = ""
    for l in dense_hsh:
        hx = str(hex(l)[2:]).zfill(2)
        hsh_str += hx
    return hsh_str

def part_1():
    def read_input():
        input_lst = []
        with open("input/input10.txt") as input_file:
            for line in input_file:
                input_lst = [int(i) for i in line.rstrip().split(",")]
        return input_lst
    lst = hsh(read_input())[0]
    return lst[0]*lst[1]

def part_2():
    def read_input():
        input_lst = []
        with open("input/input10.txt") as input_file:
            for line in input_file:
                input_lst = [i for i in line.rstrip()]
        return input_lst

    input_lst = read_input()
    ord_lst   = [ord(str(i)) for i in input_lst] + [17,31,73,47,23]
    return knot_hsh(ord_lst)

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()
