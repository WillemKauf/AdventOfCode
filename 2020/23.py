from collections import deque

def read_input():
    input_lst = None
    with open("input/input23.txt") as input_file:
        for line in input_file:
            input_lst = deque([int(i) for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    def simulate(num_moves, input_lst):
        for _ in range(0, num_moves):
            curr_cup = input_lst[0]
            input_lst.rotate(-1)
            removed_cups = [input_lst.popleft() for _ in range(0, 3)]
            dest_cup = curr_cup-1
            while dest_cup not in input_lst:
                dest_cup = (dest_cup-1)%(n+1)
            dest_cup_index = input_lst.index(dest_cup)
            for cup in removed_cups[::-1]:
                input_lst.insert(dest_cup_index+1, cup)
        return input_lst

    n          = len(input_lst)
    end_circle = simulate(100, input_lst)
    return "".join([str(end_circle[(end_circle.index(1)+i)%n]) for i in range(1, n)])

def part_2(input_lst):
    class Cup:
        def __init__(self, val):
            self.val    = val
            self.next_c = None

        def set_next_cup(self, next_c):
            self.next_c = next_c

    def simulate(num_moves, cup_lst, index_map):
        next_cup = cup_lst[0]
        n = len(input_lst)
        for i in range(0, num_moves):
            curr_cup = next_cup

            removed_cup_vals    = [curr_cup.next_c.val, curr_cup.next_c.next_c.val, curr_cup.next_c.next_c.next_c.val]
            removed_cup_indices = [index_map[removed_cup_val] for removed_cup_val in removed_cup_vals]

            curr_cup.next_c     = cup_lst[removed_cup_indices[-1]].next_c
            dest_cup_val        = curr_cup.val-1

            while dest_cup_val in [cup_lst[cup].val for cup in removed_cup_indices] or dest_cup_val == 0:
                dest_cup_val = (dest_cup_val-1)%(n+1)

            dest_cup_index  = index_map[dest_cup_val]
            dest_cup        = cup_lst[dest_cup_index]

            cup_lst[removed_cup_indices[-1]].next_c = dest_cup.next_c
            dest_cup.next_c                         = cup_lst[removed_cup_indices[0]]
            cup_lst[removed_cup_indices[0]].next_c  = cup_lst[removed_cup_indices[1]]
            cup_lst[removed_cup_indices[1]].next_c  = cup_lst[removed_cup_indices[2]]

            next_cup = curr_cup.next_c

        one_index = index_map[1]
        return cup_lst[one_index].next_c.val*cup_lst[one_index].next_c.next_c.val

    input_lst = list(input_lst) + [i for i in range(max(input_lst)+1, 1000000+1)]
    cup_lst   = []
    index_map = {}

    for i, val in enumerate(input_lst):
        cup_lst.append(Cup(val))
        index_map[val] = i

    n = len(input_lst)
    for i, cup in enumerate(cup_lst):
        cup_lst[i].set_next_cup(cup_lst[(i+1)%n])

    return simulate(10000000, cup_lst, index_map)

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
