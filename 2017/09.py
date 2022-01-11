def read_input():
    with open("input/input9.txt") as input_file:
        for line in input_file:
            input_lst = [i for i in line.rstrip()]
    return input_lst

def part_1(input_lst):
    i          = 0
    n          = len(input_lst)
    group_d    = 0
    in_garbage = False
    res        = 0
    while i < n:
        c = input_lst[i]
        if c == "{":
            if in_garbage == False:
                group_d += 1
        elif c == "}":
            if in_garbage == False:
                res += group_d
                group_d -= 1
        elif c == "!":
            i += 1
        elif c == "<":
            in_garbage = True
        elif c == ">":
            in_garbage = False
        i += 1
    return res

def part_2(input_lst):
    i          = 0
    n          = len(input_lst)
    in_garbage = False
    res        = 0
    while i < n:
        c = input_lst[i]
        if c not in ["!", "<", ">"]:
            if in_garbage:
                res += 1
        elif c == "!":
            i += 1
        elif c == "<":
            if in_garbage:
                res += 1
            in_garbage = True
        elif c == ">":
            in_garbage = False
        i += 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
