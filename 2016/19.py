from collections import deque

def read_input():
    input_int = []
    with open("input/input19.txt") as input_file:
        for line in input_file:
            input_int = int(line.rstrip())
    return input_int

def part_1(input_int):
    elves = deque(range(1, input_int+1))
    n     = input_int
    while n > 1:
        elves.rotate(-1)
        elves.popleft()
        n -= 1
    return elves.popleft()


def part_2(input_int):
    elves  = deque(range(1, input_int+1))
    offset = 0
    n      = input_int
    while n > 1:
        rot = n//2
        elves.rotate(-(rot-offset))
        elves.popleft()
        n -= 1
        offset = (rot-1) % n
    return elves.popleft()

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
