from collections import Counter
def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip())
    return input_lst

def part_1(input_lst):
    n_twice  = 0
    n_thrice = 0
    for s in input_lst:
        cnt = Counter(s)
        if 2 in cnt.values():
            n_twice += 1
        if 3 in cnt.values():
            n_thrice += 1
    return n_twice*n_thrice

def part_2(input_lst):
    seen = set()
    for s in input_lst:
        for s2 in input_lst:
            sorted_tup = tuple(sorted([s,s2]))
            if s == s2 or sorted_tup in seen:
                continue
            seen.add(sorted_tup)
            n_diff = 0
            for p in range(0, len(s)):
                if s[p] != s2[p]:
                    n_diff += 1
            if n_diff == 1:
                common_str = ""
                for p in range(0, len(s)):
                    if s[p] == s2[p]:
                        common_str += s[p]
                return common_str
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
