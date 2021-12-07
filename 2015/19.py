from collections import defaultdict

def read_input():
    hsh_map  = defaultdict(list)
    molecule = None
    with open("input/input19.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            if line == "":
                molecule = input_file.readline().rstrip()
                break
            line = line.split(" => ")
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
    #Over my head
    lst = []
    j = 0
    while j < len(molecule):
        if molecule[j].isupper():
            if j != len(molecule)-1 and molecule[j+1].islower():
                lst.append(molecule[j]+molecule[j+1])
                j += 2
            else:
                lst.append(molecule[j])
                j += 1
    num_elements = len(lst)
    num_Rn       = lst.count("Rn")
    num_Ar       = lst.count("Ar")
    num_Y        = lst.count("Y")
    return num_elements - num_Rn - num_Ar - 2*num_Y -1

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
