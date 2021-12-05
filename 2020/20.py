import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize,linewidth=400)

def read_input():
    input_dct = {}
    with open("input/input20.txt") as input_file:
        curr_grid = []
        curr_id   = None
        for line in input_file:
            line = line.rstrip()
            if line == "":
                input_dct[curr_id] = np.array(curr_grid)
                curr_grid          = []
                curr_id            = None
                continue
            elif curr_id == None:
                curr_id = line.split()[1][:-1]
            else:
                curr_grid.append([c for c in line])
        if curr_id != None:
            input_dct[curr_id] = np.array(curr_grid)
    block_dct = generate_all_blocks(input_dct)
    assert len(block_dct) == len(input_dct)
    return block_dct

def generate_all_blocks(input_dct):
    all_blocks = {block_id:[] for block_id in input_dct}
    for flip in [0, 1]:
        for rot in [0, 1, 2, 3]:
            for block_id, block in input_dct.items():
                all_blocks[block_id].append(create_new_block(np.copy(block), rot, flip))
    return all_blocks

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

def is_valid(block_a, block_b, side):
    if side == "R": #block_b is on right side of a
        side_a = block_a[:, -1]
        side_b = block_b[:,  0]
    elif side == "B": #block_b is on bottom side of a
        side_a = block_a[-1, :]
        side_b = block_b[0,  :]
    else:
        raise ValueError
    return all(side_a == side_b)

def recursive_check(block_array, used_blocks, i, j, block_dct, return_res=True):
    n = len(block_array)
    if j == n:
        res = int(used_blocks[0])*int(used_blocks[n-1])*int(used_blocks[-1])*int(used_blocks[-n])
        return res, block_array
    for block_id, blocks in block_dct.items():
        if block_id not in used_blocks:
            for block in blocks:
                if i > 0:
                    if not is_valid(block_array[j][i-1], block, "R"):
                        continue
                if j > 0:
                    if not is_valid(block_array[j-1][i], block, "B"):
                        continue
                block_array[j][i] = block
                new_i = (i+1) % n
                if new_i < i:
                    new_j = j+1
                else:
                    new_j = j
                res = recursive_check(block_array, used_blocks+[block_id], new_i, new_j, block_dct, return_res)
                if res != None:
                    return res
    return None

def part_1(block_dct):
    n = int(np.sqrt(len(block_dct)))
    return recursive_check([[None for _ in range(0, n)] for _ in range(0, n)], [], 0, 0, block_dct)

def part_2(block_array):
    n = len(block_array)
    sea_monster_text = [[None for _ in range(0, 18)] + ["#", None],
                        ["#", None, None, None, None, "#", "#", None, None, None, None, "#", "#", None, None, None, None, "#", "#", "#"],
                        [None, "#", None, None, "#", None, None, "#", None, None, "#", None, None, "#", None, None, "#", None, None, None]]

    for j in range(0, n):
        for i in range(0, n):
            #Remove left border
            if (0 <= i <= n-1):
                block_array[j][i] = np.delete(block_array[j][i], 0, axis=1)

            #Remove right border
            if (0 <= i <= n-1):
                block_array[j][i] = np.delete(block_array[j][i], -1, axis=1)

            #Remove top border
            if (0 <= j <= n-1):
                block_array[j][i] = np.delete(block_array[j][i], 0, axis=0)

            #Remove bottom border
            if (0 <= j <= n-1):
                block_array[j][i] = np.delete(block_array[j][i], -1, axis=0)


    new_block         = np.concatenate([np.concatenate(block_array[i][:], axis=1) for i in range(0, n)], axis=0)
    nx, ny            = new_block.shape
    dy                = len(sea_monster_text)
    dx                = len(sea_monster_text[0])
    sea_monster_count = 0
    for j in range(0, ny-dy):
        for i in range(0, nx-dx):
            is_flag = True
            for jj in range(0, dy):
                for ii in range(0, dx):
                    coord = new_block[j+jj][i+ii]
                    text  = sea_monster_text[jj][ii]
                    if text == None:
                        continue
                    if coord != text:
                        is_flag = False
            if is_flag:
                sea_monster_count += 1
    count_new_block = sum([1 for row in new_block for s in row if s == "#"])
    count_monster   = sum([1 for row in sea_monster_text for s in row if s == "#"])
    return count_new_block - sea_monster_count*count_monster

def main():
    block_dct = read_input()
    res_1, block_array = part_1(block_dct)
    print(res_1)
    print(part_2(block_array))

if __name__ == "__main__":
    main()
