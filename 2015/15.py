import re

class Cookie:
    def __init__(self, name, cap, dur, fla, tex, cal):
        self.name = name
        self.cap  = int(cap)
        self.dur  = int(dur)
        self.fla  = int(fla)
        self.tex  = int(tex)
        self.cal  = int(cal)
        self.lst  = [self.cap, self.dur, self.fla, self.tex]

def read_input():
    cookie_arr = []
    with open("input/input15.txt", "r") as i_f:
        regex = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
        for line in i_f:
            line = line.rstrip()
            cookie_arr.append(Cookie(*re.match(regex, line).groups()))
    return cookie_arr

def part_1(cookie_arr, flag=False):
    max_val = -1
    for l in range(0, 101):
        for k in range(0, 100-l):
            for j in range(0, 100-l-k):
                i = 100-l-k-j
                w = [i,j,k,l]
                curr_val = 1
                for q in range(0, 4):
                    curr_w = 0
                    for c in range(0, len(cookie_arr)):
                        curr_w += w[c]*cookie_arr[c].lst[q]
                    curr_val *= curr_w
                    if curr_w < 0:
                        curr_val = -1
                        break
                tol_cal = 0
                for c in range(0, len(cookie_arr)):
                    tol_cal += w[c]*cookie_arr[c].cal
                if tol_cal != 500 and flag:
                    continue
                max_val = max(curr_val, max_val)
    return max_val

def part_2(cookie_arr):
    return part_1(cookie_arr, True)

def main():
    cookie_arr = read_input()
    print(part_1(cookie_arr))
    print(part_2(cookie_arr))

if __name__ == "__main__":
   main()
