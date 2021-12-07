import itertools
import re

def read_input(part_two=False):
    pref_dict = {}
    if part_two:
        pref_dict["Me"] = {}
    with open("input/input13.txt", "r") as i_f:
        regex = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)"
        for line in i_f:
            line = line.rstrip()
            person, diff, val, person2 = re.match(regex, line).groups()
            val = int(val)
            if diff == "lose":
                val *= -1
            if person not in pref_dict.keys():
                pref_dict[person] = {}
                if part_two:
                    pref_dict[person]["Me"] = 0
                    pref_dict["Me"][person] = 0
            pref_dict[person][person2] = val
    return pref_dict

def solve_puzzle(pref_dict):
    unique_names = list(pref_dict.keys())
    n = len(unique_names)
    max_val = -10000
    for perm in itertools.permutations(unique_names):
        curr_val = 0
        for i in range(0, len(perm)):
            person_c = perm[i]
            person_l = perm[(i-1)%n]
            person_r = perm[(i+1)%n]
            curr_val += pref_dict[person_c][person_l] + pref_dict[person_c][person_r]
        max_val = max(max_val, curr_val)
    return max_val

def part_1(pref_dict):
    return solve_puzzle(pref_dict)

def part_2(pref_dict):
    return solve_puzzle(pref_dict)

def main():
    print(part_1(read_input()))
    print(part_2(read_input(True)))

if __name__ == "__main__":
   main()
