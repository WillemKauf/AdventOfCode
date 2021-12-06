def read_input():
    input_lst = []
    with open("input/input6.txt") as input_file:
        curr_group = []
        for line in input_file:
            line = line.rstrip()
            if line == "":
                input_lst.append(curr_group)
                curr_group = []
            else:
                curr_group.append(line)
        if len(curr_group):
            input_lst.append(curr_group)
    return input_lst

def part_1(input_lst):
    res = 0
    for lst in input_lst:
        seen = set()
        for s in lst:
            for c in s:
                seen.add(c)
        res += len(seen)
    return res

def part_2(input_lst):
    res = 0
    for lst in input_lst:
        seen = set(lst[0])
        for i in range(1, len(lst)):
            seen &= set(lst[i])
        res += len(seen)
    return res

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

