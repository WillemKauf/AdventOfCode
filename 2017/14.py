from collections import deque
import itertools
knot_hsh = __import__("10").knot_hsh

def read_input():
    input_str = []
    with open("input/input14.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    res = 0
    for j in range(0, 128):
        hsh_str = input_str + "-" + str(j)
        ord_lst = [ord(str(i)) for i in hsh_str] + [17,31,73,47,23]
        hsh_str = knot_hsh(ord_lst)
        bin_str = []
        for h in hsh_str:
            bin_str += bin(int(h, 16))[2:].zfill(4)
        res += list(bin_str).count("1")
    return res

def part_2(input_str):
    grid = [[0 for i in range(0, 128)] for j in range(0, 128)]
    for j in range(0, 128):
        hsh_str = input_str + "-" + str(j)
        ord_lst = [ord(str(i)) for i in hsh_str] + [17,31,73,47,23]
        hsh_str = knot_hsh(ord_lst)
        bin_str = []
        for h in hsh_str:
            bin_str += bin(int(h, 16))[2:].zfill(4)
        for i in range(0, len(bin_str)):
            grid[j][i] = int(bin_str[i])
    res  = 0
    seen = set()
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]

    for j in range(0, 128):
        for i in range(0, 128):
            if (i,j) in seen:
                continue
            c = grid[j][i]
            if c == 0:
                continue
            queue = deque([(i,j)])
            res += 1
            while len(queue):
                curr_pos = queue.popleft()
                seen.add(curr_pos)
                for dd in ddir:
                    new_pos = (curr_pos[0] + dd[0], curr_pos[1] + dd[1])
                    if 0 <= new_pos[0] < 128 and 0 <= new_pos[1] < 128:
                        if new_pos not in seen and grid[new_pos[1]][new_pos[0]] == 1:
                            queue.append((new_pos))
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
