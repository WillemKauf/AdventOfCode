def read_input():
    input_lst = []
    with open("input/input23.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            if len(line) == 3:
                input_lst.append([line[0], line[1][0], line[2]])
            else:
                input_lst.append(line)
    return input_lst

def part_1(input_lst, reg_dct):
    index = 0
    n = len(input_lst)
    while True:
        if index >= n:
            return reg_dct["b"]
        line = input_lst[index]
        cmd = line[0]
        reg = line[1]
        if cmd == "hlf":
            reg_dct[reg] //= 2
        elif cmd == "tpl":
            reg_dct[reg] *= 3
        elif cmd == "inc":
            reg_dct[reg] += 1
        elif cmd == "jmp":
            offset = int(line[1])
            index += offset
            continue
        elif cmd == "jie":
            if not reg_dct[reg] % 2:
                offset = int(line[2])
                index += offset
                continue
        elif cmd == "jio":
            if reg_dct[reg] == 1:
                offset = int(line[2])
                index += offset
                continue
        index += 1

def main():
    print(part_1(read_input(), {"a":0, "b":0}))
    print(part_1(read_input(), {"a":1, "b":0}))

if __name__ == "__main__":
    main()
