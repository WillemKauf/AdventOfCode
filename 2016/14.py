from collections import deque
import hashlib

def read_input():
    input_str = []
    with open("input/input14.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def part_1(input_str):
    num_keys  = 0
    i         = 0
    poss_keys = deque([])
    seen_keys = set()
    while True:
        poss_key = hashlib.md5((input_str+str(i)).encode()).hexdigest()
        for j in range(0, len(poss_key)-4):
            char = poss_key[j]
            if all([c == poss_key[j] for c in poss_key[j:j+5]]):
                for k, info in enumerate(poss_keys):
                    key, c, index = info
                    if c == char and abs(index-i) <= 1000:
                        seen_keys.add(index)
                        if len(seen_keys) == 64:
                            return index
        for j in range(0, len(poss_key)-2):
            char = poss_key[j]
            if all([c == char for c in poss_key[j:j+3]]):
                poss_keys.append((poss_key, char, i))
                break
        i += 1

def part_2(input_str):
    num_keys  = 0
    i         = 0
    poss_keys = deque([])
    seen_keys = set()
    while True:
        to_hash  = (input_str+str(i)).encode()
        poss_key = hashlib.md5(to_hash).hexdigest().encode()
        for j in range(0, 2016):
            poss_key = hashlib.md5(poss_key).hexdigest().encode()
        for j in range(0, len(poss_key)-4):
            char = poss_key[j]
            if all([c == poss_key[j] for c in poss_key[j:j+5]]):
                for k, info in enumerate(poss_keys):
                    key, c, index = info
                    if c == char and abs(index-i) <= 1000:
                        seen_keys.add(index)
                        if len(seen_keys) == 64:
                            return index
        for j in range(0, len(poss_key)-2):
            char = poss_key[j]
            if all([c == char for c in poss_key[j:j+3]]):
                poss_keys.append((poss_key, char, i))
                break
        i += 1

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
