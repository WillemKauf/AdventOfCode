from collections import defaultdict
import heapq
from copy import deepcopy
import itertools
import random

def read_input():
    state_dct = defaultdict(list)
    floor_map = {"first":1, "second":2, "third":3, "fourth":4}
    num_chips = 0
    num_gens  = 0
    with open("input/input11.txt") as input_file:
        for line in input_file:
            line  = line.rstrip().split()
            floor = floor_map[line[1]]
            line  = line[3:]
            for i,st in enumerate(line):
                if st[:9] == "microchip":
                    chip = line[i-1].split("-")[0][:2].upper()+"M"
                    state_dct[floor].append(chip)
                    num_chips += 1
                elif st[:9] == "generator":
                    gen = line[i-1].split("-")[0][:2].upper()+"G"
                    state_dct[floor].append(gen)
                    num_gens += 1
    assert num_chips == num_gens
    return state_dct, num_chips

def m_to_g(m):
    return m[:2]+"G"

def g_to_m(g):
    return g[:2]+"M"

def check_valid_state(state, poss_inv, old_floor, new_floor):
    new_state = deepcopy(state)
    if old_floor < new_floor and all([len(state[i]) == 0 for i in range(new_floor, 0, -1)]):
        return False
    for inv in poss_inv:
        new_state[old_floor].remove(inv)
        new_state[new_floor].append(inv)
    for floor in range(old_floor, new_floor+1):
        floor_inv = new_state[floor]
        chips = [m for m in floor_inv if m[-1] == "M"]
        for chip in chips:
            if m_to_g(chip) not in floor_inv and len(chips) > 1:
                return False
    return new_state

def val_state(state):
    val = 0
    for floor, lst in state.items():
        for i in lst:
            val += floor
    return val

def hsh_state(state):
    hsh = ""
    for floor, lst in state.items():
        hsh += str(floor)
        for i in sorted(lst):
            hsh += i
    return hsh

def part_1(initial_state, num_chips):
    queue = []
    seen = set()
    heapq.heappush(queue, (-val_state(initial_state), 0, hsh_state(initial_state), 1, random.uniform(0,1), deepcopy(initial_state)))
    while len(queue):
        _, num_steps, _, floor, _, state = heapq.heappop(queue)
        seen.add(hsh_state(state))
        if len(state[4]) == num_chips*2:
            return num_steps
        floor_inv            = state[floor]
        one_item_moves       = [comb for comb in itertools.combinations(floor_inv, 1)]
        two_item_moves       = [comb for comb in itertools.combinations(floor_inv, 2)]
        for dd in [1, -1]:
            new_floor = floor+dd
            if 1 <= new_floor <= 4:
                for poss_move in one_item_moves+two_item_moves:
                    new_state = check_valid_state(state, poss_move, floor, new_floor)
                    if new_state != False:
                        hsh_new_state = hsh_state(new_state)
                        if hsh_new_state not in seen:
                            heapq.heappush(queue,((-val_state(new_state), num_steps+1, hsh_new_state, new_floor, random.uniform(0,1), new_state)))
    return None

def part_2(initial_state, num_chips):
    initial_state[1] += ["ELG", "ELM", "DIG", "DIM"]
    num_chips += 2
    queue = []
    seen = set()
    heapq.heappush(queue, (-val_state(initial_state), 0, hsh_state(initial_state), 1, random.uniform(0,1), deepcopy(initial_state)))
    while len(queue):
        _, num_steps, _, floor, _, state = heapq.heappop(queue)
        seen.add(hsh_state(state))
        if len(state[4]) == num_chips*2:
            return num_steps
        floor_inv            = state[floor]
        one_item_moves       = [comb for comb in itertools.combinations(floor_inv, 1)]
        two_item_moves       = [comb for comb in itertools.combinations(floor_inv, 2)]
        for dd in [1, -1]:
            new_floor = floor+dd
            if 1 <= new_floor <= 4:
                for poss_move in one_item_moves+two_item_moves:
                    new_state = check_valid_state(state, poss_move, floor, new_floor)
                    if new_state != False:
                        hsh_new_state = hsh_state(new_state)
                        if hsh_new_state not in seen:
                            heapq.heappush(queue,((-val_state(new_state), num_steps+1, hsh_new_state, new_floor, random.uniform(0,1), new_state)))

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
