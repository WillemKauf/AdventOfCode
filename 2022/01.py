from collections import defaultdict
import heapq

def read_input():
    input_arr = []
    with open("input/input1.txt", "r") as input_file:
        curr_arr = []
        for line in input_file.readlines():
            line = line.rstrip()
            if line == "":
                input_arr.append(curr_arr)
                curr_arr = []
            else:
                curr_arr.append(int(line))
    return input_arr

def part1(input_arr):
    heap = []
    res = defaultdict(int)
    for arr in input_arr:
        heapq.heappush(heap, -sum(arr))
    return -heap[0]

def part2(input_arr):
    heap = []
    res = defaultdict(int)
    for arr in input_arr:
        heapq.heappush(heap, -sum(arr))
    res = 0
    for i in range(0, 3):
        res -= heapq.heappop(heap)
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()
