import numpy as np

def read_input():
    input_lst = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            input_lst = np.array([int(i) for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    width     = 25
    height    = 6
    min_zeros = 99999999999
    res       = None
    for i in range(0, len(input_lst), width*height):
        new_arr    = np.reshape(input_lst[i:i+width*height], (height,width))
        num_count  = np.bincount(new_arr.flatten())
        curr_zeros = num_count[0]
        if curr_zeros < min_zeros:
            min_zeros = curr_zeros
            res       = num_count[1]*num_count[2]
    return res

def part_2(input_lst):
    width     = 25
    height    = 6
    img       = np.full((height,width), -1,dtype=np.int8)
    for i in range(0, len(input_lst), width*height):
        new_arr = np.reshape(input_lst[i:i+width*height], (height,width))
        for j in range(0, height):
            for i in range(0, width):
                if img[j][i] == -1:
                    if new_arr[j][i] in [0,1]:
                        img[j][i] = new_arr[j][i]
    for j in img:
        print("".join(["⬛"*(int(i)==1)+"⬜"*(int(i)==0) for i in j]))


def main():
    print(part_1(read_input()))
    part_2(read_input())

if __name__ == "__main__":
    main()
