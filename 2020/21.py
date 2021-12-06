def read_input():
    input_lst = []
    hsh_map   = {}
    with open("input/input21.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(" (contains ")
            ingrs = line[0].split(" ")
            alle = line[1].split(", ")
            alle[-1] = alle[-1][:-1]
            for a in alle:
                if a not in hsh_map:
                    hsh_map[a] = [ingrs]
                else:
                    hsh_map[a].append(ingrs)
            input_lst.append([ingrs, alle])
    return input_lst, hsh_map

def part_1(input_lst, hsh_map):
    all_ingrs = set()
    for alle, ingrs_lst in hsh_map.items():
        ingr_set = []
        for ingr_lst in ingrs_lst:
            for ingr in ingr_lst:
                all_ingrs.add(ingr)
            if not len(ingr_set):
                ingr_set = set(ingr_lst)
            else:
                ingr_set &= set(ingr_lst)
        hsh_map[alle] = list(ingr_set)

    no_alle_lst = list(all_ingrs)
    for ingr_lst in hsh_map.values():
        for ingr in ingr_lst:
            if ingr in no_alle_lst:
                no_alle_lst.remove(ingr)

    res = 0
    for ingr_lst, alle in input_lst:
        for ingr in no_alle_lst:
            res += ingr_lst.count(ingr)
    return res

def part_2(input_lst, hsh_map):
    all_ingrs = set()
    for alle, ingrs_lst in hsh_map.items():
        ingr_set = []
        for ingr_lst in ingrs_lst:
            for ingr in ingr_lst:
                all_ingrs.add(ingr)
            if not len(ingr_set):
                ingr_set = set(ingr_lst)
            else:
                ingr_set &= set(ingr_lst)
        hsh_map[alle] = list(ingr_set)

    def recursive_delete(alle, hsh_map):
        ingr_lst = hsh_map[alle]
        assert(len(ingr_lst) == 1)
        ingr = ingr_lst[0]
        for alle2, ingr2_lst in hsh_map.items():
            if alle == alle2:
                continue
            if ingr in ingr2_lst:
                ingr2_lst.remove(ingr)
                if len(ingr2_lst) == 1:
                    hsh_map = recursive_delete(alle2, hsh_map)
        return hsh_map

    for alle, ingr_lst in hsh_map.items():
        if len(ingr_lst) == 1:
            hsh_map = recursive_delete(alle, hsh_map)

    return "".join([v[0]+"," for _, v in sorted(hsh_map.items())])[:-1]

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()

