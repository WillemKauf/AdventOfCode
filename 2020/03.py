def read_input():
    input_lst = []
    with open("input/input3.txt") as input_file:
        for line in input_file:
            lst = []
            for char in line.rstrip():
                lst.append(char)
            input_lst.append(lst)
    return input_lst

def part_1(input_lst):
    x, y = [0,0]
    res = 0
    dx = 3
    dy = 1
    for i in range(1, len(input_lst)):
        row = input_lst[i]
        x = (x+dx)%len(row)
        y += dy
        if input_lst[y][x] == "#":
            res += 1
    return res

def part_2(input_lst):
    res = 1
    for (dx,dy) in zip([1,3,5,7,1], [1,1,1,1,2]):
        x, y = [0,0]
        curr_res = 0
        for i in range(1, len(input_lst)//dy):
            row = input_lst[i]
            x = (x+dx)%len(row)
            y += dy
            if input_lst[y][x] == "#":
                curr_res += 1
        res *= curr_res
    return res


def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

