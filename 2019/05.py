from Intcode import IntCode

def read_input():
    input_lst = []
    with open("input/input5.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(',')]
    return input_lst

def part_1(input_lst):
    intcode = IntCode(input_lst)
    intcode.set_input([1])
    intcode.parse_tape()
    return intcode.output[-1]

def part_2(input_lst):
    intcode = IntCode(input_lst)
    intcode.set_input([5])
    intcode.parse_tape()
    return intcode.output[-1]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
