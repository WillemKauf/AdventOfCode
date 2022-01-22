import itertools

def read_input():
    input_lst = []
    with open("input/input19.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line[:-1]])
    return input_lst

def part_1(input_lst):
    ddir      = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    pos       = None
    direc     = (0,1)
    seen      = []
    len_x     = len(input_lst[0])
    len_y     = len(input_lst)
    num_steps = 0
    for i in range(0, len(input_lst[0])):
        if input_lst[0][i] == "|":
            pos = (i,0)
    assert pos != None
    while True:
        x, y = pos
        c    = input_lst[y][x]
        if c.isupper():
            seen.append(c)
        if c == "+":
            prev_pos = (pos[0] - direc[0], pos[1] - direc[1])
            for dd in ddir:
                new_pos = (pos[0] + dd[0], pos[1] + dd[1])
                if new_pos == prev_pos:
                    continue
                new_x, new_y = new_pos
                if 0 <= new_x < len_x and 0 <= new_y < len_y:
                    if input_lst[new_y][new_x] not in ["", " "]:
                        direc = (new_pos[0] - pos[0], -(pos[1] - new_pos[1]))

        new_pos      = (pos[0] + int(direc[0]), pos[1] + int(direc[1]))
        new_x, new_y = new_pos
        num_steps += 1
        if input_lst[new_y][new_x] in ["", " "]:
            return "".join(seen), num_steps
        pos = new_pos
    return None

def main():
    code, steps = part_1(read_input())
    print(code)
    print(steps)

if __name__ == "__main__":
    main()
