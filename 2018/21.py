"""
#ip 4
r[0, 1, 2, 3, ip, 5]
 0 seti 123 0 5      -> r[5] = 123          ip = 0
 1 bani 5 456 5      -> r[5] = r[5] & 456   ip = 1
 2 eqri 5 72 5       -> r[5] = r[5] == 72   ip = 2
 3 addr 5 4 4        -> ip  += r[5]         ip = ip + r[5]
 4 seti 0 0 4        -> ip   = 0            ip = 0
 5 seti 0 7 5        -> r[5] = 0            ip = ???
 6 bori 5 65536 3    -> r[3] = r[5] | 65336 (2**16)
 7 seti 733884 6 5   -> r[5] = 733884
 8 bani 3 255 1      -> r[1] = r[3] & 255
 9 addr 5 1 5        -> r[5] = r[5] + r[1]
10 bani 5 16777215 5 -> r[5] = r[5] & 16777215 (2**24)
11 muli 5 65899 5    -> r[5] = r[5] * 65899
12 bani 5 16777215 5 -> r[5] = r[5] & 16777215
13 gtir 256 3 1      -> r[1] = 1 if 256 > r[3] else 0
14 addr 1 4 4        -> ip  += r[1]
15 addi 4 1 4        -> ip  += 1
16 seti 27 8 4       -> ip   = 27
17 seti 0 6 1        -> r[1] = 0
18 addi 1 1 2        -> r[2] = r[1] + 1
19 muli 2 256 2      -> r[2] = r[2] * 256
20 gtrr 2 3 2        -> r[2] = 1 if r[2] == r[3] else 0 (GOTO 28 if 1 else GOTO 7 with r[3]/256)
21 addr 2 4 4        -> ip  += r[2]
22 addi 4 1 4        -> ip  += 1
23 seti 25 4 4       -> ip   = 25
24 addi 1 1 1        -> r[1] = r[1] + 1
25 seti 17 8 4       -> ip   = 17
26 setr 1 7 3        -> r[3] = r[1]
27 seti 7 0 4        -> ip   = 7
28 eqrr 5 0 1        -> r[5] = r[0] == r[1] (CHECK r[0])
29 addr 1 4 4        -> ip += r[1]
30 seti 5 9 4        -> ip  = 5
"""

def part_1():
    seen    = set()
    r5      = 0
    while True:
        r3 = r5 | 0x10000
        r5 = 733884
        while True:
            r1 = r3 & 255
            r5 += r1
            r5 &= 2**24-1
            r5 *= 65899
            r5 &= 2**24-1
            if 256 > r3:
                return r5
            r3 //= 256

def part_2():
    seen   = set()
    r5     = 0
    it     = 0
    max_it = 3
    while True:
        r3 = r5 | 0x10000
        r5 = 733884
        while True:
            r1 = r3 & 255
            r5 += r1
            r5 &= 2**24-1
            r5 *= 65899
            r5 &= 2**24-1
            if 256 > r3:
                if r5 not in seen:
                    curr_res = r5
                    seen.add(r5)
                else:
                    it += 1
                    if it == max_it:
                        return curr_res
                break
            r3 //= 256

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()
