import re
def read_input():
    input_arr = []
    hsh = {}
    with open("input/input7.txt") as i_f:
        for line in i_f:
            line = line.rstrip()
            input_arr.append(line)
    for line in input_arr:
        comma_cnt = line.count(",")
        if comma_cnt == 0:
            if re.search(r"contain no", line):
                regex = r"(\w+\s\w+) bags contain no other bags."
                grps = re.match(regex, line).groups()
                hsh[grps[0]] = None
            else:
                regex = r"(\w+\s\w+) bags contain (\d) (\w+\s\w+)."
                grps = re.match(regex, line).groups()
                grp, int_1, str_1 = grps
                hsh[grp] = {str_1:int(int_1)}
        elif comma_cnt == 1:
            regex = r"(\w+\s\w+) bags contain (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+."
            grps = re.match(regex, line).groups()
            grp, int_1, str_1, int_2, str_2 = grps
            hsh[grp] = {str_1:int(int_1), str_2:int(int_2)}
        elif comma_cnt == 2:
            regex = r"(\w+\s\w+) bags contain (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+."
            grps = re.match(regex, line).groups()
            grp, int_1, str_1, int_2, str_2, int_3, str_3 = grps
            hsh[grp] = {str_1:int(int_1), str_2:int(int_2), str_3:int(int_3)}
        elif comma_cnt == 3:
            regex = r"(\w+\s\w+) bags contain (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+."
            grps = re.match(regex, line).groups()
            grp, int_1, str_1, int_2, str_2, int_3, str_3, int_4, str_4 = grps
            hsh[grp] = {str_1:int(int_1), str_2:int(int_2), str_3:int(int_3), str_4:int(int_4)}
        elif comma_cnt == 4:
            regex = r"(\w+\s\w+) bags contain (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+, (\d) (\w+\s\w+) \w+,  (\d) (\w+\s\w+) \w+."
            grps = re.match(regex, line).groups()
            grp, int_1, str_1, int_2, str_2, int_3, str_3, int_4, str_4, int_5, str_5 = grps
            hsh[grp] = {str_1:int(int_1), str_2:int(int_2), str_3:int(int_3), str_4:int(int_4), str_5:int(int_5)}
    return hsh

def part_1(input_hsh):
    def recursive_helper(parent, input_hsh, seen):
        if parent == "shiny gold":
            return 1
        else:
            res = 0
            children = input_hsh[parent]
            if children == None:
                return 0
            for child in children:
                if child not in seen:
                    seen.append(child)
                    res += recursive_helper(child, input_hsh, seen)
        return res

    res = 0
    for parent in input_hsh:
        if parent != "shiny gold":
            res += recursive_helper(parent, input_hsh, [])
    return res

def part_2(input_hsh):
    def recursive_helper(parent, input_hsh):
        res = 0
        children = input_hsh[parent]
        if children == None:
            return 0
        for child, num in children.items():
            res += num + num*recursive_helper(child, input_hsh)
        return res

    res = recursive_helper("shiny gold", input_hsh)
    return res

def main():
    input_hsh = read_input()
    print(part_1(input_hsh))
    print(part_2(input_hsh))

if __name__ == "__main__":
    main()

