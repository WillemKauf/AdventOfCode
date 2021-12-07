def read_input():
    with open("input/input8.txt") as input_file:
        input_arr = [i.rstrip() for i in input_file]
    return input_arr

def part_1(input_arr):
    literal_sum = 0
    memory_sum  = 0
    for line in input_arr:
        literal_sum += len(list(line))
        i = 0
        while i < len(list(line)):
            if line[i] == "\\":
                if line[i+1] == "x":
                    memory_sum += 1
                    i += 4
                else:
                    memory_sum += 1
                    i += 2
            elif line[i] == "\"":
                i += 1
            else:
                memory_sum += 1
                i += 1
    return literal_sum - memory_sum

def part_2(input_arr):
    literal_sum = 0
    memory_sum  = 0
    for line in input_arr:
        literal_sum += len(list(line))
        i = 0
        new_line = "\""
        for char in line:
            if char == "\"":
                new_line += "\\\""
            elif char == "\\":
                new_line += "\\\\"
            else:
                new_line += char
        new_line += "\""
        memory_sum += len(new_line)
    return memory_sum - literal_sum

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

if __name__ == "__main__":
   main()
