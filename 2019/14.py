import math
from collections import defaultdict

def read_input():
    input_dct = {}
    ore_dct   = {}
    with open("input/input14.txt") as input_file:
        for line in input_file:
            line            = line.rstrip()
            line            = line.split(" => ")
            reactants       = line[0].split(", ")
            n_product, prod = line[1].split(" ")
            n_reactants     = [int(i.split(" ")[0]) for i in reactants]
            reacts          = [i.split(" ")[1] for i in reactants]
            input_dct[prod] = [int(n_product), {reacts[i]:n_reactants[i] for i in range(0, len(n_reactants))}]
    return input_dct

def part_1(input_dct):
    def recursive_solve(element, n_element, n_ore, inv):
        n_product, react_dct = input_dct[element]
        n_float              = inv[element]
        mul_fac              = math.ceil((n_element - n_float)/n_product)
        n_produce            = mul_fac*n_product
        n_total              = n_float + n_produce
        n_extra              = n_total - n_element
        inv[element]         = n_extra

        if len(react_dct) == 1 and "ORE" in react_dct:
            n_ore += mul_fac*react_dct["ORE"]
            return inv, n_ore

        for react, n_react in react_dct.items():
            inv, n_ore = recursive_solve(react, mul_fac*n_react, n_ore, inv)

        return inv, n_ore
    return recursive_solve("FUEL", 1, 0, defaultdict(int))[1]

def part_2(input_dct):
    def recursive_solve(element, n_element, n_ore, inv):
        n_product, react_dct = input_dct[element]
        n_float              = inv[element]
        mul_fac              = math.ceil((n_element - n_float)/n_product)
        n_produce            = mul_fac*n_product
        n_total              = n_float + n_produce
        n_extra              = n_total - n_element
        inv[element]         = n_extra

        if len(react_dct) == 1 and "ORE" in react_dct:
            n_ore += mul_fac*react_dct["ORE"]
            return inv, n_ore

        for react, n_react in react_dct.items():
            inv, n_ore = recursive_solve(react, mul_fac*n_react, n_ore, inv)

        return inv, n_ore
    def binary_search(l, r, n_ore):
        while l < r-1:
            m   = math.floor((l+r)/2)
            res = recursive_solve("FUEL", m, 0, defaultdict(int))[1]
            if res < n_ore:
                l = m
            elif res > n_ore:
                r = m
            else:
                return m
        return m
    return binary_search(0, 50000000, 1000000000000)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
