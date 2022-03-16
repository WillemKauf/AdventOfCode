import itertools
import numpy as np
from collections import defaultdict

class Scanner:
    def __init__(self, num, lst):
        self.num = num
        self.lst = lst

def read_input():
    input_lst = []
    with open("input/input19.txt") as input_file:
        curr_lst = []
        num      = None
        for line in input_file:
            line = line.rstrip()
            if line == "":
                input_lst.append(Scanner(num, curr_lst))
                curr_lst = []
                num      = None
            elif line[0:3] == "---":
                num = int(line.split()[2])
            else:
                curr_lst.append(np.array([int(i) for i in line.split(",")], dtype=np.float64))
        if len(curr_lst):
            input_lst.append(Scanner(num, curr_lst))
    return input_lst

def get_orientations():
    facs = [-1, 1]
    rot_matrices = []
    for x,y,z in itertools.product(facs, repeat=3):
        for perm in itertools.permutations([[x,0,0],[0,y,0],[0,0,z]]):
            rot_matrix = np.array(perm)
            if np.linalg.det(rot_matrix) > 0:
                rot_matrices.append(rot_matrix)
    return rot_matrices

def recursive_parse(n1, n2, offset_dct, rot_dct, offset, rotation, seen):
    """The offset originally passed is in the n1 coordinate system.
       new_offset is distance from n1->n2 (A->B), in the n2 coordinate system.
       rot_mat    is the rotation matrix that will get from coordinate system B to coordinate system A.
    """
    scan_offset   = offset_dct[n2][n1]
    rot_mat       = rot_dct[n2][n1]
    new_rotation  = np.dot(rotation, rot_mat)
    new_offset    = np.dot(offset + scan_offset, rot_mat)
    if n2 == 0:
        return new_offset, new_rotation
    else:
        for node, dct in offset_dct.items():
            if n2 in dct and node not in seen:
                res = recursive_parse(n2, node, offset_dct, rot_dct, new_offset, new_rotation, seen|set([n1]))
                if res != None:
                    return res

def part_1(input_lst):
    rot_mats      = get_orientations()
    seen_beacons  = set()
    seen_scanners = set()
    offset_dct    = defaultdict(dict)
    rot_dct       = defaultdict(dict)
    for scanner_1 in input_lst:
        for scanner_2 in input_lst:
            rep = tuple(sorted([scanner_1.num, scanner_2.num]))
            if scanner_1 == scanner_2 or rep in seen_scanners:
                continue
            seen_scanners.add(rep)
            for rot_mat in rot_mats:
                hsh_mp = defaultdict(list)
                for s1 in scanner_1.lst:
                    rot = np.dot(rot_mat, s1)
                    for s2 in scanner_2.lst:
                        diff = rot - s2
                        hsh_mp[tuple(diff)].append(s2)
                for k, s_lst in hsh_mp.items():
                    if(len(s_lst) >= 12):
                        offset_dct[scanner_1.num][scanner_2.num] = np.array(k)
                        rot_dct[scanner_1.num][scanner_2.num]    = rot_mat
                        offset_dct[scanner_2.num][scanner_1.num] = np.dot(np.linalg.inv(rot_mat), -np.array(k))
                        rot_dct[scanner_2.num][scanner_1.num]    = np.linalg.inv(rot_mat)
                        for s in s_lst:
                            seen_beacons.add(tuple(s))
    zero_offset_dct = {}
    zero_rot_dct    = {}
    for n1, n_dct in offset_dct.items():
        for n2, offset in n_dct.items():
            if n1 != 0 and n1 not in zero_offset_dct:
                zero_offset_dct[n1], zero_rot_dct[n1] = recursive_parse(n1, n2, offset_dct, rot_dct, np.zeros(3), np.identity(3), set())
    beacons = set()
    for scanner in input_lst:
        offset = zero_offset_dct[scanner.num] if scanner.num != 0 else np.zeros(3)
        rot    = zero_rot_dct[scanner.num] if scanner.num != 0 else np.identity(3)
        for p in scanner.lst:
            d  = np.dot(p, rot) #The distance from the beacon to the scanner in the 0th coordinate system
            d0 = offset + d #The distance from the beacon to the 0th scanner
            beacons.add(tuple(d0))
    len_beacons = len(beacons)

    largest_dist = -1
    for s1, d1 in zero_offset_dct.items():
        for s2, d2 in zero_offset_dct.items():
            dist = int(sum(np.abs(d1-d2)))
            largest_dist = max(largest_dist, dist)

    return len_beacons, largest_dist


def main():
    p1, p2 = part_1(read_input())
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
