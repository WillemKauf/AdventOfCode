from Intcode import IntCode, NICs

def read_input():
    input_lst = []
    with open("input/input23.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    n = 50
    intcode_lst = []
    for i in range(0, n):
        intcode = IntCode(input_lst)
        intcode_lst.append(intcode)
    intcodes = NICs(intcode_lst, rank_as_input=True)
    return intcodes.sync_run()

def part_2(input_lst):
    n = 50
    intcode_lst = []
    for i in range(0, n):
        intcode = IntCode(input_lst)
        intcode_lst.append(intcode)
    intcodes = NICs(intcode_lst, rank_as_input=True)
    return intcodes.sync_run(p2=True)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
