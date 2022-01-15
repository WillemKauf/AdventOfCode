from collections import defaultdict

def read_input():
    input_lst = []
    with open("input/input4.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split()
            time = line[0][1:] + "-" + line[1][:-1]
            if len(line) == 4:
                input_lst.append([time, line[2]])
            else:
                input_lst.append([time, int(line[3][1:]), "begins"])
    return sorted(input_lst, key=lambda l: l[0])

def datetime_comp(datetime):
    day, time      = datetime[:-6], datetime[-5:]
    hr, m          = [int(i) for i in time.split(":")]
    return day, hr, m

def part_1(input_lst):
    dct      = defaultdict(dict)
    prev_day = None
    for cmd in input_lst:
        if len(cmd) == 3:
            datetime, g, _ = cmd
            day, hr, m = datetime_comp(datetime)
            if day != prev_day:
                dct[day][g] = []
        else:
            datetime, a               = cmd
            prev_day, prev_hr, prev_m = datetime_comp(prev_datetime)
            day, hr, m                = datetime_comp(datetime)
            if day != prev_day:
                dct[day][g] = []
            if a == "wakes":
                dct[day][g].append([prev_m, m])
        prev_datetime = datetime

    sleep_dct = defaultdict(int)
    seen_dct  = defaultdict(dict)
    for d, l in dct.items():
        for g, dt in l.items():
            sleep_dct[g] += sum([m[1] - m[0] for m in dt])
            for m in dt:
                for t in range(m[0], m[1]):
                    if t not in seen_dct[g]:
                        seen_dct[g][t] = 0
                    seen_dct[g][t] += 1
    max_g  = sorted(sleep_dct.items(), key=lambda p:p[1],reverse=True)[0][0]
    max_m  = sorted(seen_dct[max_g].items(), key=lambda p:p[1],reverse=True)[0][0]

    max_g2 = -1
    max_m2 = -1
    max_n2 = -1
    for g, l in seen_dct.items():
        for m, n in l.items():
            if n > max_n2:
                max_n2 = n
                max_m2 = m
                max_g2 = g
    return max_g*max_m, max_g2*max_m2

def main():
    p1, p2 = part_1(read_input())
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
