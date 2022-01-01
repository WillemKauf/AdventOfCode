def read_input():
    input_lst = []
    with open("input/input7.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip())
    return input_lst

def part_1(input_lst):
    def check(st):
        return st[:2] == st[2:][::-1] and st[0] != st[1]
    mp = {"[":True, "]":False}
    res = 0
    for s in input_lst:
        pair_flag    = False
        bracket_flag = False
        dct          = {}
        curr_str     = ""
        for i in range(0, len(s)):
            c = s[i]
            if c in ["[", "]"]:
                dct[curr_str] = mp[c]
                curr_str = ""
            else:
                curr_str += c
        if len(curr_str):
            dct[curr_str] = True

        for st, v in dct.items():
            if pair_flag == True and v:
                continue
            if bracket_flag == True:
                break
            for i in range(0, len(st)-3):
                new_st = st[i:i+4]
                if check(new_st) and v:
                    pair_flag = True
                if check(new_st) and not v:
                    bracket_flag = True
                    break
        if pair_flag and not bracket_flag:
            res += 1
    return res

def part_2(input_lst):
    def check(st):
        return st[0] == st[2] and st[0] != st[1]
    mp = {"[":True, "]":False}
    res = 0
    for s in input_lst:
        dct          = {}
        curr_str     = ""
        for i in range(0, len(s)):
            c = s[i]
            if c in ["[", "]"]:
                dct[curr_str] = mp[c]
                curr_str = ""
            else:
                curr_str += c
        if len(curr_str):
            dct[curr_str] = True

        seen = set()
        for st, v in dct.items():
            if v:
                for i in range(0, len(st)-2):
                    new_st  = st[i:i+3]
                    if check(new_st):
                        conj_st = new_st[1]+new_st[0]+new_st[1]
                        seen.add(conj_st)

        break_flag = False
        for st, v in dct.items():
            if break_flag:
                break
            if not v:
                for i in range(0, len(st)-2):
                    new_st = st[i:i+3]
                    if new_st in seen:
                        res += 1
                        break_flag = True
                        break
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
