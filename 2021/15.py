import itertools
import heapq
import numpy as np

def read_input():
    input_lst = []
    with open("input/input15.txt") as input_file:
        for line in input_file:
            input_lst.append([int(i) for i in line.rstrip()])
    return input_lst

def A_star(input_lst):
    queue    = []
    start    = (0,0)
    end      = (len(input_lst[0])-1, len(input_lst)-1)
    seen_dct = {start:None}
    cost_dct = {start:0}
    heapq.heappush(queue, (0,start))
    ddir = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    while len(queue):
        curr_node = heapq.heappop(queue)[1]
        if curr_node == end:
            break
        curr_x, curr_y = curr_node
        for dx, dy in ddir:
            new_x, new_y = curr_x+dx, curr_y+dy
            if 0 <= new_x < len(input_lst[0]) and 0 <= new_y < len(input_lst):
                neighbour = (new_x, new_y)
                new_cost  = cost_dct[curr_node] + input_lst[new_y][new_x]
                if neighbour not in cost_dct or new_cost < cost_dct[neighbour]:
                    cost_dct[neighbour] = new_cost
                    priority            = new_cost + abs(end[0]-neighbour[0]) + abs(end[1]-neighbour[1])
                    heapq.heappush(queue, (priority, neighbour))
                    seen_dct[neighbour] = curr_node
    return cost_dct[end]

def part_1(input_lst):
    return A_star(input_lst)

def part_2(input_lst):
    big_lst = np.copy(input_lst)

    for i in range(1, 5):
        new_lst = np.repeat(input_lst, 1, axis = 1)+i
        for y in range(0, len(new_lst)):
            for x in range(0, len(new_lst[y])):
                if new_lst[y,x] == 0:
                    new_lst[y,x] = 1
                elif new_lst[y,x] > 9:
                    new_lst[y,x] = new_lst[y,x]%9
        big_lst = np.concatenate((big_lst, new_lst), axis=1)
    final_lst = np.copy(big_lst)

    for j in range(1, 5):
        new_lst  = big_lst[0:len(input_lst), :]+j
        for y in range(0, len(new_lst)):
            for x in range(0, len(new_lst[y])):
                if new_lst[y,x] == 0:
                    new_lst[y,x] = 1
                elif new_lst[y,x] > 9:
                    new_lst[y,x] = new_lst[y,x]%9
        final_lst = np.concatenate((final_lst, new_lst), axis = 0)

    return A_star(final_lst)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
