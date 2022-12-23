from collections import defaultdict

def read_input(p2=False):
    key = 811589153
    input_arr  = []
    counter = defaultdict(int)
    with open("input/input20.txt", "r") as input_file:
        for i, line in enumerate(input_file.readlines()):
            line = line.rstrip()
            num  = line
            if p2:
                num = str(int(num)*key)
            num_str = num + "_" + str(counter[num])
            counter[num] += 1
            input_arr.append(num_str)
    return input_arr

def part1(input_arr):
    mixed_arr = input_arr[:]
    n = len(mixed_arr)
    for num_str in input_arr:
        index = mixed_arr.index(num_str)
        num = int(num_str.split("_")[0])
        if num == 0:
            continue
        mixed_arr.pop(index)
        if num > 0:
            mixed_arr.insert((index+num)%(n-1), num_str)
        elif num < 0:
            mixed_arr.insert((index+num)%(n-1), num_str)
    index_0 = mixed_arr.index("0_0")
    indices = [1000, 2000, 3000]
    res = 0
    for index in indices:
        res += int(mixed_arr[(index_0+index)%n].split("_")[0])
    return res

def part2(input_arr):
    mixed_arr = input_arr[:]
    n = len(mixed_arr)
    for _ in range(0, 10):
        for num_str in input_arr:
            index = mixed_arr.index(num_str)
            num = int(num_str.split("_")[0])
            if num == 0:
                continue
            mixed_arr.pop(index)
            if num > 0:
                mixed_arr.insert((index+num)%(n-1), num_str)
            elif num < 0:
                mixed_arr.insert((index+num)%(n-1), num_str)

    index_0 = mixed_arr.index("0_0")
    indices = [1000, 2000, 3000]
    res = 0
    for index in indices:
        res += int(mixed_arr[(index_0+index)%n].split("_")[0])
    return res

def main():
    print(part1(read_input()))
    print(part2(read_input(True)))

if __name__ == "__main__":
    main()
