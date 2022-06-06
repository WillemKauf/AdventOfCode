import itertools
from collections import defaultdict

def read_input():
    input_arr = []
    with open("input/input17.txt", "r") as input_file:
        for line in input_file:
            input_arr.append(int(line.rstrip()))
    return input_arr

def part_1(input_arr):
    total_amount = 150
    dp = [1] + [0]*total_amount
    for num in input_arr:
        for target in range(total_amount, num-1, -1):
            diff = target-num
            dp[target] += dp[diff]
    return dp[total_amount]

def part_2(input_arr):
    n            = len(input_arr)
    total_amount = 150
    combs        = defaultdict(list)
    seen         = set()
    def dfs(sm, seq_arr, pick_arr):
        combs = []
        for ind, i in enumerate(pick_arr):
            c = input_arr[i]
            new_sm  = sm + c
            new_seq_arr = tuple(sorted(seq_arr + tuple([i])))
            if new_seq_arr in seen:
                continue
            seen.add(new_seq_arr)
            if new_sm > total_amount:
                continue
            elif new_sm < total_amount:
                new_pick_arr = pick_arr[:ind] + pick_arr[ind+1:]
                for comb in dfs(new_sm, new_seq_arr, new_pick_arr):
                    combs.append(comb)
            elif new_sm == total_amount:
                combs.append(new_seq_arr)
        return combs

    for i, c in enumerate(input_arr):
        for comb in dfs(c, tuple([i]), [j for j in range(i)] + [j for j in range(i+1, n)]):
            combs[len(comb)].append(tuple([input_arr[i] for i in comb]))
    return len(combs[min(combs.keys())])

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
