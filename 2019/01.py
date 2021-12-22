def read_input():
    input_lst = []
    with open("input/input1.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def part_1(input_lst):
    return sum([n//3-2 for n in input_lst])

def part_2(input_lst):
    res = 0
    for n in input_lst:
        n = n//3-2
        while n >= 0:
            res += n
            n = n//3-2
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
