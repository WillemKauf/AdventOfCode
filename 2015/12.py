import re
import json

def solve_puzzle():
    with open("input/input12.txt") as input_file:
        regex = r"([-+]?\d+)"
        return sum([int(i) for i in re.findall(regex, input_file.read())])


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

def solve_puzzle2():
    input_arr = json.loads(open('input/input12.txt', 'r').read())
    sm = 0
    for arr in input_arr:
        sm += recursive_solve(arr)
    return sm

def main():
    print(solve_puzzle())
    print(solve_puzzle2())

main()
