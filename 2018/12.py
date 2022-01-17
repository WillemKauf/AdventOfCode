from collections import defaultdict

def read_input():
    state, input_dct = defaultdict(int), {}
    mp = {".":0, "#":1}
    with open("input/input12.txt") as input_file:
        state = defaultdict(int, {i:mp[v] for i, v in enumerate(input_file.readline().rstrip().split(": ")[1])})
        input_file.readline()
        for line in input_file:
            line = line.rstrip().split(" => ")
            a    = "".join([str(mp[c]) for c in line[0]])
            b    = mp[line[1]]
            input_dct[a] = b
    return state, input_dct

def part_1(state, input_dct):
    n_iter = 20
    for _ in range(0, n_iter):
        n         = len(state)
        new_state = defaultdict(int)
        for i in range(-5, n+5):
            s = "".join([str(state[j]) for j in range(i-2, i+3)])
            new_state[i] = input_dct[s]
        state = new_state
    return sum([k for k in state if state[k] == 1])

def part_2(state, input_dct):
    n_iter = 50000000000
    s_history = []
    d_history = []
    for _ in range(0, n_iter):
        n         = len(state)
        score     = sum([k for k in state if state[k] == 1])
        s_history.append(score)
        new_state = defaultdict(int)
        for i in range(-5, n+5):
            s = "".join([str(state[j]) for j in range(i-2, i+3)])
            new_state[i] = input_dct[s]
        state = new_state
        n_score = sum([k for k in state if state[k] == 1])
        d_score = n_score - score
        d_history.append(d_score)
        if len(d_history) > 10:
            if all([d == d_history[-1] for d in d_history[-10:]]):
                break
    score = s_history[-10] + (n_iter-len(s_history[:-10]))*d_history[-1]
    return score


def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
