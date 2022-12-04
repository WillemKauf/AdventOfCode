def read_input():
    input_arr = []
    with open("input/input4.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            a, b = line.split(",")
            input_arr.append([int(i) for i in a.split("-")] + [int(i) for i in b.split("-")])
    return input_arr

def part1(input_arr):
    func = lambda a,b,c,d : (a <= c and b >= d) or (c <= a and d >= b)
    return sum([func(*p) for p in input_arr])

def part2(input_arr):
    func = lambda a,b,c,d : max(a,c) <= min(b,d)
    return sum([func(*p) for p in input_arr])

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
