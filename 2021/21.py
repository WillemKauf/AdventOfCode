import itertools
from collections import deque

def read_input():
    input_lst = []
    with open("input/input21.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            input_lst.append(int(line[-1]))
    return input_lst

def part_1(input_lst):
    p1    = input_lst[0]
    p2    = input_lst[1]
    p1_s  = 0
    p2_s  = 0
    die   = deque(range(1,100+1))
    board = [i for i in range(1, 10+1)]
    it    = 0
    n     = len(board)
    while True:
        roll = die[0]+die[1]+die[2]
        die.rotate(-3)
        if it % 2 == 0:
            p1 = board[(p1+roll-1)%n]
            p1_s += p1
        else:
            p2 = board[(p2+roll-1)%n]
            p2_s += p2
        it += 1
        if p1_s >= 1000 or p2_s >= 1000:
            return min(p1_s, p2_s)*it*3

def part_2(input_lst):
    p1        = input_lst[0]
    p2        = input_lst[1]
    board     = [i for i in range(1, 10+1)]
    dp        = {}
    n         = len(board)
    die_rolls = [prod for prod in itertools.product([1,2,3], repeat=3)]
    def recursive_play(p1, p2, p1_s, p2_s, it):
        p1_res, p2_res = 0, 0
        p_turn = it % 2
        if p1_s >= 21:
            return (1,0)
        if p2_s >= 21:
            return (0,1)
        if (p1, p2, p1_s, p2_s, p_turn) in dp:
            return dp[(p1, p2, p1_s, p2_s, p_turn)]
        for prod in die_rolls:
            roll = sum(prod)
            if p_turn == 0:
                n_p1_res, n_p2_res = recursive_play(board[(p1+roll-1)%n], p2, p1_s + board[(p1+roll-1)%n], p2_s, it+1)
            else:
                n_p1_res, n_p2_res = recursive_play(p1, board[(p2+roll-1)%n], p1_s, p2_s + board[(p2+roll-1)%n], it+1)
            p1_res += n_p1_res
            p2_res += n_p2_res
        dp[(p1, p2, p1_s, p2_s, p_turn)] = (p1_res, p2_res)
        return p1_res, p2_res
    return max(recursive_play(p1, p2, 0, 0, 0))

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
