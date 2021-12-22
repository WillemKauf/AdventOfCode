import numpy as np
from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input10.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    res = 0
    pos = (None, None)
    unique_lst = [(i,j) for j in range(0, len(input_lst)) for i in range(0, len(input_lst[j])) if input_lst[j][i] == "#"]
    def test_pos(i,j):
        seen = set()
        for ii,jj in unique_lst:
            angle = np.arctan2(j-jj,i-ii)
            if angle not in seen:
                seen.add(angle)
        return len(seen)

    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            if input_lst[j][i] == "#":
                new_res = test_pos(i,j)
                if new_res >= res:
                    res = new_res
                    pos = (i,j)
    return res, pos

def part_2(input_lst, pos):
    unique_lst = [(i,j) for j in range(0, len(input_lst)) for i in range(0, len(input_lst[j])) if input_lst[j][i] == "#" and (i,j) != pos]
    ast_angles = defaultdict(list)
    for k, ast in enumerate(unique_lst):
        i,j = ast
        angle = np.arctan2(pos[1]-j,pos[0]-i)-np.pi/2
        if angle < 0:
            angle += 2*np.pi
        ast_angles[angle].append(ast)

    for angle, dist_lst in ast_angles.items():
        ast_angles[angle] = sorted(dist_lst, key = lambda p: abs(pos[1]-p[1])+abs(pos[0]-p[0]))
    ast_angles = sorted(ast_angles.items())

    num_destroyed = 0
    while True:
        for i in range(0, len(ast_angles)):
            curr = ast_angles[i][1].pop(0)
            num_destroyed += 1
            if num_destroyed == 200:
                return curr[0]*100+curr[1]
    return None

def main():
    res, pos = part_1(read_input())
    print(res, pos)
    print(part_2(read_input(), pos))

if __name__ == "__main__":
    main()
