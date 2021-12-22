def read_input():
    input_lst = []
    with open("input/input17.txt") as input_file:
        for line in input_file:
            line = line.rstrip()[13:]
            line = line.split(", ")
            x_min, x_max = [int(i) for i in line[0].split("=")[1].split("..")]
            y_min, y_max = [int(i) for i in line[1].split("=")[1].split("..")]
            input_lst.append((x_min, x_max))
            input_lst.append((y_min, y_max))
    return input_lst


def sign(x):
    return bool(x > 0) - bool(x < 0)

def func(dx, dy, t):
    if sign(dx) > 0:
        x = sum([i+1 for i in range(max(dx-t, 0), dx)])
    else:
        x = sum([i for i in range(dx, min(dx+t, 0))])
    y = sum([i+1 for i in range(dy-t, dy)])
    return x,y

def part_1(input_lst):
    (x_min, x_max), (y_min, y_max) = input_lst
    x_0, y_0 = 0, 0
    for dy in range(abs(y_min), 1, -1):
        curr_h = dy*(dy+1)//2
        for dx in range(1, x_max):
            max_x = sign(dx)*(abs(dx)*(abs(dx)+1)//2)
            if x_min <= max_x:
                min_t = x_min//dx
                t     = min_t
                x,y = func(dx,dy,t)
                while y > y_min:
                    t += 1
                    x,y = func(dx,dy,t)
                    if y_min <= y <= y_max and x_min <= x <= x_max:
                        return curr_h

def part_2(input_lst):
    (x_min, x_max), (y_min, y_max) = input_lst
    x_0, y_0 = 0, 0
    res = 0
    for dy in range(-abs(y_min)-1, abs(y_min)+1):
        for dx in range(1, x_max+1):
            max_x = sign(dx)*(abs(dx)*(abs(dx)+1)//2)
            if x_min <= max_x:
                min_t = x_min//dx
                t     = min_t
                x,y = func(dx,dy,t)
                while y >= y_min:
                    if y_min <= y <= y_max and x_min <= x <= x_max:
                        res += 1
                        break
                    t += 1
                    x,y = func(dx,dy,t)
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
