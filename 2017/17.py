from collections import deque

def read_input():
    input_num = []
    with open("input/input17.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num

def part_1(num_steps):
    queue = deque([0])
    for _ in range(0, 2017):
        n = len(queue)
        queue.rotate(-num_steps)
        queue.append(n)

    return queue.popleft()

def part_2(num_steps):
    p = 0
    n = 1
    num = None
    for _ in range(0, int(50e6)):
        p = (p + num_steps)%n + 1
        if p == 1:
            num = n
        n += 1
    return num

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
