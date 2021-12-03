def read_input():
    input_lst = []
    with open("input/input15.txt") as input_file:
        for line in input_file:
            for c in line.rstrip().split(","):
                input_lst.append(int(c))
    return input_lst

def solve_puzzle(input_lst, num_turns):
    hsh_map         = {val:[None, ind+1] for ind, val in enumerate(input_lst)}
    last_spoken_num = input_lst[-1]
    n               = len(input_lst)
    for i in range(n, num_turns):
        last_times_spoken = hsh_map[last_spoken_num]
        if last_times_spoken[0] == None:
            spoken_num = 0
        else:
            spoken_num = last_times_spoken[1]-last_times_spoken[0]

        if spoken_num not in hsh_map:
            hsh_map[spoken_num] = [None, i+1]
        else:
            hsh_map[spoken_num][0], hsh_map[spoken_num][1] = hsh_map[spoken_num][1], i+1
        last_spoken_num = spoken_num
    return last_spoken_num

def part_1(input_lst):
    return solve_puzzle(input_lst, 2020)

def part_2(input_lst):
    return solve_puzzle(input_lst, 30000000)

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

