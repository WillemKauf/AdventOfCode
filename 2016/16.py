def read_input():
    input_str = []
    with open("input/input16.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str, l=272):
    curr_str = input_str
    while len(curr_str) < l:
        b = "".join([str(1 ^ int(i)) for i in curr_str[::-1]])
        curr_str += "0" + b
    check_sum = list(curr_str[:l])
    while True:
        curr_check_sum = []
        pairs = [i for i in zip(check_sum[0::2], check_sum[1::2])]
        for pair in pairs:
            if pair[0] == pair[1]:
                curr_check_sum.append("1")
            else:
                curr_check_sum.append("0")
        if len(curr_check_sum) % 2 != 0:
            return "".join(curr_check_sum)
        check_sum = curr_check_sum

def main():
    print(part_1(read_input()))
    print(part_1(read_input(), 35651584))

if __name__ == "__main__":
    main()
