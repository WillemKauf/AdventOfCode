import itertools

def read_input():
    input_arr = []
    with open("input/input17.txt", "r") as input_file:
        for line in input_file:
            input_arr.append(int(line.rstrip()))
    return input_arr

def part_1(input_arr):
    input_arr    = [20, 15, 10, 5, 5]
    total_amount = 25
    dp = [1] + [0]*total_amount
    for num in input_arr:
        for target in range(total_amount, num-1, -1):
            diff = target-num
            dp[target] += dp[diff]
    return dp[total_amount]

def part_2(input_arr):
    total_amount = 150
    num_combs    = 0
    min_res      = 999999
    for i in range(1, len(input_arr)): #For loops starts from 4 because text file clearly needs more than 3 bottles
        for comb in list(itertools.combinations(input_arr, i)):
            if sum(comb) == total_amount:
                if i <= min_res:
                    min_res    = i
                    num_combs += 1
    return num_combs

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
