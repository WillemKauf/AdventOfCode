def read_input():
    input_lst = []
    with open("input/input9.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line.rstrip()])
    return input_lst

def part_1(input_lst):
    res = 0
    for seq in input_lst:
        repeat_counter = 1
        repeat_amount  = 1
        i = 0
        while i < len(seq):
            c = seq[i]
            if c == "(" and repeat_amount == 1:
                close_bracket_index = seq.index(")", i)
                repeat_counter, repeat_amount = [int(i) for i in "".join(seq[i+1:close_bracket_index]).split("x")]
                i = close_bracket_index
            else:
                res += repeat_amount
                repeat_counter -= 1
            if repeat_counter == 0:
                repeat_counter, repeat_amount = 1, 1
            i += 1
    return res

def part_2(input_lst):
    res = 0
    mul_lst = []
    for seq in input_lst:
        i = 0
        while i < len(seq):
            c = seq[i]
            if c == "(":
                close_bracket_index = seq.index(")", i)
                repeat_counter, repeat_amount = [int(i) for i in "".join(seq[i+1:close_bracket_index]).split("x")]
                for j in range(0, len(mul_lst)):
                    if mul_lst[j][1] > 0:
                        mul_lst[j][1] -= close_bracket_index+1-i
                mul_lst.append([repeat_amount, repeat_counter])
                i = close_bracket_index+1
                continue
            else:
                prod = 1
                for j in range(0, len(mul_lst)):
                    k, v = mul_lst[j]
                    if v > 0:
                        prod *= k
                res += prod
            i += 1
            for j in range(0, len(mul_lst)):
                if mul_lst[j][1] > 0:
                    mul_lst[j][1] -= 1
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
