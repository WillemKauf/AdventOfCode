def read_input():
    input_lst = []
    with open("input/input5.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def part_1(input_lst):
    i = 0
    n = len(input_lst)
    num_steps = 0
    while i < n:
        j = input_lst[i]
        input_lst[i] += 1
        i += j
        num_steps += 1
    return num_steps

def part_2(input_lst):
    i = 0
    n = len(input_lst)
    num_steps = 0
    while i < n:
        j = input_lst[i]
        if input_lst[i] >= 3:
            input_lst[i] -= 1
        else:
            input_lst[i] += 1
        i += j
        num_steps += 1
    return num_steps

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
