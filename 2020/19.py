from copy import deepcopy

def read_input():
    rules_dct   = {}
    message_lst = []
    with open("input/input19.txt") as input_file:
        line = input_file.readline()
        while line:
            line = line.rstrip()
            if line == "":
                break
            line = line.split()
            rule_num = int(line[0].split(":")[0])
            rules = line[1:]
            if rules[0][0] == '"':
                rules = rules[0].replace('"', '')
            rules_dct[rule_num] = rules
            line = input_file.readline()
        line = input_file.readline()
        while line:
            line = line.rstrip()
            message_lst.append(line)
            line = input_file.readline()
    return message_lst, rules_dct

def part_1(message_lst, rules_dct):
    def recursive_solve(string, rule_num):
        rules = rules_dct[int(rule_num)]
        if isinstance(rules, str):
            if string[0] == rules:
                return 1
            else:
                return None
        else:
            if "|" in rules:
                or_index = rules.index("|")
                for or_rules in [rules[:or_index], rules[or_index+1:]]:
                    ind = 0
                    for rule in or_rules:
                        n_ind = recursive_solve(string[ind:], rule)
                        if n_ind == None:
                            ind = None
                            break
                        ind += n_ind
                    if ind != None:
                        return ind
            else:
                ind = 0
                for rule in rules:
                    n_ind = recursive_solve(string[ind:], rule)
                    if n_ind == None:
                        ind = None
                        break
                    ind += n_ind
                if ind != None:
                    return ind
        return None

    return sum([recursive_solve(message, 0) == len(message) for message in message_lst])

def part_2(message_lst, rules_dct):
    rules_dct[8]  = ["42", "|", "42", "8"]
    rules_dct[11] = ["42", "31", "|", "42", "11", "31"]
    def recursive_solve(string, rule_num):
        rules = rules_dct[int(rule_num)]
        if isinstance(rules, str):
            if string[0] == rules:
                return 1
            else:
                return None
        else:
            if "|" in rules:
                or_index = rules.index("|")
                for or_rules in [rules[:or_index], rules[or_index+1:]]:
                    ind = 0
                    for rule in or_rules:
                        n_ind = recursive_solve(string[ind:], rule)
                        if n_ind == None:
                            ind = None
                            break
                        ind += n_ind
                    if ind != None:
                        return ind
            else:
                ind = 0
                for rule in rules:
                    n_ind = recursive_solve(string[ind:], rule)
                    if n_ind == None:
                        ind = None
                        break
                    ind += n_ind
                if ind != None:
                    return ind
        return None

    return sum([recursive_solve(message, 0) == len(message) for message in message_lst])

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
