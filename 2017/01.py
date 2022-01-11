def read_input():
    input_str = []
    with open("input/input1.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    n = len(input_str)
    return sum([int(input_str[i])*(input_str[i] == input_str[(i-1)%n]) for i in range(0, len(input_str))])

def part_2(input_str):
    n = len(input_str)
    return sum([int(input_str[i])*(input_str[i] == input_str[(i+n//2)%n]) for i in range(0, len(input_str))])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
