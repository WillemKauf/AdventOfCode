def read_input():
    input_lst = []
    with open("input/input7.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(',')]
    return input_lst

def part_1(input_lst):
    min_fuel = 999999999999
    for i, num in enumerate(input_lst):
        curr_fuel_cost = 0
        for i2, num2 in enumerate(input_lst):
            curr_fuel_cost += abs(num2 - num)
        min_fuel = min(curr_fuel_cost, min_fuel)
    return min_fuel

def part_2(input_lst):
    min_fuel = 999999999999
    for i2, num2 in enumerate(range(min(input_lst), max(input_lst))):
        curr_fuel_cost = 0
        for i, num in enumerate(input_lst):
            sm = sum(range(1, abs(num2-num)+1))
            curr_fuel_cost += sm
        min_fuel = min(curr_fuel_cost, min_fuel)
    return min_fuel

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
