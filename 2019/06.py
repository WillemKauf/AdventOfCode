def read_input():
    input_dct = {}
    with open("input/input6.txt") as input_file:
        for line in input_file:
            a,b = line.rstrip().split(")")
            input_dct[b] = a
            if a not in input_dct:
                input_dct[a] = None
    return input_dct

def part_1(input_dct):
    dp = {}
    def recursive_dive(node, dp, depth=0):
        if node in dp:
            return dp[node]+depth
        parent = input_dct[node]
        if parent == None:
            return depth
        return recursive_dive(parent, dp, depth+1)

    res = 0
    for node in input_dct.keys():
        n_res = recursive_dive(node, dp)
        dp[node] = n_res
        res += n_res
    return res

def part_2(input_dct):
    dp = {}
    def recursive_dive(node, dp, path=[], depth=0):
        if node in dp:
            return dp[node][0]+depth, path+dp[node][1]
        parent = input_dct[node]
        if parent == None:
            return depth, path+[node]
        return recursive_dive(parent, dp, path+[node], depth+1)

    for node in input_dct.keys():
        n_res, path = recursive_dive(node, dp)
        dp[node] = (n_res, path)
        if "YOU" in dp and "SAN" in dp:
            intersect = [i for i in dp["YOU"][1] if i in dp["SAN"][1]][0]
            return (dp["YOU"][1].index(intersect)-1)+(dp["SAN"][1].index(intersect)-1)
    return None


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
