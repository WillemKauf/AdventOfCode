def read_input():
    input_lst = []
    with open("input/input1.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            num  = int(line[1:])
            mul  = 1 if line[0] == "+" else -1
            input_lst.append(mul*num)
    return input_lst

def part_1(input_lst):
    return sum(input_lst)

def part_2(input_lst):
    seen = set()
    res  = 0
    while True:
        for n in input_lst:
            res += n
            if res in seen:
                return res
            seen.add(res)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
