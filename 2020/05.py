def read_input():
    input_lst = []
    with open("input/input5.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip())
    return input_lst

def part_1(input_lst):
    max_res = 0
    for s in input_lst:
        row = s[:7]
        col = s[7:]
        row = row.replace("F", "0")
        row = row.replace("B", "1")
        col = col.replace("L", "0")
        col = col.replace("R", "1")
        row = int(row, 2)
        col = int(col, 2)
        max_res = max(max_res, row*8 + col)
    return max_res

def part_2(input_lst):
    seen_ids = []
    for s in input_lst:
        row = s[:7]
        col = s[7:]
        row = row.replace("F", "0")
        row = row.replace("B", "1")
        col = col.replace("L", "0")
        col = col.replace("R", "1")
        row = int(row, 2)
        col = int(col, 2)
        seen_ids.append(row*8 + col)
    for i in range(0, max(seen_ids)):
        if i not in seen_ids:
            if i+1 in seen_ids and i-1 in seen_ids:
                return i

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

