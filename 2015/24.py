from collections import defaultdict
import itertools

def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def part_1(input_lst):
    min_QE  = int(1e12)
    min_len = int(1e12)
    goal    = sum(input_lst)//3
    for i in range(0, len(input_lst)):
        group_one_combs = [comb for comb in itertools.combinations(input_lst, i) if sum(comb) == goal]
        for group_one in group_one_combs:
            if len(group_one) > min_len:
                return min_QE
            new_lst = list(input_lst)
            for num in group_one:
                new_lst.remove(num)
            for j in range(0, len(new_lst)):
                group_two_combs = [comb for comb in itertools.combinations(new_lst, j) if sum(comb) == goal]
                for group_two in group_two_combs:
                    new_lst_two = list(new_lst)
                    for num in group_two:
                        new_lst_two.remove(num)
                    group_three = list(new_lst_two)
                    if sum(group_three) == goal:
                        prod = 1
                        for num in group_one:
                            prod *= num
                        if prod < min_QE:
                            min_QE = prod
                            return min_QE
                            min_len = len(group_one)
    return None

def part_2(input_lst):
    min_QE  = int(1e12)
    min_len = int(1e12)
    goal    = sum(input_lst)//4
    for i in range(0, len(input_lst)):
        group_one_combs = [comb for comb in itertools.combinations(input_lst, i) if sum(comb) == goal]
        for group_one in group_one_combs:
            if len(group_one) > min_len:
                return min_QE
            new_lst = list(input_lst)
            for num in group_one:
                new_lst.remove(num)
            for j in range(0, len(new_lst)):
                group_two_combs = [comb for comb in itertools.combinations(new_lst, j) if sum(comb) == goal]
                for group_two in group_two_combs:
                    new_lst_two = list(new_lst)
                    for num in group_two:
                        new_lst_two.remove(num)
                    for k in range(0, len(new_lst_two)):
                        group_three_combs = [comb for comb in itertools.combinations(new_lst_two, k) if sum(comb) == goal]
                        for group_three in group_three_combs:
                            new_lst_three = list(new_lst_two)
                            for num in group_three:
                                new_lst_three.remove(num)
                            group_four = list(new_lst_three)
                            if sum(group_four) == goal:
                                prod = 1
                                for num in group_one:
                                    prod *= num
                                if prod < min_QE:
                                    min_QE = prod
                                    min_len = len(group_one)
                                    return min_QE
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
