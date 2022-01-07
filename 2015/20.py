def read_input():
    input_num = []
    with open("input/input20.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num

def part_1(input_num):
    def get_factors(house):
        factors = set()
        for i in range(1, int(house**1/2)+1):
            if (house % i) == 0:
                factors.add(i)
                factors.add(house//i)
        return factors

    house = 500000
    while True:
        factors      = get_factors(house)
        num_presents = 10*sum(factors)
        if num_presents >= input_num:
            return house
        house += 1
    return None

def part_2(input_num):
    def get_factors(house):
        factors = set()
        for i in range(1, int(house**1/2)+1):
            if (house % i) == 0:
                if house//i*50 >= house:
                    factors.add(house//i)
                if i*50 >= house:
                    factors.add(i)
        return factors
    house = 786240
    while True:
        factors      = get_factors(house)
        num_presents = 11*sum(factors)
        if num_presents >= input_num:
            return house
        house += 1
    return None


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()

