import itertools

def read_input():
    input_lst = []
    with open("input/input14.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            val = line[2]
            if line[0][:3] == "mem":
                addr = (line[0][3:])[1:-1]
            else:
                addr = line[0]
            input_lst.append([addr, val])
    return input_lst

def part_1(input_lst):
    mask = None
    mem = {}
    for addr, val in input_lst:
        if addr == "mask":
            mask = val
            continue
        bin_val = "{0:b}".format(int(val))
        bin_val = str(bin_val).zfill(36)
        for i, c in enumerate(mask):
            if c in ["0", "1"]:
                bin_val = bin_val[:i] + c + bin_val[i+1:]
        dec_val = int(bin_val, 2)
        mem[addr] = dec_val
    return sum(i for i in mem.values())

def part_2(input_lst):
    mask = None
    mem = {}
    for addr, val in input_lst:
        if addr == "mask":
            mask = val
            continue
        bin_addr = "{0:b}".format(int(addr))
        bin_addr = str(bin_addr).zfill(36)
        for i, c in enumerate(mask):
            if c in ["1", "X"]:
                bin_addr = bin_addr[:i] + c + bin_addr[i+1:]
        combs = itertools.product(["0", "1"], repeat=mask.count("X"))
        for comb in combs:
            comb_ind = 0
            curr_addr = bin_addr
            for i, c in enumerate(mask):
                if c == "X":
                    curr_addr = curr_addr[:i] + comb[comb_ind] + curr_addr[i+1:]
                    comb_ind += 1
            dec_addr = int(curr_addr, 2)
            mem[dec_addr] = int(val)
    return sum(i for i in mem.values())

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

