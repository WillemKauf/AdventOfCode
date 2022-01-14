class Particle:
    def __init__(self, ind, p, v, a):
        self.ind  = ind
        self.p    = p
        self.v    = v
        self.a    = a
        self.live = True

    def __str__(self):
        return f"{self.p}, {self.v}, {self.a}"

def read_input():
    input_lst = []
    with open("input/input20.txt") as input_file:
        for ind, line in enumerate(input_file):
            line = line.rstrip().split(", ")
            p = [int(i) for i in line[0][3:-1].split(",")]
            a = [int(i) for i in line[1][3:-1].split(",")]
            v = [int(i) for i in line[2][3:-1].split(",")]
            input_lst.append(Particle(ind, p,a,v))
    return input_lst

def part_1(input_lst):
    n_iters = 500
    for _ in range(0, n_iters):
        for p in input_lst:
            p.v = [sum(x) for x in zip(p.v, p.a)]
            p.p = [sum(x) for x in zip(p.p, p.v)]

    min_dist = int(1e12)
    min_p    = None
    for p in input_lst:
        dist = abs(p.p[0]) + abs(p.p[1]) + abs(p.p[2])
        if dist < min_dist:
            min_dist = dist
            min_p = p.ind
    return min_p

def part_2(input_lst):
    n_iters = 500
    for i in range(0, n_iters):
        seen = {}
        for p in input_lst:
            if p.live == False:
                continue
            p.v = [sum(x) for x in zip(p.v, p.a)]
            p.p = [sum(x) for x in zip(p.p, p.v)]
            tup_pos = tuple(p.p)
            if tup_pos in seen:
                p.live = False
                input_lst[seen[tup_pos]].live = False
            else:
                seen[tup_pos] = p.ind
    return sum([1 for p in input_lst if p.live == True])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
