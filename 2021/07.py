def read_input():
    input_lst = []
    with open("input/input7.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(',')]
    return input_lst

def part_1(input_lst):
    pos = sorted(input_lst)[len(input_lst)//2]
    return sum([abs(p-pos) for p in input_lst])

def part_2(input_lst):
    min_fuel = int(1e12)
    for i2, num2 in enumerate(range(min(input_lst), max(input_lst))):
        curr_fuel_cost = 0
        for i, num in enumerate(input_lst):
            n  = abs(num2-num)
            sm = n*(n+1)//2
            curr_fuel_cost += sm
        min_fuel = min(curr_fuel_cost, min_fuel)
    return min_fuel

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
