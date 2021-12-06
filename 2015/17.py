def readInput():
    input_arr = []
    with open("input/input17.txt", "r") as input_file:
        for line in input_file:
            input_arr.append(int(line.rstrip()))
    return input_arr

def part_1(input_arr):
    input_arr = [20, 15, 10, 5, 5]
    total_amount = 25
    dp = [1] + [0]*total_amount
    for coin in input_arr:
        print(dp)
        for i in range(0, len(dp)):
            new_amnt = i-coin
            if(new_amnt >= 0):
                dp[i] += dp[new_amnt]
    print(dp)
    return dp[total_amount]

def main():
    input_arr = readInput()
    print(part_1(input_arr))

main()
