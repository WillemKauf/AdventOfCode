from collections import defaultdict
import heapq

def read_input(part_2=False):
    hsh_map  = defaultdict(list)
    molecule = None
    with open("input/input19.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            if line == "":
                molecule = input_file.readline().rstrip()
                break
            line = line.split(" => ")
            if part_2:
                hsh_map[line[1]].append(line[0])
            else:
                hsh_map[line[0]].append(line[1])
    return molecule, hsh_map

def part_1(molecule, hsh_map):
    j = 0
    strings = {"":0}
    while j < len(molecule):
        new_strings = {}
        if molecule[j] in hsh_map:
            mol_base = molecule[j]
            for k, v in strings.items():
                new_strings[k+mol_base] = v
            for k, v in strings.items():
                for replace in hsh_map[mol_base]:
                    new_strings[k+replace] = v+1
            j += 1
        elif molecule[j]+molecule[j+1] in hsh_map:
            mol_base = molecule[j]+molecule[j+1]
            for k, v in strings.items():
                new_strings[k+mol_base] = v
            for k, v in strings.items():
                for replace in hsh_map[mol_base]:
                    new_strings[k+replace] = v+1
            j += 2
        else:
            if molecule[j+1].islower():
                mol_base = molecule[j]+molecule[j+1]
            else:
                mol_base = molecule[j]
            for k, v in strings.items():
                new_strings[k+mol_base] = v
            j += len(mol_base)
        strings = {k:v for k,v in new_strings.items() if v < 2}
    return len(set([k for k,v in strings.items() if v == 1]))

def part_2(molecule, hsh_map):
    queue = []
    seen_states = {}
    desired_molecule = "e"
    heapq.heappush(queue, (len(molecule), 0, molecule))
    min_steps = int(1e12)
    while len(queue):
        _, num_steps, mol = heapq.heappop(queue)
        if mol == desired_molecule:
            min_steps = min(min_steps, num_steps)
            continue
        for i in range(0, len(mol)):
            rep_str = ""
            for j in range(i, min(i+11, len(mol))):
                rep_str += mol[j]
                if rep_str in hsh_map:
                    n_skip = len(rep_str)
                    for rep in hsh_map[rep_str]:
                        new_mol = mol[:i] + rep + mol[i+n_skip:]
                        new_steps = num_steps + 1
                        if new_steps >= min_steps:
                            continue
                        if new_mol in seen_states:
                            if seen_states[new_mol] <= new_steps:
                                continue
                        seen_states[new_mol] = new_steps
                        heapq.heappush(queue, (len(new_mol), new_steps, new_mol))
    return min_steps

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input(True)))

if __name__ == "__main__":
    main()
