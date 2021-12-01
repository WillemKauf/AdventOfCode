def read_input():
    input_lst = []
    with open("input/input1.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rsplit()[0]))
    return input_lst

def part_1(input_lst):
    res = 0
    for i in range(1, len(input_lst)):
        if input_lst[i] > input_lst[i-1]:
            res += 1
    return res

def part_2(input_lst):
    res = 0
    for i in range(2, len(input_lst)-1):
        prev_val    = input_lst[i-2]
        curr_val    = input_lst[i+1]
        if(curr_val > prev_val):
            res += 1
    return res

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()
