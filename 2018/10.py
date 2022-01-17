import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

class Point:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def update(self):
        self.pos = self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]

def read_input():
    input_lst = []
    with open("input/input10.txt") as input_file:
        for line in input_file:
            line = line.rstrip()[8:].split(" velocity")
            pos  = [int(i) for i in line[0][2:-1].split(", ")]
            vel  = [int(i) for i in line[1][2:-1].split(", ")]
            input_lst.append(Point(pos, vel))
    return input_lst

def vis(lst, max_x, max_y):
    arr = np.zeros((max_y-162+1, max_x-131+1))
    for p in lst:
        arr[p.pos[1]-162][p.pos[0]-131] = 1
    for j in arr:
        print("".join(["⬛"*(int(i)==1)+"⬜"*(int(i)==0) for i in j]))

def part_1(input_lst):
    num_steps = 0
    while True:
        num_steps += 1
        max_x = -1
        max_y = -1
        min_x = int(1e12)
        min_y = int(1e12)
        for p in input_lst:
            p.update()
            max_x = max(max_x, p.pos[0])
            min_x = min(min_x, p.pos[0])
            max_y = max(max_y, p.pos[1])
            min_y = min(min_y, p.pos[1])
        if abs(max_x-min_x) < 100 and abs(max_y-min_y) < 10:
            vis(input_lst, max_x, max_y)
            return num_steps

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
