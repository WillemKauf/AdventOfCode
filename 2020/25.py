def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip()))
    return input_lst

def transform(subject_number):
    val       = 1
    loop_size = 0
    while True:
        loop_size += 1
        val       *= subject_number
        val        = val % 20201227
        yield val, loop_size

def transform_with_loop_size(subject_number, loop_size):
    val = 1
    for _ in range(0, loop_size):
        val       *= subject_number
        val        = val % 20201227
    return val

def part_1(input_lst):
    card_pub, door_pub = input_lst
    card_loop_size     = None
    door_loop_size     = None
    for card_val, card_size in transform(7):
        if card_val == card_pub:
            card_loop_size = card_size
            break

    for door_val, door_size in transform(7):
        if door_val == door_pub:
            door_loop_size = door_size
            break

    if card_loop_size < door_loop_size:
        subject_number = card_pub
        loop_size      = door_loop_size
    else:
        subject_number = door_pub
        loop_size      = card_loop_size

    return transform_with_loop_size(subject_number, loop_size)

def main():
    input_lst = read_input()
    print(part_1(input_lst))

if __name__ == "__main__":
    main()

