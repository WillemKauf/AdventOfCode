import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize,linewidth=400)

def read_input():
    input_dct = {}
    with open("input/input21.txt") as input_file:
        for line in input_file:
            line  = line.replace(".", "0").replace("#", "1")
            line  = line.rstrip().split(" => ")
            a     = line[0]
            b     = line[1]
            for t in get_transforms(a):
                input_dct[t] = b
    return input_dct

def get_transforms(string):
    lst = []
    array = str_to_array(string)
    for flip in [0,1]:
        for rot in [0,1,2,3]:
            yield array_to_str(create_new_block(np.copy(array), rot, flip))

def str_to_array(string):
    split_string = string.split("/")
    lst_str = []

    for j in split_string:
        curr_lst = []
        for i in j:
            curr_lst.append(int(i))
        lst_str.append(curr_lst)
    return np.array(lst_str)

def array_to_str(array):
    string = ""
    for j in array:
        if len(string):
            string += "/"
        for i in j:
            string += str(i)
    return string

def rotate_block(block, rot):
    if rot == 0:
        return block
    else:
        return np.rot90(block, rot, axes=(1,0))

def flip_block(block, flip):
    if flip == 0:
        return block
    else:
        return np.flip(block, 1)

def create_new_block(block, rot, flip):
    return flip_block(rotate_block(block, rot), flip)

def part_1(input_dct, n_iter=5):
    grid = str_to_array("010/001/111")
    for _ in range(0, n_iter):
        x = grid.shape[0]
        if x % 2 == 0:
            split_fac = x//2
        else:
            split_fac = x//3
        n_grid = None
        flag_two = False
        for s_grid in np.split(grid, split_fac):
            flag = False
            for ss_grid in np.split(s_grid, split_fac, axis=1):
                str_grid = array_to_str(ss_grid)
                p_grid   = str_to_array(input_dct[str_grid])
                if flag == False:
                    curr_grid = p_grid
                    flag = True
                else:
                    curr_grid = np.concatenate((curr_grid, p_grid), axis=1)
            if flag_two == False:
                n_grid = curr_grid
                flag_two = True
            else:
                n_grid = np.concatenate((n_grid, curr_grid), axis=0)
        grid = n_grid
    return np.count_nonzero(grid)

def main():
    print(part_1(read_input()))
    print(part_1(read_input(), 18))

if __name__ == "__main__":
    main()
