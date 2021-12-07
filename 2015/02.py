def read_input():
    input_arr = []
    with open("input/input2.txt") as input_file:
        for line in input_file.readlines():
            l,w,h = [int(i) for i in line.rstrip().split("x")]
            curr_arr = [l,w,h]
            input_arr.append(curr_arr)
    return input_arr

def part_1(input_arr):
    ribbon_amount = lambda lst: 2*lst[0]*lst[1] + 2*lst[1]*lst[2] + 2*lst[2]*lst[0] + min(lst[0]*lst[1], lst[0]*lst[2], lst[1]*lst[2])
    return sum(map(ribbon_amount, [lst for lst in input_arr]))

def part_2(input_arr):
    ribbon_amount = lambda lst: lst[0]*lst[1]*lst[2] + 2*(sum(lst)-max(lst))
    return sum(map(ribbon_amount, [lst for lst in input_arr]))

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
