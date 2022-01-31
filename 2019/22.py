from collections import deque

def read_input():
    input_lst = []
    with open("input/input22.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            if len(line) == 2:
                line[1] = int(line[1])
                input_lst.append(line)
            else:
                if line[1] == "into":
                    input_lst.append(line[3])
                else:
                    input_lst.append([line[0], int(line[-1])])
    return input_lst

def part_1(input_lst):
    n     = 10007
    cards = deque(range(n))
    for cmd in input_lst:
        if cmd == "stack":
            cards.reverse()
        elif cmd[0] == "cut":
            cards.rotate(-cmd[1])
        elif cmd[0] == "deal":
            new_cards = deque(range(n))
            while len(cards):
                new_cards.popleft()
                new_cards.appendleft(cards.popleft())
                new_cards.rotate(-cmd[1])
            cards = new_cards
    return cards.index(2019)

def part_2(input_lst):
    """
    f(x) = (ax+b)%n
    Deal into new stack   -> card at pos x is now at n-x-1,   f(x) = (-x-1)%n, a=-1, b=-1
    cut N cards           -> card at pos x is now at (x-N)%n, f(x) = (x-N)%n,  a=1,  b=-N
    deal with increment N -> card at pos x is now at (N*x)%n, f(x) = (N*x)%n,  a=N,  b=0
    Not gonna lie, I still don't understand modular arithmetic, and I likely never will.
    Solution unashamedly cobbled together from a multitude of sources.
    """
    n = 119315717514047
    k = 101741582076661
    x = 2020
    a = 1
    b = 0
    for cmd in input_lst:
        if cmd == "stack":
            a = (-a)%n
            b = (b+a)%n
        elif cmd[0] == "cut":
            N  = cmd[1]
            b += (a*N)%n
        elif cmd[0] == "deal":
            N     = cmd[1]
            N_exp = pow(N, n-2, n)
            a     = (a*N_exp)%n
    A = pow(a,k,n)
    B = (b*(1-A)*(pow(1-a, n-2, n)%n))%n
    return (A*x+B)%n

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
