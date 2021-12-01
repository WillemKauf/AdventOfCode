def read_input():
    input_lst = []
    with open("input/input1.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            input_lst.append(int(line))
    return input_lst

def part_1(input_lst):
    hsh_map = {}
    target = 2020
    for num in input_lst:
        if num in hsh_map:
            return num*hsh_map[num]
        hsh_map[target-num] = num

def part_2(input_lst):
    hsh_map = {}
    for num in input_lst:
        target = 2020-num
        for num2 in input_lst:
            if num2 in hsh_map:
                return num*num2*hsh_map[num2]
            hsh_map[target-num2] = num2

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

