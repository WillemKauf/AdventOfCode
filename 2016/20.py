def read_input():
    input_lst = []
    with open("input/input20.txt") as input_file:
        for line in input_file:
            line = [int(i) for i in line.rstrip().split("-")]
            input_lst.append(line)
    return sorted(input_lst)

def part_1(input_lst):
    min_ip = 0
    for a,b in input_lst:
        if a <= min_ip <= b:
            min_ip = b+1
    return min_ip

def part_2(input_lst):
    l_total        = 4294967295+1
    prev_a, prev_b = input_lst[0]
    l_seen         = prev_b - prev_a + 1
    for i in range(1, len(input_lst)):
        a,b = input_lst[i]
        assert a <= b
        if a <= prev_b:
            l_seen -= min(prev_b, b) - a + 1
        l_seen += b - a + 1
        prev_a, prev_b = a, max(b, prev_b)
    return l_total - l_seen

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
