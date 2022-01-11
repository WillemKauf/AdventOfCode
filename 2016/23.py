def read_input():
    input_lst = []
    with open("input/input23.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip().split())
    return input_lst

def part_1(input_lst, a=7):
    dct = {"a":a, "b":0, "c":0, "d":0}
    i = 0
    while i < len(input_lst):
        cmd = input_lst[i]
        if cmd == None:
            continue
        if cmd[0] == "cpy":
            x,y = cmd[1:]
            if x.islower():
                dct[y] = dct[x]
            else:
                dct[y] = int(x)
        elif cmd[0] == "dec":
            x = cmd[1]
            dct[x] -= 1
        elif cmd[0] == "tgl":
            x = cmd[1]
            if x.islower():
                v = dct[x]
            else:
                v = x
            if i+v >= len(input_lst):
                i += 1
                continue
            tgl_cmd = input_lst[i+v]
            if len(tgl_cmd) == 2:
                if tgl_cmd[0] == "inc":
                    input_lst[i+v][0] = "dec"
                else:
                    input_lst[i+v][0] = "inc"
            if len(tgl_cmd) == 3:
                if tgl_cmd[0] == "jnz":
                    input_lst[i+v][0] = "cpy"
                else:
                    input_lst[i+v][0] = "jnz"
        elif cmd[0] == "jnz":
            x,y = cmd[1:]
            if x.islower():
                v = dct[x]
            else:
                v = int(x)
            if v == 0:
                i += 1
                continue
            if y.islower():
                v = dct[y]
            else:
                v = int(y)
            i += v
            continue
        elif cmd[0] == "inc":
            x = cmd[1]
            dct[x] += 1
        i += 1
    return dct["a"]

def main():
    print(part_1(read_input()))
    print(part_1(read_input(), 12))

if __name__ == "__main__":
    main()
