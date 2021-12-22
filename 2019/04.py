def read_input():
    input_lst = []
    with open("input/input4.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split("-")]
    return input_lst

def part_1(input_lst):
    res = 0
    for n in range(input_lst[0], input_lst[1]+1):
        n         = str(n)
        mono_flag = True
        adj_flag  = False
        for j in range(0, len(n)-1):
            if n[j] == n[j+1]:
                adj_flag = True
            if n[j] > n[j+1]:
                mono_flag = False
        if mono_flag and adj_flag:
            res += 1
    return res

def part_2(input_lst):
    res = 0
    for n in range(input_lst[0], input_lst[1]+1):
        n         = str(n)
        mono_flag = list(n) == sorted(n)
        adj_flag  = False
        for d in n:
            if n.count(d) == 2:
                adj_flag = True
                break
        if mono_flag and adj_flag:
            res += 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
