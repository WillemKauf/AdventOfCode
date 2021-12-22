def read_input():
    input_lst = []
    with open("input/input3.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_lst.append([int(i) for i in line])
    return input_lst

def part_1(input_lst):
    res = 0
    for line in input_lst:
        a,b,c = sorted(line)
        if a + b > c:
            res += 1
    return res

def part_2(input_lst):
    res = 0
    for j in range(0, len(input_lst)-2, 3):
        for i in range(0, len(input_lst[j])):
            a,b,c = sorted([input_lst[j][i],input_lst[j+1][i],input_lst[j+2][i]])
            print(a,b,c)
            if a + b > c:
                res += 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
