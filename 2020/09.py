def read_input():
    input_lst = []
    with open("input/input9.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def part_1(input_lst):
    preamble_len = 25
    for i in range(preamble_len, len(input_lst)):
        prev_nums = input_lst[i-preamble_len:i]
        target = input_lst[i]
        hsh_map = {}
        flag = False
        for num in prev_nums:
            if num in hsh_map:
                flag = True
                break
            hsh_map[target-num] = num
        if flag == False:
            return target

def part_2(input_lst):
    preamble_len = 25
    for i in range(preamble_len, len(input_lst)):
        prev_nums = input_lst[i-preamble_len:i]
        target = input_lst[i]
        hsh_map = {}
        flag = False
        for num in prev_nums:
            if num in hsh_map:
                flag = True
                break
            hsh_map[target-num] = num
        if flag == False:
            invalid_number = target
            break
    for p1 in range(0, len(input_lst)):
        p2 = p1
        curr_sum = input_lst[p1]
        while True:
            p2 += 1
            curr_sum += input_lst[p2]
            if(curr_sum == invalid_number):
                return min(input_lst[p1:p2]) + max(input_lst[p1:p2])
            elif(curr_sum > invalid_number):
                break

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

