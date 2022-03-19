import math
import ast

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            input_lst.append([c for c in line.rstrip()])
    return input_lst

def explode(num):
    bracket_level = 0
    for i, c in enumerate(num):
        if c == "[":
            bracket_level += 1
        elif c == "]":
            bracket_level -= 1
        if bracket_level == 5:
            next_bracket = num.index("]", i)
            a, _, b = num[i+1:next_bracket]
            for j in range(i, next_bracket+1):
                num[j] = None
            need_zero_a = False
            for j in range(i, -1, -1):
                if num[j] == None:
                    continue
                elif num[j] == "[":
                    need_zero_a = True
                elif num[j].isnumeric():
                    num[j] = str(int(num[j])+int(a))
                    break
            if need_zero_a:
                num[i] = "0"
            need_zero_b = False
            for j in range(next_bracket, len(num)):
                if num[j] == None:
                    continue
                if num[j] == "]":
                    need_zero_b = True
                elif num[j].isnumeric():
                    num[j] = str(int(num[j])+int(b))
                    break
            if need_zero_b:
                num[next_bracket] = "0"
            num = [c for c in num if c != None]
            return True, num
    return False, num

def split(num):
    for i, c in enumerate(num):
        if c.isnumeric():
            c = int(c)
            if c > 9:
                a = str(math.floor(c/2))
                b = str(math.ceil(c/2))
                num[i] = "["
                num.insert(i+1, a)
                num.insert(i+2, ",")
                num.insert(i+3, b)
                num.insert(i+4, "]")
                return True, num
    return False, num

def recursive_parse(num):
    sm = 0
    a, b = num
    if isinstance(a, int):
        sm += 3*a
    else:
        sm += 3*recursive_parse(a)
    if isinstance(b, int):
        sm += 2*b
    else:
        sm += 2*recursive_parse(b)
    return sm

def add_nums(n1, n2):
    num = ["["] + [c for c in n1] + [","] + [c for c in n2] + ["]"]
    action = True
    while action:
        action = False
        action, num = explode(num)
        if not action:
            action, num = split(num)
    return num

def part_1(input_lst):
    num = input_lst[0]
    for new_num in input_lst[1:]:
        num = add_nums(num, new_num)
    return recursive_parse(ast.literal_eval("".join(num)))

def part_2(input_lst):
    max_sum = 0
    for n1 in input_lst:
        for n2 in input_lst:
            if n1 == n2:
                continue
            n = add_nums(n1,n2)
            max_sum = max(max_sum, recursive_parse(ast.literal_eval("".join(n))))
    return max_sum

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
