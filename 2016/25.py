def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip().split())
    return input_lst

def part_1(input_lst):
    for a in range(0, 100000000000000000):
        dct    = {"a":a, "b":0, "c":0, "d":0}
        i      = 0
        output = []
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
            elif cmd[0] == "out":
                x = cmd[1]
                if x.islower():
                    v = dct[x]
                else:
                    v = x
                output.append(v)
                if len(output) == 1:
                    if v != 0:
                        break
                if len(output) > 1:
                    if output[-1] == 0:
                        if output[-2] != 1:
                            break
                    elif output[-1] == 1:
                        if output[-2] != 0:
                            break
                if len(output) > 1000:
                    return a
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

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
