import functools
import ast

def read_input():
    input_arr = []
    with open("input/input13.txt", "r") as input_file:
        curr_arr = []
        for line in input_file.readlines():
            line = line.rstrip()
            if line == "":
                input_arr.append(curr_arr)
                curr_arr = []
            else:
                curr_arr.append(ast.literal_eval(line))
    if len(curr_arr):
        input_arr.append(curr_arr)
    return input_arr

def compareLists(l1, l2):
    p1 = 0
    p2 = 0
    n1 = len(l1)
    n2 = len(l2)
    while p1 < len(l1) and p2 < len(l2):
        res = compare(l1[p1], l2[p2])
        if res == 0:
            p1 += 1
            p2 += 1
        else:
            if res == -1:
                return False
            break
    return p2 < n2

def compare(v1, v2):
    if isinstance(v1, int) and isinstance(v2, int):
        if v2 == v1:
            return 0
        elif v2 > v1:
            return 1
        else:
            return -1
    elif isinstance(v1, list) and isinstance(v2, int):
        return compare(v1, [v2])
    elif isinstance(v1, int) and isinstance(v2, list):
        return compare([v1], v2)
    elif isinstance(v1, list) and isinstance(v2, list):
        p1 = 0
        p2 = 0
        n1 = len(v1)
        n2 = len(v2)
        while p1 < n1 and p2 < n2:
            res = compare(v1[p1], v2[p2])
            if res == 0:
                p1 += 1
                p2 += 1
            else:
                return res
        if p1 >= n1 and p2 < n2:
            return 1
        elif p1 < n1 and p2 >= n2:
            return -1
        else:
            return 0

def part1(input_arr):
    sm = 0
    for i, (l1, l2) in enumerate(input_arr, 1):
        if compareLists(l1, l2):
            sm += i
    return sm

def part2(input_arr):
    input_arr = [l1 for l1, _ in input_arr] + [l2 for _, l2 in input_arr]
    div_packet_one = [[2]]
    div_packet_two = [[6]]
    input_arr.append(div_packet_one)
    input_arr.append(div_packet_two)
    input_arr.sort(key = functools.cmp_to_key(compare), reverse=True)
    return (input_arr.index(div_packet_one)+1)*(input_arr.index(div_packet_two)+1)

def main():
    input_arr = read_input()
    print(part1(input_arr[:]))
    print(part2(input_arr[:]))

if __name__ == "__main__":
    main()
