from collections import defaultdict
def read_input():
    input_arr = []
    with open("input/input1.txt", "r") as input_file:
        curr_arr = []
        for line in input_file.readlines():
            line = line.rstrip()
            if line == "":
                input_arr.append(curr_arr)
                curr_arr = []
            else:
                curr_arr.append(int(line))
    return input_arr

def part1(input_arr):
    res = defaultdict(int)
    for i, arr in enumerate(input_arr):
        for j in arr:
            res[i] += j
    return max(res.values())

def part2(input_arr):
    res = defaultdict(int)
    for i, arr in enumerate(input_arr):
        for j in arr:
            res[i] += j
    rres = 0
    for i in range(0, 3):
        rres += sorted(res.values(), reverse=True)[i]
    return rres

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
