def read_input():
    input_lst = []
    with open("input/input25.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            input_lst.append(int(line[-3][:-1]))
            input_lst.append(int(line[-1][:-1]))
    return input_lst

def part_1(input_lst):
    r, c     = input_lst
    n1       = 20151125
    mul_fac  = 252533
    mod_fac  = 33554393
    curr_num = n1
    ind      = 2
    while True:
        i = 0
        j = ind+1
        dd = [1, -1]
        for k in range(0, ind):
            i += dd[0]
            j += dd[1]
            curr_num = (curr_num*mul_fac)%mod_fac
            if (i,j) == (c,r):
                return curr_num
        ind += 1
    return curr_num

def part_2(input_lst):
    pass

def main():
    print(part_1(read_input()))
    #print(part_2(read_input()))

if __name__ == "__main__":
    main()
