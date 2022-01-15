import numpy as np

#This is bad old code. But it works.

class Coord:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def read_input():
    with open("input/input6.txt") as inputFile:
        input_lst = [[int(x) for x in line.split(",")] for line in inputFile]
    return input_lst

def on_edge(coordName, area_grid):
    for j in range(0, len(area_grid)):
        for i in [0, len(area_grid[j])-1]:
            if area_grid[j][i] == coordName:
                return True
    for j in [0, len(area_grid)-1]:
        for i in range(1, len(area_grid[j])-1):
            if area_grid[j][i] == coordName:
                return True
    return False

def part_1(input_lst):
    max_x = max(input_lst, key = lambda x:x[0])[0]
    max_y = max(input_lst, key = lambda x:x[1])[1]
    area_grid = np.zeros((max_x, max_y))
    coord_lst = [Coord(x,y,name) for name, (x, y) in enumerate(input_lst, 1)]
    for j in range(0, len(area_grid)):
        for i in range(0, len(area_grid[j])):
            min_dist = 1e12
            for coord in coord_lst:
                curr_dist = abs(i-coord.x)+abs(j-coord.y)
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    min_coord = coord.name
                elif curr_dist == min_dist:
                    min_coord = -1
            area_grid[j][i] = min_coord
    max_area = 0
    for coord in coord_lst:
        if on_edge(coord.name, area_grid):
            continue
        if (area_grid == coord.name).sum() > max_area:
            max_area = (area_grid == coord.name).sum()
    return max_area

def part_2(input_arr):
    max_x = max(input_arr, key = lambda x:x[0])[0]
    max_y = max(input_arr, key = lambda x:x[1])[1]
    area_grid = np.zeros((max_x, max_y))
    coord_arr = [Coord(x,y,name) for name, (x, y) in enumerate(input_arr, 1)]
    max_dist = 10000
    region_size = 0
    for j in range(0, len(area_grid)):
        for i in range(0, len(area_grid[j])):
            total_dist = 0
            for coord in coord_arr:
                curr_dist = abs(i-coord.x)+abs(j-coord.y)
                total_dist += curr_dist
            if total_dist < max_dist:
                region_size += 1
    return region_size

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

main()
