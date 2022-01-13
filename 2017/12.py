def read_input():
    input_dct = {}
    with open("input/input12.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(" <-> ")
            lst = line[1].split(", ")
            node = int(line[0])
            input_dct[node] = [int(i) for i in line[1].split(", ")]
    return input_dct

def part_1(input_dct):
    seen = set()
    def recursive_search(n):
        for c in input_dct[n]:
            if c in seen:
                continue
            seen.add(c)
            recursive_search(c)

    recursive_search(0)
    return len(seen)

def part_2(input_dct):
    sets = {}
    def recursive_search(n, seen):
        if n in sets:
            return None
        if n in seen:
            return seen
        seen.add(n)
        for c in input_dct[n]:
            new_seen = recursive_search(c, seen)
        return new_seen

    cnt = 1
    for n in input_dct:
        seen = recursive_search(n, set())
        if seen == None:
            continue
        for c in seen:
            sets[c] = cnt
        cnt += 1
    return max(sets.values())

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
