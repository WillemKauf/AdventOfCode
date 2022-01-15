from collections import defaultdict
def read_input():
    input_dct = defaultdict(list)
    with open("input/input7.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            a = line[1]
            b = line[-3]
            if a not in input_dct:
                input_dct[a] = []
            input_dct[b].append(a)
    return input_dct

def part_1(input_dct):
    sorted_dct = sorted(input_dct.items())
    def recursive_solve(seen):
        for c, pl in sorted_dct:
            if c in seen:
                continue
            if all([p in seen for p in pl]):
                seen = recursive_solve(seen+[c])
                break
        return seen

    for c, pl in sorted_dct:
        if len(pl) == 0:
            res = recursive_solve([c])
            return "".join(res)

class Worker:
    def __init__(self, n):
        self.n = n
        self.t = None
        self.j = None

    def __str__(self):
        return f"{self.n}, {self.j}, {self.t}"

    def give_job(self, j, t):
        self.j = j
        self.t = t

    def update(self):
        if self.t == None:
            return None
        self.t -= 1
        if self.t == 0:
            self.t = None
            return self.j
        return None

def part_2(input_dct):
    t_mp       = {chr(i):60+i-ord("A")+1 for i in range(ord("A"), ord("Z")+1)}
    sorted_dct = sorted(input_dct.items())
    worker_lst = []
    for i in range(0, 5):
        worker_lst.append(Worker(i))
    seen       = set()
    comp_seen  = []
    n          = len(sorted_dct)
    num_steps  = 0
    while True:
        num_steps += 1
        for c, pl in sorted_dct:
            if c in seen:
                continue
            if all([p in comp_seen for p in pl]):
                for worker in worker_lst:
                    if worker.t == None:
                        worker.give_job(c, t_mp[c])
                        seen.add(c)
                        break
        for worker in worker_lst:
            new = worker.update()
            if new != None:
                comp_seen.append(new)
        if len(comp_seen) == n:
            return num_steps

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
