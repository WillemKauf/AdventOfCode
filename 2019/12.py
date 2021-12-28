import numpy as np

def read_input():
    input_dct = {}
    with open("input/input12.txt") as input_file:
        for i, line in enumerate(input_file):
            line = line.rstrip()[1:-1]
            line = line.split(", ")
            curr_lst = []
            for l in line:
                c = int(l.split("=")[1])
                curr_lst.append(c)
            input_dct[i] = curr_lst
    return input_dct

def part_1(pos_dct):
    vel_dct = {i:[0,0,0] for i in range(0, len(pos_dct))}
    n_dims  = 3
    for _ in range(0, 1000):
        for planet in pos_dct:
            for planet2 in pos_dct:
                if planet == planet2:
                    continue
                for i in range(0, n_dims):
                    c_pos  = pos_dct[planet][i]
                    c_pos2 = pos_dct[planet2][i]
                    if c_pos > c_pos2:
                        vel_dct[planet][i] -= 1
                    elif c_pos < c_pos2:
                        vel_dct[planet][i] += 1
        for planet in pos_dct:
            for i in range(0, n_dims):
                pos_dct[planet][i] += vel_dct[planet][i]
    res = 0
    for planet in pos_dct:
        Ep = sum([abs(i) for i in pos_dct[planet]])
        Ek = sum([abs(i) for i in vel_dct[planet]])
        res += Ep*Ek
    return res

def part_2(pos_dct):
    vel_dct = {i:[0,0,0] for i in range(0, len(pos_dct))}
    n_dims  = 3
    seen    = {i:set() for i in range(0, len(pos_dct))}
    lcd     = [None for i in range(0, n_dims)]
    it      = 0
    while True:
        for i in range(0, n_dims):
            if lcd[i] != None:
                continue
            c_rep = tuple([p[i] for p in pos_dct.values()])+tuple([v[i] for v in vel_dct.values()])
            if c_rep in seen[i]:
                lcd[i] = it
            seen[i].add(c_rep)
        if all([i != None for i in lcd]):
            return np.lcm.reduce(lcd)
        for planet in pos_dct:
            for planet2 in pos_dct:
                if planet == planet2:
                    continue
                for i in range(0, n_dims):
                    c_pos  = pos_dct[planet][i]
                    c_pos2 = pos_dct[planet2][i]
                    if c_pos > c_pos2:
                        vel_dct[planet][i] -= 1
                    elif c_pos < c_pos2:
                        vel_dct[planet][i] += 1
        for planet in pos_dct:
            for i in range(0, n_dims):
                pos_dct[planet][i] += vel_dct[planet][i]
        it += 1

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
