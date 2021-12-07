import re
import json

def part_1():
    with open("input/input12.txt") as input_file:
        regex = r"([-+]?\d+)"
        return sum([int(i) for i in re.findall(regex, input_file.read())])

def part_2():
    def recursive_solve(arr):
        if isinstance(arr, dict):
            if "red" in arr.values():
                return 0
            else:
                return sum(map(recursive_solve, arr.values()))
        elif isinstance(arr, list):
            return sum(map(recursive_solve, arr))
        elif isinstance(arr, int):
            return arr
        return 0

    input_arr = json.loads(open('input/input12.txt', 'r').read())
    sm = 0
    for arr in input_arr:
        sm += recursive_solve(arr)
    return sm

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
   main()
