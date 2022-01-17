from collections import deque

def read_input():
    input_num = []
    with open("input/input14.txt") as input_file:
        for line in input_file:
            input_num = int(line.rstrip())
    return input_num

def get_nums(num):
    if num == 0:
        return deque([0])
    nums = deque([])
    while num != 0:
        nums.appendleft(num % 10)
        num = num // 10
    return nums

def part_1(input_num):
    recipes = deque([3,7])
    p1      = 0
    p2      = 1
    scores  = ""
    n       = len(recipes)
    while True:
        r1          = recipes[p1]
        r2          = recipes[p2]
        new_recipes = r1 + r2
        for r in get_nums(new_recipes):
            recipes.append(r)
            n += 1
            if n > input_num:
                scores += str(r)
            if n == input_num+10:
                return scores
        p1 = (p1+1+r1)%n
        p2 = (p2+1+r2)%n

def part_2(input_num):
    recipes = "37"
    p1      = 0
    p2      = 1
    n_num   = len(str_num)
    while True:
        r1          = int(recipes[p1])
        r2          = int(recipes[p2])
        new_recipes = str(r1 + r2)
        recipes    += new_recipes
        n           = len(recipes)
        if str_num in recipes[-n_num-1:]:
            return n-n_num-len(new_recipes)+1
        p1 = (p1+1+r1)%n
        p2 = (p2+1+r2)%n

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
