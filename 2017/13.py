def read_input():
    input_dct = {}
    with open("input/input13.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(": ")
            input_dct[int(line[0])] = int(line[1])
    return input_dct

def part_1(input_dct):
    state     = {k:0 for k in input_dct}
    dd        = {k:1 for k in input_dct}
    pos       = -1
    res       = 0
    max_range = max(state)
    for i in range(0, max_range+1):
        pos += 1
        if pos in state:
            if state[pos] == 0:
                res += pos*input_dct[pos]
        for k in state:
            state[k] = state[k]+dd[k]
            if state[k] == input_dct[k]-1 or state[k] == 0:
                dd[k] *= -1
    return res

def part_2(input_dct):
    t_0 = 0
    period_dct = {r:2*(input_dct[r]-1) for r in input_dct}
    while True:
        break_flag = True
        for r,d in input_dct.items():
            t = r + t_0
            p = period_dct[r]
            if t % p == 0:
                t_0 += 1
                break_flag = False
        if break_flag:
            return t_0

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
