from collections import deque

def read_input():
    input_lst = []
    with open("input/input18.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip())

    def get_bracket_index(lst, i, depth):
        bracket_index = None
        d = 0
        n = len(lst)
        for j in range(i, n):
            if lst[j] == "(":
                d += 1
            elif lst[j] == ")":
                d -= 1
            if d == 0:
                bracket_index = j
                break
        if bracket_index == None:
            raise ValueError
        return bracket_index

    def parse(lst, op_list, depth):
        i = 0
        curr_lst = deque()
        n = len(lst)
        while i < n:
            if lst[i] == "(":
                bracket_index = get_bracket_index(lst, i, depth+1)
                curr_lst.append(parse(lst[i+1:bracket_index+1], op_list, depth+1))
                i = bracket_index+1
                continue
            elif lst[i] in op_list:
                curr_lst.append(lst[i])
            i += 1
        return curr_lst

    vals = deque([parse(lst, [str(i) for i in range(0, 10)], 0) for lst in input_lst])
    opps = deque([parse(lst, ["*", "+"], 0) for lst in input_lst])
    return vals, opps

def part_1(vals_lst, opps_lst):
    def parse(vals, opps):
        while len(vals) > 1:
            a = vals.popleft()
            opp = opps.popleft()
            if isinstance(a, deque):
                new = parse(a, opp)
                vals.appendleft(new)
            else:
                b = vals.popleft()
                if isinstance(b, deque):
                    b_opp = opps.popleft()
                    new = parse(b, b_opp)
                    vals.appendleft(new)
                    vals.appendleft(a)
                    opps.appendleft(opp)
                if isinstance(b, str):
                    if opp == "+":
                        a = str(int(a)+int(b))
                    elif opp == "*":
                        a = str(int(a)*int(b))
                    vals.appendleft(a)
        return vals.popleft()

    return sum(int(parse(vals_lst[i], opps_lst[i])) for i in range(0, len(vals_lst)))

def part_2(vals_lst, opps_lst):
    def get_add_count(opps):
        res = 0
        for opp in opps:
            if isinstance(opp, deque):
                res += get_add_count(opp)
            elif opp == "+":
                res += 1
        return res

    def parse(vals, opps):
        while len(vals) > 1:
            a = vals.popleft()
            opp = opps.popleft()
            add_count = get_add_count(opps)
            if isinstance(a, deque):
                new = parse(a, opp)
                vals.appendleft(new)
            else:
                b = vals.popleft()
                if isinstance(b, deque):
                    b_opp = opps.popleft()
                    new = parse(b, b_opp)
                    vals.appendleft(new)
                    vals.appendleft(a)
                    opps.appendleft(opp)
                if isinstance(b, str):
                    if opp == "+":
                        a = str(int(a)+int(b))
                        vals.appendleft(a)
                    elif opp == "*":
                        if add_count != 0:
                            vals.append(a)
                            vals.appendleft(b)
                            opps.append(opp)
                        else:
                            a = str(int(a)*int(b))
                            vals.appendleft(a)
        return vals.popleft()

    return sum(int(parse(vals_lst[i], opps_lst[i])) for i in range(0, len(vals_lst)))

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()

