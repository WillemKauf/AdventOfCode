from collections import defaultdict, deque
import heapq
import itertools

def read_input():
    input_lst = []
    with open("input/input23.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def make_locations(j_max):
    return {"A":[(3,j) for j in range(1, j_max)],
            "B":[(5,j) for j in range(1, j_max)],
            "C":[(7,j) for j in range(1, j_max)],
            "D":[(9,j) for j in range(1, j_max)]}

def parse_graph(input_lst):
    nodes          = {}
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            c = input_lst[j][i]
            if c.isupper() or c == ".":
                nodes[(i,j-1)] = c
    return nodes

def bfs(state, pos):
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    queue = deque([(0, pos)])
    seen  = {}
    while len(queue):
        curr_steps, curr_pos = queue.popleft()
        for dd in ddir:
            new_pos = curr_pos[0] + dd[0], curr_pos[1] + dd[1]
            if new_pos in state and new_pos not in seen and new_pos != pos:
                if state[new_pos] == ".":
                    seen[new_pos] = curr_steps+1
                    queue.append((curr_steps+1, new_pos))
    return seen

def vis(state):
    j_max = max(state, key=lambda l: l[1])[1]+3
    lst = [["#" for i in range(0, 13)] for j in range(0, j_max)]
    for p, n in state.items():
        lst[p[1]+1][p[0]] = n
    for l in lst:
        print("".join(l))
    print()

def count_correct(state, locations):
    res = 0
    for n, p_lst in locations.items():
        for p in p_lst:
            if state[p] == n:
                res += 1
    return res

def serialize_state(state):
    state_str = ""
    for _, n in sorted(state.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        state_str += n
    return state_str

def part_1(input_lst):
    nodes          = parse_graph(input_lst)
    cost_mp        = {"A":1, "B":10, "C":100, "D":1000}
    stopping_spots = [i for i in range(0, 11+1) if i not in [3,5,7,9]]
    queue          = []
    cnt            = 0
    seen           = {}
    min_cost       = int(1e12)
    locations      = make_locations(3)
    heapq.heappush(queue, (0, 0, cnt, nodes))
    while len(queue):
        num_correct, cost, _, state = heapq.heappop(queue)
        num_correct *= -1
        if num_correct == 8:
            min_cost = min(min_cost, cost)
            continue
        for pos, node in state.items():
            if node.isupper():
                poss_moves        = bfs(state, pos)
                desired_locations = locations[node]
                if pos == desired_locations[1]:
                    continue
                if pos[1] == 0:
                    poss_moves = {p:v for p,v in poss_moves.items() if p[1] != 0 and p in desired_locations}
                else:
                    poss_moves = {p:v for p,v in poss_moves.items() if (p[1] == 0 and p[0] in stopping_spots) or p in desired_locations}
                if desired_locations[1] in poss_moves:
                    #make best move
                    poss_moves = {desired_locations[1]:poss_moves[desired_locations[1]]}
                if desired_locations[0] in poss_moves:
                    #make move, if desired_location[1] is currently filled by other node of same type
                    if state[desired_locations[1]] == node:
                        #make best move
                        poss_moves = {desired_locations[0]:poss_moves[desired_locations[0]]}
                    else:
                        #Something else is in the way, don't even bother.
                        poss_moves.pop(desired_locations[0])
                for move, dist in poss_moves.items():
                    new_cost = cost + cost_mp[node]*dist
                    if new_cost < min_cost:
                        new_state = dict(state)
                        new_state[move], new_state[pos] = new_state[pos], new_state[move]
                        state_rep = serialize_state(new_state)
                        if state_rep in seen:
                            if seen[state_rep] <= new_cost:
                                continue
                        seen[state_rep] = new_cost
                        cnt += 1
                        heapq.heappush(queue, (-count_correct(new_state, locations), new_cost, cnt, new_state))
    return min_cost

def part_2(input_lst):
    input_lst.insert(3, "  #D#C#B#A#  ")
    input_lst.insert(4, "  #D#B#A#C#  ")
    nodes          = parse_graph(input_lst)
    cost_mp        = {"A":1, "B":10, "C":100, "D":1000}
    stopping_spots = [i for i in range(0, 11+1) if i not in [3,5,7,9]]
    queue          = []
    cnt            = 0
    seen           = {}
    min_cost       = int(1e12)
    locations      = make_locations(5)
    heapq.heappush(queue, (0, 0, cnt, nodes))
    while len(queue):
        num_correct, cost, _, state = heapq.heappop(queue)
        num_correct *= -1
        if num_correct == 16:
            min_cost = min(min_cost, cost)
            continue
        for pos, node in state.items():
            if node.isupper():
                poss_moves        = bfs(state, pos)
                desired_locations = locations[node]
                if pos == desired_locations[3]:
                    continue
                if pos[1] == 0:
                    poss_moves = {p:v for p,v in poss_moves.items() if p[1] != 0 and p in desired_locations}
                else:
                    poss_moves = {p:v for p,v in poss_moves.items() if (p[1] == 0 and p[0] in stopping_spots) or p in desired_locations}
                if desired_locations[3] in poss_moves:
                    poss_moves = {desired_locations[3]:poss_moves[desired_locations[3]]}
                if desired_locations[2] in poss_moves:
                    if state[desired_locations[3]] == node:
                        poss_moves = {desired_locations[2]:poss_moves[desired_locations[2]]}
                    else:
                        poss_moves.pop(desired_locations[2])
                if desired_locations[1] in poss_moves:
                    if all([state[desired_locations[j]] == node for j in range(2,4)]):
                        poss_moves = {desired_locations[1]:poss_moves[desired_locations[1]]}
                    else:
                        poss_moves.pop(desired_locations[1])
                if desired_locations[0] in poss_moves:
                    if all([state[desired_locations[j]] == node for j in range(1,4)]):
                        poss_moves = {desired_locations[0]:poss_moves[desired_locations[0]]}
                    else:
                        poss_moves.pop(desired_locations[0])
                for move, dist in poss_moves.items():
                    new_cost = cost + cost_mp[node]*dist
                    if new_cost < min_cost:
                        new_state = dict(state)
                        new_state[move], new_state[pos] = new_state[pos], new_state[move]
                        state_rep = serialize_state(new_state)
                        if state_rep in seen:
                            if seen[state_rep] <= new_cost:
                                continue
                        seen[state_rep] = new_cost
                        cnt += 1
                        heapq.heappush(queue, (-count_correct(new_state, locations), new_cost, cnt, new_state))
    return min_cost

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
