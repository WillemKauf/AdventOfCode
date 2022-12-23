import re
import heapq
import copy

def read_input():
    input_arr = []
    with open("input/input19.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            nums = re.findall(r'\d+', line)
            input_arr.append([int(i) for i in nums])
    return input_arr

class Inventory():
    def __init__(self, blueprint, robots={"ORE":1, "CLAY":0, "OBS":0, "GEO":0}, ores={"ORE":0, "CLAY":0, "OBS":0, "GEO":0}):
        self.blueprint = blueprint
        self.robots    = robots
        self.ores      = ores

    def __repr__(self):
        return repr((self.robots, self.ores))

    def __lt__(self, other):
        return (self.ores["GEO"], self.ores["OBS"], self.ores["CLAY"], self.ores["ORE"], self.robots["GEO"], self.robots["OBS"], self.robots["CLAY"], self.robots["ORE"]) > (other.ores["GEO"], other.ores["OBS"], other.ores["CLAY"], other.ores["ORE"], other.robots["GEO"], other.robots["OBS"], other.robots["CLAY"], other.robots["ORE"])

    def __deepcopy__(self, memo):
        return Inventory(self.blueprint, copy.deepcopy(self.robots), copy.deepcopy(self.ores))

    def update(self):
        for robot, num in self.robots.items():
            self.ores[robot] += num
            if robot != "GEO":
                self.ores[robot] = min(self.max_spend[robot], self.ores[robot])

    def get_maxs(self, time):
        self.max_ore  = max(self.blueprint[1], self.blueprint[2], self.blueprint[3], self.blueprint[5])
        self.max_clay = self.blueprint[4]
        self.max_obs  = self.blueprint[6]
        self.max_spend = {"ORE":self.max_ore*time, "CLAY":self.max_clay*time, "OBS":self.max_obs*time}

    def create_and_update(self, robot, time):
        self.get_maxs(time)
        create_flag = False
        if robot == "ORE":
            if self.ores["ORE"] >= self.blueprint[1] and self.ores["ORE"] < self.max_spend[robot]:
                self.ores["ORE"] -= self.blueprint[1]
                create_flag = True
        elif robot == "CLAY":
            if self.ores["ORE"] >= self.blueprint[2] and self.ores["CLAY"] < self.max_spend[robot]:
                self.ores["ORE"] -= self.blueprint[2]
                create_flag = True
        elif robot == "OBS":
            if self.ores["ORE"] >= self.blueprint[3] and self.ores["CLAY"] >= self.blueprint[4] and self.ores["OBS"] < self.max_spend[robot]:
                self.ores["ORE"]  -= self.blueprint[3]
                self.ores["CLAY"] -= self.blueprint[4]
                create_flag = True
        elif robot == "GEO":
            if self.ores["ORE"] >= self.blueprint[5] and self.ores["OBS"] >= self.blueprint[6]:
                self.ores["ORE"] -= self.blueprint[5]
                self.ores["OBS"] -= self.blueprint[6]
                create_flag = True
        self.update()
        if create_flag and robot != None:
            self.robots[robot] += 1

def encode_state(inv, time):
    return ("".join([str(i) for i in inv.robots.values()]), time)

def part1(input_arr):
    TIME = 24
    res  = 0
    for blueprint in input_arr:
        seen = {}
        time_seen = {}
        max_res = -1
        queue = [(Inventory(blueprint), TIME)]
        while len(queue):
            inv, time = heapq.heappop(queue)
            if time == 0:
                max_res = max(max_res, inv.ores["GEO"])
                continue
            for robot in ["GEO", "OBS", "CLAY", "ORE", None]:
                new_inv = copy.deepcopy(inv)
                new_inv.create_and_update(robot, time)
                state = encode_state(new_inv, time)
                if state in seen:
                    if all([seen[state][0] >= new_inv.ores["ORE"], seen[state][1] >= new_inv.ores["CLAY"], seen[state][2] >= new_inv.ores["OBS"], seen[state][3] >= new_inv.ores["GEO"]]):
                        continue
                seen[state] = (new_inv.ores["ORE"], new_inv.ores["CLAY"], new_inv.ores["OBS"], new_inv.ores["GEO"])
                if time in time_seen:
                    if time_seen[time] > new_inv.ores["GEO"]:
                        continue
                time_seen[time] = new_inv.ores["GEO"]
                heapq.heappush(queue, (new_inv, time-1))
        res += blueprint[0]*max_res
    return res

def part2(input_arr):
    TIME = 32
    res  = 1
    for blueprint in input_arr:
        time_seen = {}
        seen = {}
        max_res = -1
        queue = [(Inventory(blueprint), TIME)]
        while len(queue):
            inv, time = heapq.heappop(queue)
            if time == 0:
                max_res = max(max_res, inv.ores["GEO"])
                continue
            for robot in ["GEO", "OBS", "CLAY", "ORE", None]:
                new_inv = copy.deepcopy(inv)
                new_inv.create_and_update(robot, time)
                state = encode_state(new_inv, time)
                if state in seen:
                    if all([seen[state][0] >= new_inv.ores["ORE"], seen[state][1] >= new_inv.ores["CLAY"], seen[state][2] >= new_inv.ores["OBS"], seen[state][3] >= new_inv.ores["GEO"]]):
                        continue
                seen[state] = (new_inv.ores["ORE"], new_inv.ores["CLAY"], new_inv.ores["OBS"], new_inv.ores["GEO"])
                if time in time_seen:
                    if time_seen[time] > new_inv.ores["GEO"]:
                        continue
                time_seen[time] = new_inv.ores["GEO"]
                heapq.heappush(queue, (new_inv, time-1))
        res *= max_res
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr[:]))
    print(part2(input_arr[:3]))

if __name__ == "__main__":
    main()
