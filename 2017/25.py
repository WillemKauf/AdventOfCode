from collections import defaultdict

def read_input():
    #Yeah, I'm not parsing that.
    pass

def part_1(input_lst):
    n_steps = 12629077
    state   = "A"
    tape    = defaultdict(int)
    pos     = 0
    for _ in range(0, n_steps):
        if state == "A":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
            else:
                tape[pos] = 0
                pos -= 1
            state = "B"
        elif state == "B":
            if tape[pos] == 0:
                tape[pos] = 0
                pos += 1
                state = "C"
            else:
                tape[pos] = 1
                pos -= 1
        elif state == "C":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "D"
            else:
                tape[pos] = 0
                pos -= 1
                state = "A"
        elif state == "D":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "E"
            else:
                tape[pos] = 1
                pos -= 1
                state = "F"
        elif state == "E":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "A"
            else:
                tape[pos] = 0
                pos -= 1
                state = "D"
        elif state == "F":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "A"
            else:
                tape[pos] = 1
                pos -= 1
                state = "E"
    return sum(tape.values())

def main():
    print(part_1(read_input()))

if __name__ == "__main__":
    main()
