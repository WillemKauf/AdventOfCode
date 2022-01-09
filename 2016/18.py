def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        mp = {"^":1, ".":0}
        for line in input_file:
            line = line.rstrip()
            for c in line:
                input_lst.append(mp[c])
    return input_lst

def part_1(trap_lst, n_iter=40):
    res = trap_lst.count(0)
    n   = len(trap_lst)
    for _ in range(0, n_iter-1):
        new_trap_lst = []
        for i in range(0, n):
            if i == 0:
                seg = [0]+trap_lst[i:i+2]
            elif i == n-1:
                seg = trap_lst[i-1:i+1]+[0]
            else:
                seg = trap_lst[i-1:i+2]
            sm   = sum(seg)
            l_sm = sum(seg[:2])
            r_sm = sum(seg[1:])
            if (sm == l_sm == 2) or (sm == r_sm == 2) or (l_sm == 1 and r_sm == 0) or (l_sm == 0 and r_sm == 1):
                new_trap_lst.append(1)
            else:
                new_trap_lst.append(0)
                res += 1
        trap_lst = new_trap_lst
    return res

def main():
    print(part_1(read_input()))
    print(part_1(read_input(), 400000))

if __name__ == "__main__":
    main()
