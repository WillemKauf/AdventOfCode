def read_input():
    input_lst = []
    with open("input/input16.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(",")
            for l in line:
                input_lst.append(l)
    return input_lst

def dance(input_lst, dct):
    n   = len(dct)
    for l in input_lst:
        c = l[0]
        if c == "s":
            s = int(l[1:])
            for k, v in dct.items():
                if v >= n-s:
                    dct[k] = v-n+s
                else:
                    dct[k] = v+s
        elif c == "x":
            a,b = [int(i) for i in l[1:].split("/")]
            p_a, p_b = None, None
            for k, v in dct.items():
                if v == a:
                    p_a = k
                elif v == b:
                    p_b = k
            dct[p_a], dct[p_b] = dct[p_b], dct[p_a]
        elif c == "p":
            a,b = l[1:].split("/")
            dct[a], dct[b] = dct[b], dct[a]
    return dct

def part_1(input_lst):
    dct = dance(input_lst, {chr(i):i-ord("a") for i in range(ord("a"), ord("p")+1)})
    return "".join(sorted(dct, key = lambda k: dct[k]))

def part_2(input_lst):
    dct  = {chr(i):i-ord("a") for i in range(ord("a"), ord("p")+1)}
    seen = {}
    n    = int(1e8)
    for i in range(0, n):
        dct     = dance(input_lst, dct)
        str_rep = "".join(sorted(dct, key = lambda k: dct[k]))
        if str_rep in seen:
            n_seen  = n % len(seen) - 1
            for k,v in seen.items():
                if v == n_seen:
                    return k
        else:
            seen[str_rep] = i
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
