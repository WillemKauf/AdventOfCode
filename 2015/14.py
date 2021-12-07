import re

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name      = name
        self.speed     = int(speed)
        self.fly_time  = int(fly_time)
        self.rest_time = int(rest_time)
        self.state_t   = int(fly_time)
        self.state     = "Flying"
        self.dist      = 0
        self.points    = 0

    def update_state(self):
        if self.state == "Flying":
            self.dist += self.speed
        self.state_t -= 1
        if self.state_t == 0:
            if self.state == "Flying":
                self.state = "Resting"
                self.state_t = self.rest_time
            else:
                self.state = "Flying"
                self.state_t = self.fly_time

def read_input():
    r_l = []
    with open("input/input14.txt") as i_f:
        regex = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
        for line in i_f:
            line = line.rstrip()
            r_l.append(Reindeer(*(re.match(regex, line).groups())))
    return r_l

def part_1(r_l):
    final_t = 2503
    max_dist = 0
    max_reindeer = None

    for reindeer in r_l:
        dist = 0
        t = 0
        while(t < final_t):
            fly_dt = min(final_t-t, reindeer.fly_time)
            t += fly_dt
            dist += fly_dt*reindeer.speed
            rest_dt = min(final_t-t, reindeer.rest_time)
            t += rest_dt
        if dist > max_dist:
            max_dist = dist
            max_reindeer = reindeer.name
    return max_dist

def part_2(r_l):
    final_t = 2503
    t = 0
    while (t < final_t):
        for i in range(0, len(r_l)):
            reindeer = r_l[i]
            reindeer.update_state()
        max_dist = max(r_l, key = lambda r : r.dist).dist
        for reindeer in r_l:
            if reindeer.dist == max_dist:
                reindeer.points += 1
        t += 1
    max_points = max(r_l, key = lambda r : r.points).points
    return max_points

def main():
    r_l = read_input()
    print(part_1(r_l))
    print(part_2(r_l))

if __name__ == "__main__":
   main()
