from collections import namedtuple, defaultdict

def read_input():
    input_lst = []
    Nanobot = namedtuple("Nanobot", ["n", "pos", "r"])
    with open("input/input23.txt") as input_file:
        for n, line in enumerate(input_file):
            line = line.rstrip().split(", ")
            pos = [int(i) for i in line[0].split("=")[1][1:-1].split(",")]
            r   = int(line[1].split("=")[1])
            input_lst.append(Nanobot(n, pos, r))
    return input_lst

def dist(pos1, pos2):
    return abs(pos2[0]-pos1[0])+abs(pos2[1]-pos1[1])+abs(pos2[2]-pos1[2])

def part_1(input_lst):
    res     = 0
    max_bot = max(input_lst, key=lambda n:n.r)
    for nanobot in input_lst:
        d = dist(max_bot.pos, nanobot.pos)
        if d <= max_bot.r:
            res += 1
    return res

def part_2(input_lst):
    def parse_neighbours():
        neighbours = defaultdict(set)
        for nanobot in input_lst:
            for nanobot2 in input_lst:
                if nanobot.n == nanobot2.n:
                    continue
                d = dist(nanobot.pos, nanobot2.pos)
                if d <= nanobot.r + nanobot2.r:
                    neighbours[nanobot.n].add(nanobot2.n)
        return neighbours
    def bron_kerbosch(R, P, X, max_len=0, max_surf=0):
        max_R = []
        if not any([P,X]):
            curr_len = len(R)
            if curr_len > max_len:
                max_len   = curr_len
                max_R     = R
                distances = [dist(n.pos, (0,0,0)) - n.r for n in max_R]
                max_surf  = max(max_surf, max(distances))
                return None, None, max_surf
        for n in P:
            new_R                    = R + [n]
            new_P                    = [new_n for new_n in P if new_n.n in neighbours[n.n]]
            new_X                    = [new_n for new_n in X if new_n.n in neighbours[n.n]]
            new_R, new_len, new_surf = bron_kerbosch(new_R, new_P, new_X, max_len, max_surf)
            if new_R == new_len == None:
                return None, None, max(new_surf, max_surf)
            if new_len > max_len:
                max_R   = new_R
                max_len = new_len
            P.remove(n)
            X.append(n)
        return max_R, max_len, max_surf

    neighbours = parse_neighbours()
    return bron_kerbosch([], input_lst, [])[2]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
