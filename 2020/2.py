class Info():
    def __init__(self, min_b, max_b, letter, password):
        self.min_b    = min_b
        self.max_b    = max_b
        self.letter   = letter
        self.password = password

def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            line         = line.split()
            bounds       = line[0].split("-")
            min_b, max_b = [int(i) for i in bounds]
            letter       = line[1][0]
            password     = line[2]
            info         = Info(min_b, max_b, letter, password)
            input_lst.append(info)
    return input_lst

def part_1(input_lst):
    res = 0
    for info in input_lst:
        min_b    = info.min_b
        max_b    = info.max_b
        letter   = info.letter
        password = info.password
        count    = password.count(letter)
        if(min_b <= count <= max_b):
            res += 1
    return res

def part_2(input_lst):
    res = 0
    for info in input_lst:
        min_b    = info.min_b
        max_b    = info.max_b
        letter   = info.letter
        password = info.password
        if sum([password[min_b-1] == letter, password[max_b-1] == letter]) == 1:
            res += 1
    return res


def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

