from collections import deque

def read_input():
    input_dct = {}
    with open("input/input15.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_dct[line[1]] = int(line[-1])
    return input_dct

def part_1(input_dct):
    fac_dct = {"A":16807, "B":48271}
    div_fac = 2147483647
    res     = 0
    for _ in range(0, int(4e7)):
        bin_nums = {k:0 for k in input_dct}
        for g, v in input_dct.items():
            input_dct[g] = (v*fac_dct[g]) % div_fac
            bin_nums[g]  = bin(input_dct[g])[2:].zfill(32)
        if bin_nums["A"][16:] == bin_nums["B"][16:]:
            res += 1
    return res

def part_2(input_dct):
    fac_dct = {"A":16807,     "B":48271}
    num_dct = {"A":deque([]), "B":deque([])}
    mod_dct = {"A":4,         "B":8}
    div_fac = 2147483647
    res     = 0
    pairs   = 0
    while pairs < int(5e6):
        for g, v in input_dct.items():
            new_num = (v*fac_dct[g]) % div_fac
            input_dct[g] = new_num
            if new_num % mod_dct[g] == 0:
                bin_num = bin(new_num)[2:].zfill(32)
                num_dct[g].append(bin_num)
        if len(num_dct["A"]) and len(num_dct["B"]):
            pairs += 1
            bin_A = num_dct["A"].popleft()
            bin_B = num_dct["B"].popleft()
            if bin_A[16:] == bin_B[16:]:
                res += 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
