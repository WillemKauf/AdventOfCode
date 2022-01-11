from collections import Counter

def read_input():
    input_lst = []
    with open("input/input4.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip().split()])
    return input_lst

def part_1(input_lst):
    res = 0
    for l in input_lst:
        count = Counter(l)
        if max(count.values()) == 1:
            res += 1
    return res

def part_2(input_lst):
    res = 0
    for l in range(0, len(input_lst)):
        for k in range(0, len(input_lst[l])):
            input_lst[l][k] = "".join(sorted(input_lst[l][k]))

    for l in input_lst:
        count = Counter(l)
        if max(count.values()) == 1:
            res += 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
