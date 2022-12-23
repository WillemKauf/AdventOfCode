from sympy import symbols, solve
from sympy.parsing.sympy_parser import parse_expr

def read_input(p2=False):
    input_arr = []
    with open("input/input21.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            line = line.split(": ")
            if p2:
                if line[0] == "root":
                    line[1] = line[1].replace("+", "=")
            input_arr.append(line)
    return input_arr

def part1(input_arr):
    i = 0
    n = len(input_arr)
    ops = ["+", "-", "*", "/"]
    nums = {}
    while True:
        for monkey, job in input_arr:
            if job.isnumeric():
                nums[monkey] = int(job)
            else:
                for op in ops:
                    if job.find(op) != -1:
                        dep_monkeys = job.split(f" {op} ")
                        if dep_monkeys[0] in nums and dep_monkeys[1] in nums:
                            eval_str = f"nums[dep_monkeys[0]] {op} nums[dep_monkeys[1]]"
                            nums[monkey] = int(eval(eval_str))
        if "root" in nums:
            return nums["root"]

def recurse(input_arr, curr_monkey, vals):
    ops = ["+", "-", "*", "/"]
    for monkey, job in input_arr:
        if curr_monkey == monkey:
            if job.isnumeric():
                if monkey == "humn":
                    vals[curr_monkey] = "HUMN"
                else:
                    vals[curr_monkey] = int(job)
            else:
                for op in ops:
                    if job.find(op) != -1:
                        dep_monkeys = job.split(f" {op} ")
                        vals[curr_monkey] = f"({recurse(input_arr, dep_monkeys[0], vals)} {op} {recurse(input_arr, dep_monkeys[1], vals)})"
    return vals[curr_monkey]

def part2(input_arr):
    start = "root"
    vals = {}
    for monkey, job in input_arr:
        if monkey == start:
            start_job = job
            vals[start] = start_job
            break
    sym_monkeys = []
    dep_monkeys = start_job.split(" = ")
    for dep_monkey in dep_monkeys:
        recurse(input_arr, dep_monkey, vals)
    HUMN = symbols("HUMN")
    expr = parse_expr(vals[dep_monkeys[1]]) - parse_expr(vals[dep_monkeys[0]])
    return solve(expr)[0]

def main():
    print(part1(read_input()))
    print(part2(read_input(True)))

if __name__ == "__main__":
    main()
