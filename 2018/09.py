from collections import deque, defaultdict

def read_input():
    input_lst = []
    with open("input/input9.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_lst = [int(line[0]), int(line[-2])]
    return input_lst

def part_1(input_lst):
    marbles              = deque([0])
    n_players, n_marbles = input_lst
    players              = defaultdict(int)
    for i in range(1, n_marbles+1):
        if i % 23 == 0:
            c_player = i % n_players
            players[c_player] += i
            marbles.rotate(7)
            players[c_player] += marbles.popleft()
        else:
            marbles.rotate(-2)
            marbles.appendleft(i)
    return max(players.values())

def part_2(input_lst):
    input_lst[1] *= 100
    return part_1(input_lst)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
