def read_input():
    input_lst = []
    with open("input/input2.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    pos     = [1,1]
    keypad  = [[1,2,3],[4,5,6],[7,8,9]]
    hsh_map = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
    res = ""
    for line in input_lst:
        for s in line:
            ddir = hsh_map[s]
            if 0 <= pos[0]+ddir[0] < len(keypad):
                pos[0] += ddir[0]
            if 0 <= pos[1]+ddir[1] < len(keypad):
                pos[1] += ddir[1]
        res += str(keypad[pos[1]][pos[0]])
    return int(res)

def part_2(input_lst):
    pos     = [2,0]
    keypad  = [[None, None, 1, None, None], [None, 2, 3, 4, None], [5,6,7,8,9], [None, "A", "B", "C", None],[None, None, "D", None, None]]
    hsh_map = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
    res = ""
    for line in input_lst:
        for s in line:
            ddir = hsh_map[s]
            if 0 <= pos[0]+ddir[0] < len(keypad):
                if keypad[pos[1]][pos[0]+ddir[0]] != None:
                    pos[0] += ddir[0]
            if 0 <= pos[1]+ddir[1] < len(keypad):
                if keypad[pos[1]+ddir[1]][pos[0]] != None:
                    pos[1] += ddir[1]
        res += str(keypad[pos[1]][pos[0]])
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
