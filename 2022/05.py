import math, re
def read_input():
    input_arr = []
    instruct_arr = []
    p2 = False
    with open("input/input5.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            if line == "":
                p2 = True
                continue
            if not p2:
                curr_char = ""
                curr_stack = []
                for i, c in enumerate(line):
                    if c == "[":
                        n = math.floor((len(curr_char)+1)//4)
                        if n == 0:
                            curr_stack.append([])
                            continue
                        for i in range(0, n+1):
                            curr_stack.append([])
                    elif c == "]":
                        curr_char = ""
                        continue
                    elif c.isalpha():
                        curr_stack[-1].append(c)
                    curr_char += c
                for i, c in enumerate(curr_stack):
                    if len(input_arr)-1 <= i:
                        input_arr.append([])
                    input_arr[i].append(c)
            else:
                a,b,c = re.findall(r'\d+', line)
                instruct_arr.append([int(a),int(b),int(c)])
    for i, s in enumerate(input_arr):
        input_arr[i] = [c for j in s for c in j]

    return input_arr, instruct_arr

def part1(input_arr, instruct_arr):
    for instruct in instruct_arr:
        n, a, b = instruct
        for i in range(0, n):
            if len(input_arr[a-1]) == 0:
                continue
            c = input_arr[a-1].pop(0)
            input_arr[b-1].insert(0, c)
    s = ""
    for stack in input_arr:
        if len(stack) == 0:
            continue
        s += stack[0]
    return s

def part2(input_arr, instruct_arr):
    for instruct in instruct_arr:
        n, a, b = instruct
        curr_move = []
        for i in range(0, n):
            if len(input_arr[a-1]) == 0:
                continue
            c = input_arr[a-1].pop(0)
            curr_move.append(c)
        for c in curr_move[::-1]:
            input_arr[b-1].insert(0, c)
    s = ""
    for stack in input_arr:
        if len(stack) == 0:
            continue
        s += stack[0]
    return s


def main():
    print(part1(*read_input()))
    print(part2(*read_input()))

if __name__ == "__main__":
    main()
