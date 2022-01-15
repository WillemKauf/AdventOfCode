from collections import defaultdict
def read_input():
    input_lst = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_lst = [int(i) for i in line]
    return input_lst

def part_1(input_lst):
    def recursive_solve(i):
        sm = 0
        n_child = input_lst[i]
        n_meta  = input_lst[i+1]
        if n_child == 0:
            sm += sum(input_lst[i+2:i+2+n_meta])
            return i+n_meta+2, sm
        else:
            i += 2
            for j in range(0, n_child):
                i, new_sm = recursive_solve(i)
                sm += new_sm

        sm += sum(input_lst[i:i+n_meta])
        i  += n_meta
        return i, sm
    return recursive_solve(0)[1]

def part_2(input_lst):
    def recursive_solve(i):
        sm = 0
        n_child = input_lst[i]
        n_meta  = input_lst[i+1]
        if n_child == 0:
            sm = sum(input_lst[i+2:i+2+n_meta])
            return i+n_meta+2, sm
        else:
            child_l = defaultdict(int)
            i += 2
            for j in range(0, n_child):
                i, child_v = recursive_solve(i)
                child_l[j+1] = child_v

        metadata = input_lst[i:i+n_meta]
        for m in metadata:
            sm += child_l[m]
        i  += n_meta
        return i, sm
    return recursive_solve(0)[1]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
