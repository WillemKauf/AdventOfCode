from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input6.txt") as input_file:
        for line in input_file:
            input_lst.append([c for c in line.rstrip()])
    return input_lst

def part_1(input_lst):
    res = ""
    for i in range(0, len(input_lst[0])):
        dct = defaultdict(int)
        for j in range(0, len(input_lst)):
            dct[input_lst[j][i]] += 1
        res += sorted(dct.items(), key = lambda item: -item[1])[0][0]
    return res

def part_2(input_lst):
    res = ""
    for i in range(0, len(input_lst[0])):
        dct = defaultdict(int)
        for j in range(0, len(input_lst)):
            dct[input_lst[j][i]] += 1
        res += sorted(dct.items(), key = lambda item: item[1])[0][0]
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
