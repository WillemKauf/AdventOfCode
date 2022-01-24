from collections import deque

ddir = [(0,-1),(-1,0),(1,0),(0,1)]

class Unit():
    def __init__(self, pos, typ, atk=3):
        self.pos   = pos
        self.atk   = atk
        self.hp    = 200
        self.type  = typ
        self.dead  = False
        self.moved = False

    def __str__(self):
        return f"{self.type}, {self.pos}, {self.hp}, {self.dead}, {self.moved}"

class Graph:
    def __init__(self, input_lst, atk=3):
        self.nodes        = {}
        self.elves        = []
        self.goblins      = []
        self.elves_killed = 0
        self.parse_graph(input_lst, atk)

    def parse_graph(self, input_lst, atk):
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                c = input_lst[j][i]
                if c != "#":
                    pos = (i,j)
                    self.nodes[pos] = c
                    if c == "E":
                        self.elves.append(Unit(pos, "E", atk))
                    elif c == "G":
                        self.goblins.append(Unit(pos, "G"))

    def bfs(self, start, target):
        queue      = deque([(0, start, tuple())])
        seen       = set([start])
        poss_paths = []
        min_steps  = int(1e12)
        while len(queue):
            num_steps, pos, path = queue.popleft()
            if num_steps > min_steps:
                continue
            if self.nodes[pos] == target:
                if num_steps < min_steps:
                    poss_paths = [(path[1:], num_steps-1)]
                    min_steps  = num_steps
                elif num_steps == min_steps:
                    poss_paths.append((path[1:], num_steps-1))
                continue
            for dd in ddir:
                new_pos = pos[0] + dd[0], pos[1] + dd[1]
                if new_pos in self.nodes and new_pos not in seen:
                    new_c = self.nodes[new_pos]
                    flag_as_seen = True
                    for dd in ddir:
                        ext_pos = new_pos[0]+dd[0], new_pos[1]+dd[1]
                        if ext_pos in self.nodes:
                            if self.nodes[ext_pos] == target:
                                flag_as_seen = False
                    if new_c != target and flag_as_seen == True:
                        seen.add(new_pos)
                    if new_c in [".", target]:
                        queue.append((num_steps+1, new_pos, path+tuple([pos])))
        return poss_paths if len(poss_paths) else [[tuple(), -1]]

    def vis(self):
        max_x = max(self.nodes, key=lambda k:k[0])[0]+2
        max_y = max(self.nodes, key=lambda k:k[1])[1]+2
        lst   = [["#" for j in range(0, max_x)] for i in range(0, max_y)]
        for pos,c in self.nodes.items():
            lst[pos[1]][pos[0]] = c
        for l in lst:
            print("".join(l))
        print()

    def run_round(self, it):
        for e in self.elves:
            e.moved = False
        for g in self.goblins:
            g.moved = False

        def get_targets():
            it_sum = 1
            units = sorted(self.elves + self.goblins, key=lambda u: (u.pos[1], u.pos[0]))
            for i, a in enumerate(units):
                a.moved = True
                if a.dead:
                    continue
                curr_pos = a.pos
                target   = "E" if a.type == "G" else "G"
                pathfind = True
                for dd in ddir:
                    new_pos = curr_pos[0] + dd[0], curr_pos[1] + dd[1]
                    if new_pos in self.nodes:
                        if self.nodes[new_pos] == target:
                            pathfind = False
                if pathfind:
                    poss_paths_and_steps = self.bfs(curr_pos, target)
                    if poss_paths_and_steps[0][1] not in [-1, 0]:
                        new_path, new_steps = min(poss_paths_and_steps, key=lambda pps: (pps[0][-1][1], pps[0][-1][0], pps[0][0][1], pps[0][0][0]))
                        new_pos             = new_path[0]
                        self.nodes[a.pos]   = "."
                        self.nodes[new_pos] = a.type
                        a.pos               = new_pos

                poss_targets = set()
                g_b = self.elves if a.type == "G" else self.goblins
                for b in g_b:
                    if b.dead:
                        continue
                    dpos = (b.pos[0] - a.pos[0], b.pos[1] - a.pos[1])
                    if dpos in ddir:
                        poss_targets.add(b)
                if poss_targets:
                    best_target = min(poss_targets, key=lambda u: (u.hp, u.pos[1], u.pos[0]))
                    best_target.hp -= a.atk
                    if best_target.hp <= 0:
                        best_target.dead = True
                        if a.type == "G":
                            self.elves_killed += 1
                        self.nodes[best_target.pos] = "."
                        if all([g.dead for g in g_b]) and any([u.moved == False for u in units if u.dead == False]):
                            it_sum = 0
            return it_sum
        it_sum       = get_targets()
        self.elves   = [e for e in self.elves if not e.dead]
        self.goblins = [g for g in self.goblins if not g.dead]
        return it_sum

    def simulate(self, p2=False):
        it = 0
        while True:
            it += self.run_round(it)
            if p2:
                if self.elves_killed:
                    return -1
            if not len(self.elves):
                return it*sum([g.hp for g in self.goblins])
            if not len(self.goblins):
                return it*sum([e.hp for e in self.elves])

def read_input():
    input_lst = []
    with open("input/input15.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    graph = Graph(input_lst)
    return graph.simulate()

def part_2(input_lst):
    atk = 4
    while True:
        graph = Graph(input_lst, atk)
        res   = graph.simulate(True)
        if graph.elves_killed == 0:
            return res
        atk += 1

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
