from copy import deepcopy
from collections import deque

def read_input():
    input_lst = []
    with open("input/input22.txt") as input_file:
        curr_lst = []
        for line in input_file:
            line = line.rstrip()
            if line == "":
                input_lst.append(curr_lst)
                curr_lst = []
                continue
            if line[:6] != "Player":
                curr_lst.append(int(line))
        if len(curr_lst):
            input_lst.append(curr_lst)
    return input_lst

def part_1(input_lst):
    p1_deck = deque(input_lst[0])
    p2_deck = deque(input_lst[1])
    counter = 0
    while True:
        counter += 1
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()
        if p1_card > p2_card:
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
        if not len(p2_deck) or not len(p1_deck):
            winning_deck = list(p1_deck*(len(p1_deck) > 0)+p2_deck*(len(p2_deck) > 0))
            break

    return sum([num*(i+1) for i, num in enumerate(winning_deck[::-1])])

def part_2(input_lst):
    def recursive_combat(p1_deck, p2_deck):
        seen_p1_decks = []
        seen_p2_decks = []
        while True:
            if p1_deck in seen_p1_decks or p2_deck in seen_p2_decks:
                return ["P1", p1_deck]
            seen_p1_decks.append(p1_deck.copy())
            seen_p2_decks.append(p2_deck.copy())
            p1_card = p1_deck.popleft()
            p2_card = p2_deck.popleft()
            if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
                new_p1_deck = deque([i for i in p1_deck][:p1_card])
                new_p2_deck = deque([i for i in p2_deck][:p2_card])
                winning_deck = recursive_combat(new_p1_deck, new_p2_deck)
                if winning_deck[0] == "P1":
                    p1_deck.append(p1_card)
                    p1_deck.append(p2_card)
                else:
                    p2_deck.append(p2_card)
                    p2_deck.append(p1_card)
            else:
                if p1_card > p2_card:
                    p1_deck.append(p1_card)
                    p1_deck.append(p2_card)
                else:
                    p2_deck.append(p2_card)
                    p2_deck.append(p1_card)

            if not len(p2_deck):
                return ["P1", p1_deck]
            elif not len(p1_deck):
                return ["P2", p2_deck]

    p1_deck      = deque(input_lst[0])
    p2_deck      = deque(input_lst[1])
    winning_deck = list(recursive_combat(p1_deck, p2_deck)[1])
    return sum([num*(i+1) for i, num in enumerate(winning_deck[::-1])])

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()

