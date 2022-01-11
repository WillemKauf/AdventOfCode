import math

def read_input():
    with open("input/input3.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num

def part_1(input_num):
    #This is old code. It's terrible. But it works.
    for sector_index in range(1, 1000, 2):
        origin_num = sector_index**2
        if origin_num > input_num:
            sector_index -= 2
            origin_num = sector_index**2 + 1
            break
    dx = (sector_index - 1)//2 + 1
    dy = -(sector_index - 1)//2
    for j in range(0, sector_index):
        if origin_num == input_num:
            return dx + dy
        origin_num += 1
        dy += 1
    for i in range(0, sector_index+1):
        if origin_num == input_num:
            return dx + dy
        origin_num += 1
        if i <= sector_index //2:
            dx -= 1
        else:
            dx += 1
    for j in range(0, sector_index+1):
        if origin_num == input_num:
            return dx + dy
        origin_num += 1
        dy -= 1
    for i in range(0, sector_index+1):
        if origin_num == input_num:
            return dx + dy
        origin_num += 1
        if i <= sector_index//2:
            dx += 1
        else:
            dx -= 1
    return -1

def part_2(input_num):

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
