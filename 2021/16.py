def read_input():
    input_str = []
    with open("input/input16.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def hex_to_bin(hex_str):
    bin_str = ""
    for c in hex_str:
        bin_str += bin(int(c, 16))[2:].zfill(4)
    return bin_str

bin_to_int = lambda x: int(x, 2)

def part_1(input_str):
    def recursive_parse(hex_str, i):
        version = bin_to_int(hex_str[i:i+3])
        res     = version
        i      += 3
        type_id = bin_to_int(hex_str[i:i+3])
        i      += 3
        if type_id == 4:
            bin_rep = ""
            flag    = True
            while flag:
                if hex_str[i] == "0":
                    flag = False
                bin_rep += hex_str[i+1:i+5]
                i += 5
            return i, version
        else:
            length_type_id = hex_str[i]
            i += 1
            if length_type_id == "0":
                num_bits = bin_to_int(hex_str[i:i+15])
                i += 15
                j  = i+num_bits
                while i < j:
                    i, curr_res = recursive_parse(hex_str, i)
                    res        += curr_res
            else:
                num_subpackets = bin_to_int(hex_str[i:i+11])
                i += 11
                for _ in range(0, num_subpackets):
                    i, curr_res = recursive_parse(hex_str, i)
                    res        += curr_res
        return i, res
    return recursive_parse(hex_to_bin(input_str), 0)[1]

def part_2(input_str):
    def recursive_parse(hex_str, i):
        version = bin_to_int(hex_str[i:i+3])
        res     = 0
        i      += 3
        type_id = bin_to_int(hex_str[i:i+3])
        i      += 3
        if type_id == 4:
            bin_rep = ""
            flag    = True
            while flag:
                if hex_str[i] == "0":
                    flag = False
                bin_rep += hex_str[i+1:i+5]
                i += 5
            return i, bin_to_int(bin_rep)
        else:
            vals = []
            length_type_id = hex_str[i]
            i += 1
            if length_type_id == "0":
                num_bits = bin_to_int(hex_str[i:i+15])
                i += 15
                j  = i+num_bits
                while i < j:
                    i, curr_res = recursive_parse(hex_str, i)
                    vals.append(curr_res)
            else:
                num_subpackets = bin_to_int(hex_str[i:i+11])
                i += 11
                for _ in range(0, num_subpackets):
                    i, curr_res = recursive_parse(hex_str, i)
                    vals.append(curr_res)
            if type_id == 0:
                res = sum(vals)
            elif type_id == 1:
                res = 1
                for v in vals:
                    res *= v
            elif type_id == 2:
                res = min(vals)
            elif type_id == 3:
                res = max(vals)
            elif type_id == 5:
                res = 1 if vals[0] > vals[1] else 0
            elif type_id == 6:
                res = 1 if vals[0] < vals[1] else 0
            elif type_id == 7:
                res = 1 if vals[0] == vals[1] else 0
        return i, res
    return recursive_parse(hex_to_bin(input_str), 0)[1]

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
