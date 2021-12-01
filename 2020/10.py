def read_input():
    input_lst = []
    with open("input/input10.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def part_1(input_lst):
    input_lst += [0, max(input_lst)+3]
    input_lst  = sorted(input_lst)
    diff_one   = 0
    diff_three = 0
    for i in range(1, len(input_lst)):
        diff = input_lst[i] - input_lst[i-1]
        if diff == 1:
            diff_one += 1
        elif diff == 3:
            diff_three += 1
    return diff_one*diff_three

def part_2(input_lst):
    input_lst += [0, max(input_lst)+3]
    input_lst  = sorted(input_lst)
    dp = [0]*len(input_lst)
    dp[0] = 1
    for i in range(1, len(dp)):
        for j in range(1, 4):
            if i-j < 0:
                continue
            if input_lst[i] - input_lst[i-j] <= 3:
                dp[i] += dp[i-j]
    return dp[-1]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()

