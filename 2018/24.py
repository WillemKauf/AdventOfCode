import math
from copy import deepcopy
class Group:
    def __init__(self, lst, at_dct):
        self.num_units, self.hp, self.atk, self.ini, self.atk_type = lst
        self.at_dct = at_dct
        self.alive  = True

    def __str__(self):
        return f"{self.num_units}, with hp {self.hp}, attack {self.atk}, type {self.atk_type}, ini {self.ini}, alive {self.alive}, ats {[(k, v) for k, v in self.at_dct.items() if v != None]}"

    def eff_pow(self):
        return self.num_units*self.atk

def read_input():
    input_lst = []
    with open("input/input24.txt") as input_file:
        input_file.readline()
        curr_lst = []
        lines_of_interest = [0, 4, -6, -1]
        for line in input_file:
            line = line.rstrip()
            if line == "":
                continue
            if line == "Infection:":
                input_lst.append(curr_lst)
                curr_lst = []
                continue
            at_dct = {"cold":None, "slashing":None, "fire": None, "radiation":None, "bludgeoning":None}
            try:
                ats = line.split(" (")[1][:line.split(" (")[1].index(")")]
                ats = ats.split("; ")
                for at in ats:
                    at   = at.split(", ")
                    cond = at[0].split()[0]
                    for a in at:
                        at_dct[a.split()[-1]] = cond
            except:
                pass
            curr_lst.append(Group([int(line.split()[i]) for i in lines_of_interest]+[line.split()[-5]], at_dct))
    input_lst.append(curr_lst)
    return input_lst

mul_dct = {"immune":0, None:1, "weak":2}

def get_targets(g_a, g_b, g_a_name):
    target_dct = {}
    for i, g in enumerate(g_a):
        max_dmg      = -1
        poss_targets = set()
        for j, g2 in enumerate(g_b):
            if j in target_dct.values():
                continue
            dmg  = g.eff_pow()
            dmg *= mul_dct[g2.at_dct[g.atk_type]]
            if dmg > max_dmg:
                max_dmg      = dmg
                poss_targets = set([j])
            if dmg == max_dmg:
                poss_targets.add(j)
        if max_dmg != 0 and len(poss_targets):
            target_dct[(i, g_a_name)] = max(poss_targets, key=lambda j: (g_b[j].eff_pow(), g_b[j].ini))
    return target_dct

def simulate(immune, infect):
    it = 0
    while True:
        if it > 10000:
            return None, None
        immune         = sorted(immune, key=lambda g: (g.eff_pow(), g.ini), reverse=True)
        infect         = sorted(infect, key=lambda g: (g.eff_pow(), g.ini), reverse=True)
        immune_targets = get_targets(immune, infect, "immune")
        infect_targets = get_targets(infect, immune, "infect")
        combined_dict  = sorted({**immune_targets, **infect_targets}.items(), key = lambda k: immune[k[0][0]].ini if k[0][1] == "immune" else infect[k[0][0]].ini, reverse=True)
        for k, v in combined_dict:
            target = v
            if k[1] == "immune":
                attacker = immune[k[0]]
                if not attacker.alive:
                    continue
                defender = infect[target]
                dmg      = attacker.eff_pow()*mul_dct[defender.at_dct[attacker.atk_type]]
                infect[target].num_units -= dmg//defender.hp
                if infect[target].num_units <= 0:
                    infect[target].alive = False
            else:
                attacker = infect[k[0]]
                if not attacker.alive:
                    continue
                defender = immune[target]
                dmg      = attacker.eff_pow()*mul_dct[defender.at_dct[attacker.atk_type]]
                immune[target].num_units -= dmg//defender.hp
                if immune[target].num_units <= 0:
                    immune[target].alive = False
        immune = [g for g in immune if g.alive == True]
        infect = [g for g in infect if g.alive == True]
        if len(immune) == 0:
            return False, sum([g.num_units for g in infect])
        if len(infect) == 0:
            return True, sum([g.num_units for g in immune])
        it += 1
    return False, None

def part_1(input_lst):
    return simulate(*input_lst)[1]

def part_2(input_lst):
    immune, infect = input_lst
    l = 0
    r = int(1e12)
    while l < r:
        new_immune = deepcopy(immune)
        new_infect = deepcopy(infect)
        m = math.ceil((l+r)/2)
        for i in range(0, len(new_immune)):
            new_immune[i].atk += m
        res, n = simulate(new_immune, new_infect)
        if l == r-1:
            return n
        if res == True:
            r = m
        elif res == False:
            l = m
        else:
            l += 1
    return None

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
