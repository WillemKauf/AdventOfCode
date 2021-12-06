import itertools
import re
def read_input():
    pref_dict = {}
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
                pref_dict[person]["Me"] = 0
                pref_dict["Me"][person] = 0
            pref_dict[person][person2] = val
    return pref_dict

def solve_puzzle(pref_dict):
    unique_names = list(pref_dict.keys())
    max_val = -10000
    for perm in itertools.permutations(unique_names):
        curr_val = 0
        for i in range(0, len(perm)):
            person_c = perm[i]
            if i == 0:
                person_l = perm[-1]
            else:
                person_l = perm[i-1]
            if i == len(perm)-1:
                person_r = perm[0]
            else:
                person_r = perm[i+1]
            curr_val += pref_dict[person_c][person_l] + pref_dict[person_c][person_r]
        max_val = max(max_val, curr_val)
    return max_val

def main():
    pref_dict = read_input()
    print(solve_puzzle(pref_dict))

main()
