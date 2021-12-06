def read_input():
    with open("input/input10.txt") as input_file:
        for line in input_file:
            input_num = line.rstrip()
    return input_num

def part_1(input_num):
    input_list = (''.join(i + ('' if i == j else ', ')
            for i, j in zip(str(input_num), str(input_num)[1:] + str(input_num)[-1]))).split(", ")
    newNum = ""
    for nums in input_list:
        newNum += str(len(nums))+str(nums[0])
    return newNum


def part_2(input_num):
    return part_1(input_num)

def main():
    input_num = read_input()
    for i in range(0, 40):
        input_num = part_1(input_num)
    print(len(input_num))
    input_num = read_input()
    for i in range(0, 50):
        input_num = part_2(input_num)
    print(len(input_num))

main()
