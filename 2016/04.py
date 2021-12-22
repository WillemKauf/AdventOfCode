from collections import Counter

class Room:
    def __init__(self, name, sec_ID, check_sum):
        self.name      = name
        self.sec_ID    = sec_ID
        self.check_sum = check_sum

def read_input():
    input_lst = []
    with open("input/input4.txt") as input_file:
        for line in input_file:
            line      = line.rstrip().split("-")
            name      = "".join([i for i in line[:-1]])
            sec_ID    = int(line[-1][:line[-1].index("[")])
            check_sum = line[-1][line[-1].index("[")+1:-1]
            input_lst.append(Room(name, sec_ID, check_sum))
    return input_lst

def part_1(input_lst):
    res = 0
    for room in input_lst:
        c = Counter(sorted(room.name))
        correct_checksum = "".join([k for k, _ in c.most_common(5)])
        if correct_checksum == room.check_sum:
            res += room.sec_ID
    return res

def part_2(input_lst):
    for room in input_lst:
        sec_ID     = room.sec_ID
        len_mod    = ord('z')-ord('a')

        new_name   = "".join([chr((ord(s)-ord('a')+sec_ID%(ord('z')-ord('a')+1))%(ord('z')-ord('a')+1)+ord('a')) for s in room.name])
        if new_name == "northpoleobjectstorage":
            return sec_ID
    return None


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
