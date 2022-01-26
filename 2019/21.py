from Intcode import IntCode

def read_input():
    input_lst = []
    with open("input/input21.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1(input_lst):
    intcode = IntCode(input_lst)
    grid    = []
    txt     = """
NOT C J
AND D J
NOT A T
OR T J
WALK
""".strip()+"\n"
    program = [ord(c) for c in txt]
    intcode.set_input(program)
    while intcode.status == "Running":
        output = intcode.parse_tape()
    try:
        grid = []
        curr_lst = []
        for c in output:
            if c == 10:
                if len(curr_lst):
                    grid.append(curr_lst)
                curr_lst = []
            else:
                curr_lst.append(chr(c))
        for l in grid:
            print("".join(l))
    except:
        return output[-1]

def part_2(input_lst):
    intcode = IntCode(input_lst)
    grid    = []
    txt     = """
NOT B J
NOT C T
OR T J
NOT E T
AND D J
NOT T T
OR H T
AND T J
NOT A T
OR T J
RUN
""".strip()+"\n"
    program = [ord(c) for c in txt]
    intcode.set_input(program)
    while intcode.status == "Running":
        output = intcode.parse_tape()
    try:
        grid = []
        curr_lst = []
        for c in output:
            if c == 10:
                if len(curr_lst):
                    grid.append(curr_lst)
                curr_lst = []
            else:
                curr_lst.append(chr(c))
        for l in grid:
            print("".join(l))
    except:
        return output[-1]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
