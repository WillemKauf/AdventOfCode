import re
class Ticket:
    def __init__(self, dct):
        for k, v in dct.items():
            setattr(self, k, v)

def read_input():
    regex = r"(\w+?\s?\w+): (\d+)-(\d+) or (\d+)-(\d+)"
    curr_line = None
    attr_dct = {}
    ticket_lst = []
    nearby_ticket_lsts = []
    with open("input/input16.txt") as i_f:
        while True:
            curr_line = i_f.readline().rstrip()
            if curr_line == "":
                break
            res = re.match(regex, curr_line.rstrip())
            attr, val0, val1, val2, val3 = res.groups()
            attr_dct[attr] = [[int(val0), int(val1)], [int(val2), int(val3)]]
        if i_f.readline().rstrip() == "your ticket:":
            ticket_lst = [int(i) for i in i_f.readline().rstrip().split(",")]
        i_f.readline()
        if i_f.readline().rstrip() == "nearby tickets:":
            while True:
                curr_line = i_f.readline().rstrip()
                if curr_line == "":
                    break
                nearby_ticket_lsts.append([int(i) for i in curr_line.split(",")])
    return (attr_dct, ticket_lst, nearby_ticket_lsts)

def part_1(attr_dct, ticket_lst, nearby_ticket_lsts):
    ticket_cls = Ticket(attr_dct)
    sm = 0
    for j, nearby_ticket_lst in enumerate(nearby_ticket_lsts):
        for i, ticket in enumerate(nearby_ticket_lst):
            valid = False
            for attr in [a for a in dir(ticket_cls) if not a.startswith("__")]:
                lst0, lst1 = getattr(ticket_cls, attr)
                if((lst0[0] <= ticket <= lst0[1]) or (lst1[0] <= ticket <= lst1[1])):
                    valid = True
                    break
            if not valid:
                sm += ticket
                nearby_ticket_lsts[j][i] = None
    return sm

def part_2(attr_dct, ticket_lst, nearby_ticket_lsts):
    ticket_cls = Ticket(attr_dct)
    lst_attr_dct = {}
    true_lambda = lambda t, lst0, lst1 : (lst0[0] <= ticket <= lst0[1]) or (lst1[0] <= ticket <= lst1[1])
    for i in range(0, len(nearby_ticket_lsts[0])):
        for attr in [a for a in dir(ticket_cls) if not a.startswith("__")]:
            valid = True
            lst0, lst1 = getattr(ticket_cls, attr)
            for j in range(0, len(nearby_ticket_lsts)):
                ticket = nearby_ticket_lsts[j][i]
                if ticket == None:
                    continue
                if not true_lambda(ticket, lst0, lst1):
                    valid = False
                    break
            if valid == True:
                if attr not in lst_attr_dct:
                    lst_attr_dct[attr] = [i]
                else:
                    lst_attr_dct[attr].append(i)

    while True:
        for attr in lst_attr_dct:
            for attr2 in lst_attr_dct:
                if attr == attr2:
                    continue
                if len(lst_attr_dct[attr2]) == 1:
                    for ind2 in lst_attr_dct[attr2]:
                        if ind2 in lst_attr_dct[attr]:
                            lst_attr_dct[attr].remove(ind2)
        if(all([len(vals) == 1 for vals in lst_attr_dct.values()])):
            break
    mul = 1
    for attr in [a for a in lst_attr_dct if a[0:9] == "departure"]:
        mul *= ticket_lst[lst_attr_dct[attr][0]]
    return mul

def main():
    attr_dct, ticket_lst, nearby_ticket_lsts = read_input()
    print(part_1(attr_dct, ticket_lst, nearby_ticket_lsts))
    print(part_2(attr_dct, ticket_lst, nearby_ticket_lsts))

main()
