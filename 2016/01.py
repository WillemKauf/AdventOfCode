def read_input():
    with open("input/input1.txt") as input_file:
        for line in input_file:
            input_lst = [i for i in line.rstrip().split(", ")]
    return input_lst

def part_1(input_lst):
    pos    = complex(0,0)
    direc  = complex(0,1)
    for line in input_lst:
        ddir   = line[0]
        mag    = int(line[1:])
        direc *= complex(0, -1)*(ddir == "R") + complex(0, 1)*(ddir == "L")
        pos   += mag*direc
    return int(abs(pos.real) + abs(pos.imag))

def part_2(input_lst):
    pos   = complex(0,0)
    direc = complex(0,1)
    seen  = set()
    for line in input_lst:
        ddir   = line[0]
        mag    = int(line[1:])
        direc *= complex(0, -1)*(ddir == "R") + complex(0, 1)*(ddir == "L")
        for i in range(0, mag):
            pos += direc
            if pos in seen:
                return int(abs(pos.real) + abs(pos.imag))
            seen.add(pos)
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
