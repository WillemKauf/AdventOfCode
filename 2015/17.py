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
    combs        = defaultdict(int)
    seen         = set()
    def dfs(sm, ln, seq_arr, pick_arr):
        combs = defaultdict(int)
        for ind, i in enumerate(pick_arr):
            c = input_arr[i]
            new_sm  = sm + c
            new_ln  = ln + 1
            new_seq_arr = tuple(sorted(seq_arr + tuple([i])))
            if new_seq_arr in seen:
                continue
            seen.add(new_seq_arr)
            if new_sm > total_amount:
                continue
            elif new_sm < total_amount:
                new_pick_arr = pick_arr[:ind] + pick_arr[ind+1:]
                for l, v in dfs(new_sm, new_ln, new_seq_arr, new_pick_arr).items():
                    combs[l] += v
            else:
                combs[new_ln] += 1
        return combs

    min_n = int(1e12)
    max_v = 0
    for i, c in enumerate(input_arr):
        for n, v in dfs(c, 1, tuple([i]), [j for j in range(i)] + [j for j in range(i+1, n)]).items():
            combs[n] += v
    return combs[min(combs.keys())]

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
