from collections import defaultdict, Counter

def read_input():
    input_lst = []
    with open("input/input22.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            line = line.split()
            line[1] = line[1].split(",")
            cmd = line[0]
            x_range = line[1][0].split("..")
            y_range = line[1][1].split("..")
            z_range = line[1][2].split("..")
            x_range[0] = x_range[0][2:]
            y_range[0] = y_range[0][2:]
            z_range[0] = z_range[0][2:]
            x_range = [int(i) for i in x_range]
            y_range = [int(i) for i in y_range]
            z_range = [int(i) for i in z_range]
            input_lst.append([cmd, x_range, y_range, z_range])
    return input_lst

def part_1(input_lst):
    cubes = {}
    for cmd, x_r, y_r, z_r in input_lst:
        for x in range(max(x_r[0], -50), min(x_r[1]+1, 50)):
            for y in range(max(y_r[0], -50), min(y_r[1]+1, 50)):
                for z in range(max(z_r[0], -50), min(z_r[1]+1, 50)):
                    cubes[(x,y,z)] = 1 if cmd == "on" else 0
    return sum(cubes.values())

def part_2(input_lst):
    res = 0
    cubes = defaultdict(int)
    for cmd, x_r, y_r, z_r in input_lst:
        #If the command is off, we ONLY care about the intersections with cubes that currently have a val of +1.
        #If the command is on, we care about the entire cube, but must add a cube with a val of -1 for all overlapping volumes with cubes of value 1.
        new_cubes = defaultdict(int)
        if cmd == "on":
            new_cubes[(*x_r,*y_r,*z_r)] += 1
        for cube in cubes:
            x_int_r = [max(x_r[0], cube[0]), min(x_r[1], cube[1])]
            y_int_r = [max(y_r[0], cube[2]), min(y_r[1], cube[3])]
            z_int_r = [max(z_r[0], cube[4]), min(z_r[1], cube[5])]
            if x_int_r[0] > x_int_r[1] or y_int_r[0] > y_int_r[1] or z_int_r[0] > z_int_r[1]:
                continue
            new_cubes[(*x_int_r, *y_int_r, *z_int_r)] -= cubes[cube]
        for k,v in new_cubes.items():
            cubes[k] += v
    sm = 0
    for cube in cubes:
        sm += abs(cube[1]-cube[0]+1)*abs(cube[3]-cube[2]+1)*abs(cube[5]-cube[4]+1)*cubes[cube]
    return sm

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
