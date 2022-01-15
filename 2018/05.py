from collections import deque

def read_input():
    input_lst = []
    with open("input/input5.txt") as input_file:
        for line in input_file:
            input_lst = deque([i for i in line.rstrip()])
    return input_lst

def collapse(lst):
    flag = True
    while flag:
        stack = deque([])
        flag  = False
        while len(lst):
            c = lst.popleft()
            if len(stack):
                if stack[-1].lower() == c.lower() and stack[-1] != c:
                    flag = True
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        lst = stack
    return lst

def part_1(input_lst):
    return len(collapse(input_lst))

def part_2(input_lst):
    min_res  = int(1e12)
    for i in range(ord("a"), ord("z")):
        c       = chr(i)
        new_lst = deque([p for p in input_lst if p.lower() != c])
        res     = len(collapse(new_lst))
        if res < min_res:
            min_res  = res
    return min_res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
