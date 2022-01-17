from collections import defaultdict
import itertools

class Cart:
    def __init__(self, pos, direc, counter=0):
        self.pos      = pos
        self.direc    = direc
        self.counter  = counter
        self.removed  = False

    def __str__(self):
        return f"{self.get_pos()}, ({int(self.direc.real)}, {int(self.direc.imag)}), {self.counter}"

    def get_pos(self):
        return int(self.pos.real), int(self.pos.imag)

    def update_pos(self):
        self.pos     += self.direc

    def update_dir(self, c):
        if c == "\\":
            if int(self.direc.real):
                self.direc *= complex(0, 1)
            else:
                self.direc *= complex(0, -1)
        elif c == "/":
            if int(self.direc.real):
                self.direc *= complex(0, -1)
            else:
                self.direc *= complex(0, 1)
        elif c == "+":
            self.counter += 1
            n_seen = (self.counter-1)%3
            if n_seen == 0:
                self.direc *= complex(0, -1)
            elif n_seen == 1:
                pass
            elif n_seen == 2:
                self.direc *= complex(0, 1)
        return int(self.direc.real), int(self.direc.imag)

def unit_tests():
    print("Running Unit Tests")
    assert Cart(complex(0,0), complex(1,  0)).update_dir("\\") == (0,  1)
    assert Cart(complex(0,0), complex(0, -1)).update_dir("\\") == (-1, 0)
    assert Cart(complex(0,0), complex(-1, 0)).update_dir("\\") == (0, -1)
    assert Cart(complex(0,0), complex(0,  1)).update_dir("\\") == (1,  0)

    assert Cart(complex(0,0), complex(1,  0)).update_dir("/") == (0, -1)
    assert Cart(complex(0,0), complex(0, -1)).update_dir("/") == (1,  0)
    assert Cart(complex(0,0), complex(-1, 0)).update_dir("/") == (0,  1)
    assert Cart(complex(0,0), complex(0,  1)).update_dir("/") == (-1, 0)

    for i in range(0, 1000):
        if i % 3 == 0:
            assert Cart(complex(0,0), complex(1,  0), i).update_dir("+") == (0, -1)
            assert Cart(complex(0,0), complex(0, -1), i).update_dir("+") == (-1, 0)
            assert Cart(complex(0,0), complex(-1, 0), i).update_dir("+") == (0,  1)
            assert Cart(complex(0,0), complex(0,  1), i).update_dir("+") == (1,  0)
        elif i % 3 == 1:
            assert Cart(complex(0,0), complex(1,  0), i).update_dir("+") == (1,  0)
            assert Cart(complex(0,0), complex(0, -1), i).update_dir("+") == (0, -1)
            assert Cart(complex(0,0), complex(-1, 0), i).update_dir("+") == (-1, 0)
            assert Cart(complex(0,0), complex(0,  1), i).update_dir("+") == (0,  1)
        elif i % 3 == 2:
            assert Cart(complex(0,0), complex(1,  0), i).update_dir("+") == (0,  1)
            assert Cart(complex(0,0), complex(0, -1), i).update_dir("+") == (1,  0)
            assert Cart(complex(0,0), complex(-1, 0), i).update_dir("+") == (0, -1)
            assert Cart(complex(0,0), complex(0,  1), i).update_dir("+") == (-1, 0)

def read_input():
    input_lst = []
    with open("input/input13.txt") as input_file:
        for line in input_file:
            input_lst.append([i for i in line[:-1]])
    return input_lst

def part_1(input_lst):
    carts  = []
    ddir   = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    dir_mp = {"v":complex(0, 1), ">":complex(1, 0), "<":complex(-1, 0), "^":complex(0, -1)}
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            c = input_lst[j][i]
            if c in ["v", ">", "<", "^"]:
                carts.append(Cart(complex(i,j), dir_mp[c]))
    while True:
        for i, cart in enumerate(carts):
            cart.update_pos()
            x, y = cart.get_pos()
            c = input_lst[y][x]
            cart.update_dir(c)
            seen = set()
            for n_cart in carts:
                pos = n_cart.get_pos()
                if pos in seen:
                    return f"{pos[0]},{pos[1]}"
                seen.add(pos)
        carts = sorted(carts, key=lambda c: c.get_pos())

def part_2(input_lst):
    carts  = []
    ddir   = [prod for prod in itertools.product([-1, 0, 1], repeat=2) if abs(prod[0])+abs(prod[1]) == 1]
    dir_mp = {"v":complex(0, 1), ">":complex(1, 0), "<":complex(-1, 0), "^":complex(0, -1)}
    for j in range(0, len(input_lst)):
        for i in range(0, len(input_lst[j])):
            c = input_lst[j][i]
            if c in ["v", ">", "<", "^"]:
                carts.append(Cart(complex(i,j), dir_mp[c]))
    n_carts   = len(carts)
    n_removed = 0
    while True:
        for i, cart in enumerate(carts):
            if cart.removed:
                continue
            cart.update_pos()
            x, y = cart.get_pos()
            c = input_lst[y][x]
            cart.update_dir(c)
            seen = defaultdict(list)
            for j, n_cart in enumerate(carts):
                if n_cart.removed:
                    continue
                pos = n_cart.get_pos()
                seen[pos].append(j)
            for p, s_l in seen.items():
                if len(s_l) > 1:
                    for c_n in s_l:
                        carts[c_n].removed = True
                        n_removed += 1
        carts = sorted(carts, key=lambda c: c.get_pos())
        if n_removed == n_carts-1:
            for n_cart in carts:
                if not n_cart.removed:
                    return f"{n_cart.get_pos()[0]},{n_cart.get_pos()[1]}"
def main():
    #unit_tests()
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
