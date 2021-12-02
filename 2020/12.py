import numpy as np
import math

def read_input():
    input_lst = []
    with open("input/input12.txt") as i_f:
        for line in i_f:
            input_lst.append(line.rstrip())
    return input_lst

def part_1(input_lst):
    curr_pos = [0,0]
    curr_dir = complex(1, 0)
    for line in input_lst:
        direc = line[0]
        val = int(line[1:])
        if direc in ["N", "S", "E", "W"]:
            if direc == "N":
                curr_pos[1] += val
            elif direc == "S":
                curr_pos[1] -= val
            elif direc == "E":
                curr_pos[0] += val
            elif direc == "W":
                curr_pos[0] -= val
        if direc in ["L", "R"]:
            if direc == "L":
                ddir = complex(int(np.cos(np.deg2rad(val))), int(np.sin(np.deg2rad(val))))
                curr_dir *= ddir
            else:
                ddir = complex(int(np.cos(-np.deg2rad(val))), int(np.sin(-np.deg2rad(val))))
                curr_dir *= ddir
        if direc == "F":
            dd = curr_dir*val
            curr_pos[0] += dd.real
            curr_pos[1] += dd.imag
    return math.ceil(abs(curr_pos[0]) + abs(curr_pos[1]))

def part_2(input_lst):
    way_pos  = [10, 1]
    curr_pos = [0,0]
    curr_dir = complex(1, 0)
    for line in input_lst:
        direc = line[0]
        val = int(line[1:])
        if direc in ["N", "S", "E", "W"]:
            if direc == "N":
                way_pos[1] += val
            elif direc == "S":
                way_pos[1] -= val
            elif direc == "E":
                way_pos[0] += val
            elif direc == "W":
                way_pos[0] -= val
        if direc in ["L", "R"]:
            if direc == "L":
                ox = way_pos[0]
                oy = way_pos[1]
                way_pos[0] = ox*int(np.cos(np.deg2rad(val)))-oy*int(np.sin(np.deg2rad(val)))
                way_pos[1] = ox*int(np.sin(np.deg2rad(val)))+oy*int(np.cos(np.deg2rad(val)))
            else:
                ox = way_pos[0]
                oy = way_pos[1]
                way_pos[0] = ox*int(np.cos(-np.deg2rad(val)))-oy*int(np.sin(-np.deg2rad(val)))
                way_pos[1] = ox*int(np.sin(-np.deg2rad(val)))+oy*int(np.cos(-np.deg2rad(val)))
        if direc == "F":
            dd = [way_pos[0], way_pos[1]]
            for i in range(0, len(dd)):
                dd[i] *= val
            curr_pos[0] += dd[0]
            curr_pos[1] += dd[1]
    return math.ceil(abs(curr_pos[0]) + abs(curr_pos[1]))

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

main()
