import math

class Disc:
    def __init__(self, lst):
        self.n        = lst[0]
        self.pos_n    = lst[1]
        self.pos      = lst[2]
        self.corr_pos = lst[3]

def read_input():
    input_lst = []
    with open("input/input15.txt") as input_file:
        for line in input_file:
            line   = line.rstrip().split()
            disc_n = int(line[1][1:])
            pos_n  = int(line[3])
            pos    = int(line[-1][:-1])
            input_lst.append(Disc([disc_n, pos_n, pos, abs(pos_n-disc_n)%pos_n]))
    return input_lst

def part_1(input_lst):
    num_discs = len(input_lst)
    t         = 0
    max_seen  = 0
    dt        = 1
    while True:
        corr_seen = [d.pos_n for d in input_lst if d.pos == d.corr_pos]
        num_seen  = len(corr_seen)
        if num_seen == num_discs:
            return t

        if num_seen > max_seen:
            max_seen = num_seen
            dt       = math.lcm(*corr_seen)

        for d in input_lst:
            d.pos = (d.pos + dt) % d.pos_n

        t += dt
    return None

def part_2(input_lst):
    new_disc_n     = len(input_lst)+1
    new_disc_pos_n = 11
    input_lst.append(Disc([new_disc_n, new_disc_pos_n, 0, abs(new_disc_pos_n-new_disc_n)%new_disc_pos_n]))
    return part_1(input_lst)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
