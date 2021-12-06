def read_input():
    input_arr = []
    with open("input/input5.txt") as input_file:
        for line in input_file.readlines():
            input_arr.append(line.rstrip())
    return input_arr


def part_1(input_arr):
    def check_one(string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        is_vowel = lambda c : c in vowels
        return sum(map(is_vowel, list(string))) > 2

    def check_two(string):
        for i in range(1, len(string)):
            if(string[i] == string[i-1]):
                return True
        return False

    def check_three(string):
        bad_strings = ["ab", "cd", "pq", "xy"]
        for i in range(0, len(string)-1):
            if(string[i]+string[i+1]) in bad_strings:
                return False
        return True
    check_all = lambda string: all([check_one(string), check_two(string), check_three(string)])
    return sum(map(check_all, input_arr))

def part_2(input_arr):
    def check_one(string):
        hsh_map = {}
        for i in range(0, len(string)-1):
            pair = string[i]+string[i+1]
            if pair not in hsh_map:
                hsh_map[pair] = i
            else:
                if(hsh_map[pair] != i-1):
                    return True
        return False

    def check_two(string):
        for i in range(1, len(string)-1):
            if(string[i-1] == string[i+1]):
                return True
        return False
    check_all = lambda string: all([check_one(string), check_two(string)])
    return sum(map(check_all, input_arr))

def main():
    input_arr = read_input()
    print(part_1(input_arr))
    print(part_2(input_arr))

main()
