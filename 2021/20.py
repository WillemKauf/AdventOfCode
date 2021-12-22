import itertools

def read_input():
    input_lst = []
    with open("input/input20.txt") as input_file:
        input_str = input_file.readline().rstrip()
        input_file.readline()
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_str, input_lst

def part_1(input_str, input_lst, n=2):
    dct = {}
    mp  = {".":0, "#":1}
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            dct[(i,j)] = mp[input_lst[j][i]]

    ddir = sorted([prod for prod in itertools.product([-1,0,1], repeat=2)], key = lambda p:p[1])
    for k in range(0, n):
        to_visit = set([(p[0]+dx, p[1]+dy) for p in dct.keys() for dx,dy in ddir])
        new_dct = {}
        for p in to_visit:
            bin_str = ""
            for dx, dy in ddir:
                new_p = (p[0]+dx, p[1]+dy)
                if new_p not in dct:
                    if k % 2 == 0:
                        bin_str += str(mp[input_str[-1]])
                    else:
                        bin_str += str(mp[input_str[0]])
                else:
                    bin_str += str(dct[new_p])
            assert len(bin_str) == 9
            new_dct[p] = mp[input_str[int(bin_str,2)]]
        dct = new_dct
    return sum(dct.values())

def part_2(input_str, input_lst):
    return part_1(input_str, input_lst, 50)

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
