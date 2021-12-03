import numpy as np

def read_input():
    input_lst = []
    with open("input/input17.txt") as input_file:
        for line in input_file:
            curr_lst = []
            for c in line.rstrip():
                curr_lst.append(c)
            input_lst.append(curr_lst)
    return input_lst

def part_1(input_lst):
    len_y = len(input_lst)
    len_x = len(input_lst[0])
    state = np.empty([1, len_x, len_y], dtype=np.int32)

    for j in range(0, len_y):
        for i in range(0, len_x):
            if input_lst[j][i] == ".":
                state[0][j][i] = 0
            else:
                state[0][j][i] = 1

    def get_neighbours(state, i, j, k):
        ddir = [-1, 0, 1]
        neighbours = []
        len_z, len_y, len_x = state.shape
        for dk in ddir:
            for dj in ddir:
                for di in ddir:
                    if (dk, dj, di) == (0,0,0):
                        continue
                    kk, jj, ii = k+dk, j+dj, i+di
                    if 0 <= kk < len_z and 0 <= jj < len_y and 0 <= ii < len_x:
                        neighbours.append(state[kk][jj][ii])
        return neighbours

    def change_state(cube, neighbours):
        if cube == 1:
            if sum(neighbours) in [2,3]:
                return 1
            else:
                return 0
        else:
            if sum(neighbours) == 3:
                return 1
            else:
                return 0

    num_iters = 6
    for t in range(0, num_iters):
        for dim in range(0, 3):
            state = np.insert(state, 0,                0, axis=dim)
            state = np.insert(state, state.shape[dim], 0, axis=dim)
        new_state           = state.copy()
        new_z, new_y, new_x = new_state.shape
        for k in range(0, new_z):
            for j in range(0, new_y):
                for i in range(0, new_x):
                    cube               = state[k][j][i]
                    neighbours         = get_neighbours(state, i,j,k)
                    new_state[k][j][i] = change_state(cube, neighbours)
        state = new_state
    return np.sum(state)

def part_2(input_lst):
    len_y = len(input_lst)
    len_x = len(input_lst[0])
    state = np.empty([1, 1, len_x, len_y], dtype=np.int32)

    for j in range(0, len_y):
        for i in range(0, len_x):
            if input_lst[j][i] == ".":
                state[0][0][j][i] = 0
            else:
                state[0][0][j][i] = 1

    def get_neighbours(state, i, j, k, l):
        ddir = [-1, 0, 1]
        neighbours = []
        len_w, len_z, len_y, len_x = state.shape
        for dl in ddir:
            for dk in ddir:
                for dj in ddir:
                    for di in ddir:
                        if (dl, dk, dj, di) == (0,0,0,0):
                            continue
                        ll, kk, jj, ii = l+dl, k+dk, j+dj, i+di
                        if 0 <= ll < len_w and 0 <= kk < len_z and 0 <= jj < len_y and 0 <= ii < len_x:
                            neighbours.append(state[ll][kk][jj][ii])
        return neighbours

    def change_state(cube, neighbours):
        if cube == 1:
            if sum(neighbours) in [2,3]:
                return 1
            else:
                return 0
        else:
            if sum(neighbours) == 3:
                return 1
            else:
                return 0

    num_iters = 6
    for t in range(0, num_iters):
        for dim in range(0, 4):
            state = np.insert(state, 0,                0, axis=dim)
            state = np.insert(state, state.shape[dim], 0, axis=dim)
        new_state = state.copy()
        new_w, new_z, new_y, new_x = new_state.shape
        for l in range(0, new_w):
            for k in range(0, new_z):
                for j in range(0, new_y):
                    for i in range(0, new_x):
                        cube                  = state[l][k][j][i]
                        neighbours            = get_neighbours(state, i,j,k,l)
                        new_state[l][k][j][i] = change_state(cube, neighbours)
        state = new_state
    return np.sum(state)

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

