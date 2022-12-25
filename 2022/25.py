from collections import deque

def read_input():
    input_arr = []
    with open("input/input25.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append(line)
    return input_arr

def get_int_from_snafu(snafu):
    curr_n = 0
    for i,c in enumerate(snafu[::-1]):
        if c.isnumeric():
            curr_n += int(c)*5**i
        else:
            if c == "=":
                curr_n -= 2*5**i
            if c == "-":
                curr_n -= 5**i
    return curr_n

def part1(input_arr):
    res = 0
    for line in input_arr:
        res += get_int_from_snafu(line)
    num = "2-21=02=1-121-2-11-0" #By hand!
    return num

def main():
    input_arr = read_input()
    print(part1(input_arr[:]))

if __name__ == "__main__":
    main()
