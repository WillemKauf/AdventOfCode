from collections import defaultdict
def read_input():
    input_arr = []
    with open("input/input6.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr = line
    return input_arr

def part1(input_arr):
    n = 4
    window = []
    for i, c in enumerate(input_arr):
        window.append(c)
        if len(window) > n:
            window.pop(0)
        if len(window) == len(set(window)) == n:
            return i+1

def part2(input_arr):
    n = 14
    window = []
    for i, c in enumerate(input_arr):
        window.append(c)
        if len(window) > n:
            window.pop(0)
        if len(window) == len(set(window)) == n:
            return i+1

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(read_input()))

if __name__ == "__main__":
    main()
