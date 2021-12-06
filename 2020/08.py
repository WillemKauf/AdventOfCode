def read_input():
    input_lst = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            cmd  = line[0]
            sign = line[1][0]
            val  = int(line[1][1:])
            val = -1*val if sign == "-" else val
            input_lst.append([cmd, val])
    return input_lst

def part_1(input_lst):
    acc = 0
    pos = 0
    seen = set()
    while True:
        if pos in seen:
            return acc
        seen.add(pos)
        cmd, val = input_lst[pos]
        if cmd == "acc":
            acc += val
            pos += 1
        elif cmd == "jmp":
            pos += val
        else:
            pos += 1

def part_2(input_lst):
    def test_lst(lst):
        acc = 0
        pos = 0
        seen = set()
        while True:
            if pos in seen:
                return None
            if pos >= len(input_lst):
                return acc
            seen.add(pos)
            cmd, val = input_lst[pos]
            if cmd == "acc":
                acc += val
                pos += 1
            elif cmd == "jmp":
                pos += val
            else:
                pos += 1

    for index, (cmd, val) in enumerate(input_lst):
        if cmd == "nop":
            input_lst[index][0] = "jmp"
        elif cmd == "jmp":
            input_lst[index][0] = "nop"
        else:
            continue

        res = test_lst(input_lst)
        if(res != None):
            return res

        if cmd == "nop":
            input_lst[index][0] = "nop"
        elif cmd == "jmp":
            input_lst[index][0] = "jmp"

    return None

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

