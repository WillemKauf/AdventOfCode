def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            input_lst.append([int(i) for i in line.rstrip().split()])
    return input_lst

def part_1(input_lst):
    return sum([max(r) - min(r) for r in input_lst])

def part_2(input_lst):
    res = 0
    for r in input_lst:
        break_flag = False
        for n in r:
            if break_flag:
                break
            for n2 in r:
                if n == n2:
                    continue
                if n % n2 == 0:
                    res += n//n2
                    break_flag = True
                    break
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
