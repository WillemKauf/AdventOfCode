def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            line = line.split()
            input_lst.append([line[0], int(line[1])])
    return input_lst

def part_1(input_lst):
    cmds = {"forward":0, "down":1, "up":-1}
    return sum([val for direc, val in input_lst if direc == "forward"])*sum(map(lambda x: cmds[x[0]]*x[1], input_lst))

def part_2(input_lst):
    aim = 0
    x   = sum([val for direc, val in input_lst if direc == "forward"])
    y   = 0
    for direc, val in input_lst:
        if direc == "forward":
            y += aim*val
        elif direc == "down":
            aim += val
        elif direc == "up":
            aim -= val
    return y*x

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

