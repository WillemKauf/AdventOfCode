def read_input():
    input_lst = []
    with open("input/input6.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split()]
    return input_lst

def part_1(input_lst):
    seen      = set()
    num_steps = 0
    n         = len(input_lst)
    while True:
        tup_lst = tuple(input_lst)
        if tup_lst in seen:
            return num_steps
        seen.add(tup_lst)
        max_num   = max(input_lst)
        max_index = input_lst.index(max_num)
        input_lst[max_index] = 0
        for i in range(1, max_num+1):
            input_lst[(max_index+i)%n] += 1
        num_steps += 1
    return num_steps

def part_2(input_lst):
    seen      = {}
    num_steps = 0
    n         = len(input_lst)
    while True:
        tup_lst = tuple(input_lst)
        if tup_lst in seen:
            return num_steps - seen[tup_lst]
        seen[tup_lst] = num_steps
        max_num   = max(input_lst)
        max_index = input_lst.index(max_num)
        input_lst[max_index] = 0
        for i in range(1, max_num+1):
            input_lst[(max_index+i)%n] += 1
        num_steps += 1

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
