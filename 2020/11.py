from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input11.txt") as input_file:
        for line in input_file:
            input_lst.append([c for c in line.rstrip()])
    return input_lst

def part_1(input_lst):
    while True:
        new_lst = deepcopy(input_lst)
        changed_flag = True
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                if input_lst[j][i] == ".":
                    continue
                neighbours = []
                for dj in [-1,0,1]:
                    for di in [-1,0,1]:
                        if (dj,di) == (0,0):
                            continue
                        curr_j = j+dj
                        curr_i = i+di
                        if 0 <= curr_j < len(input_lst) and 0 <= curr_i < len(input_lst[j]):
                            neighbours.append(input_lst[curr_j][curr_i])
                occupied_neighbours = neighbours.count("#")
                if input_lst[j][i] == "L" and occupied_neighbours == 0:
                    new_lst[j][i] = "#"
                    changed_flag = False
                elif input_lst[j][i] == "#" and occupied_neighbours >= 4:
                    new_lst[j][i] = "L"
                    changed_flag = False
        if changed_flag == True:
            return sum([l.count("#") for l in input_lst])
        input_lst = new_lst

def part_2(input_lst):
    while True:
        new_lst = deepcopy(input_lst)
        changed_flag = True
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                if input_lst[j][i] == ".":
                    continue
                neighbours = []
                for dj in [-1, 0, 1]:
                    for di in [-1, 0, 1]:
                        if (dj,di) == (0,0):
                            continue
                        curr_j = j+dj
                        curr_i = i+di
                        while 0 <= curr_j < len(input_lst) and 0 <= curr_i < len(input_lst[j]):
                            curr_n = input_lst[curr_j][curr_i]
                            if curr_n != ".":
                                neighbours.append(curr_n)
                                break
                            curr_j += dj
                            curr_i += di
                occupied_neighbours = neighbours.count("#")
                if input_lst[j][i] == "L" and occupied_neighbours == 0:
                    new_lst[j][i] = "#"
                    changed_flag = False
                elif input_lst[j][i] == "#" and occupied_neighbours >= 5:
                    new_lst[j][i] = "L"
                    changed_flag = False
        if changed_flag == True:
            return sum([l.count("#") for l in input_lst])
        input_lst = new_lst

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

