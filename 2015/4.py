import hashlib
def read_input():
    input_arr = []
    with open("input/input4.txt") as input_file:
        for line in input_file.readlines():
            input_arr = line.rstrip()
    return input_arr

def part_1(input_arr):
    max_number = int(1e6)
    for i in range(0, max_number):
        curr_str = input_arr + str(i)
        curr_hsh = hashlib.md5(curr_str.encode("utf-8")).hexdigest()
        if(curr_hsh[:5] == "00000"):
            return i

def part_2(input_arr):
    max_number = int(1e8)
    for i in range(0, max_number):
        curr_str = input_arr + str(i)
        curr_hsh = hashlib.md5(curr_str.encode("utf-8")).hexdigest()
        if(curr_hsh[:6] == "000000"):
            return i

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

main()
