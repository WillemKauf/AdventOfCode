def read_input():
    input_arr = []
    with open("input/input1.txt") as input_file:
        for line in input_file.readlines():
            for char in line.rstrip():
                input_arr.append(char)
    return input_arr

def part_1(input_arr):
    return sum(map(lambda s: 1 if s == "(" else -1, input_arr))

def part_2(input_arr):
    curr_level = 0
    for i, val in enumerate(input_arr):
        direc = 1 if val == "(" else -1
        curr_level += direc
        if curr_level == -1:
            return i+1
    return None

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
