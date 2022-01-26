from Intcode import IntCode
from copy import deepcopy
import itertools

def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            input_lst = [int(i) for i in line.rstrip().split(",")]
    return input_lst

def part_1():
    #By hand.
    program  = ["west", "south", "take pointer", "south", "take prime number", "west", "take coin", "east", "north", "north", "east", "south", "take festive hat", "north", "east", "south", "south", "take space heater", "south", "take astrolabe", "north", "north", "north", "north", "take wreath", "north", "west", "take dehydrated water", "north", "east"]
    inv = ["wreath", "space heater", "coin", "pointer", "dehydrated water", "astrolabe", "festive hat", "prime number"]
    intcode  = IntCode(read_input())
    for i in range(0, len(program)+1):
        output     = intcode.parse_tape_with_output()
        output_str = ""
        for c in output:
            output_str += chr(c)
        output_str = output_str.strip().split()
        if len(program):
            cmd = program.pop(0)
            input_lst = [ord(i) for i in cmd]+[ord('\n')]
            intcode.set_input(input_lst)

    #Brute force. A binary search would work too.
    for n in range(0, len(inv)):
        for comb in itertools.combinations(inv, n):
            quick_save = deepcopy(intcode)
            new_program = []
            for item in comb:
                new_program.append(f"drop {item}")
            new_program.append("inv")
            new_program.append("south")
            for i in range(0, len(new_program)+1):
                output     = quick_save.parse_tape_with_output()
                output_str = ""
                for c in output:
                    output_str += chr(c)
                output_str = output_str.strip().split()
                if "Santa" in output_str:
                    return output_str[-8]
                if len(new_program):
                    cmd = new_program.pop(0)
                    input_lst = [ord(i) for i in cmd]+[ord('\n')]
                    quick_save.set_input(input_lst)

def main():
    print(part_1())

if __name__ == "__main__":
    main()
