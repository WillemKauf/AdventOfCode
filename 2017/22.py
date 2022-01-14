from collections import defaultdict

def read_input(mp={".":0, "#":1}, typ=int):
    input_lst = []
    with open("input/input22.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    input_dct = defaultdict(typ)
    r, c = len(input_lst), len(input_lst[0])
    for j in range(0, r):
        for i in range(0, c):
            input_dct[(i,j)] = mp[input_lst[j][i]]
    return input_dct, complex(r//2,c//2)

def part_1(grid, pos):
    direc = complex(0,1)
    res   = 0
    for _ in range(0, 10000):
        x,y = int(pos.real), int(pos.imag)
        c   = grid[(x,y)]
        if c == 0:
            direc *= complex(0, 1)
            grid[(x,y)] = 1
            res += 1
        else:
            direc *= complex(0, -1)
            grid[(x,y)] = 0
        pos = complex(pos.real + direc.real, pos.imag - direc.imag)
    return res

def part_2(grid, pos):
    direc = complex(0,1)
    res   = 0
    for _ in range(0, 10000000):
        x,y = int(pos.real), int(pos.imag)
        c   = grid[(x,y)]
        if c == "C":
            direc *= complex(0, 1)
            grid[(x,y)] = "W"
        elif c == "W":
            grid[(x,y)] = "I"
            res += 1
        elif c == "I":
            direc *= complex(0, -1)
            grid[(x,y)] = "F"
        elif c == "F":
            direc *= complex(-1,0)
            grid[(x,y)] = "C"
        pos = complex(pos.real + direc.real, pos.imag - direc.imag)
    return res

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input({".":"C", "#":"I"}, lambda: "C")))

if __name__ == "__main__":
    main()
