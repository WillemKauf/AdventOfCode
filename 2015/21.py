from collections import defaultdict, namedtuple
import itertools

class Boss:
    def __init__(self, input_lst):
        self.hp, self.dmg, self.armor = input_lst

class Player:
    def __init__(self, wep, armor, rings):
        self.hp    = 100
        self.dmg   = 0
        self.armor = 0
        self.parse([wep, armor, *rings])

    def parse(self, items):
        for item in items:
            self.dmg   += item.dmg
            self.armor += item.armor

def read_input():
    input_lst = []
    shop_dct  = defaultdict(list)
    with open("input/input21.txt") as input_file:
        for line in input_file:
            input_lst.append(int(line.rstrip().split()[-1]))

    with open("input/input21_shop.txt") as input_file:
        Item = namedtuple("Item", ["name", "cost", "dmg", "armor"])
        curr_attr = None
        for line in input_file:
            line = line.rstrip().split()
            if not len(line):
                continue
            if line[0][-1] == ":":
                curr_attr = line[0][:-1]
                continue
            name, cost, dmg, armor = line
            shop_dct[curr_attr].append(Item(name, int(cost), int(dmg), int(armor)))
    shop_dct["Armor"].append(Item("None", 0, 0, 0))
    shop_dct["Rings"].append(Item("None1", 0, 0, 0))
    shop_dct["Rings"].append(Item("None2", 0, 0, 0))
    return input_lst, shop_dct

def sim_battle(player, boss):
    player_turn = True
    while player.hp or boss.hp:
        if player_turn:
            boss.hp -= max(player.dmg - boss.armor, 1)
            if boss.hp <= 0:
                return True
        else:
            player.hp -= max(boss.dmg - player.armor, 1)
            if player.hp <= 0:
                return False
        player_turn = not player_turn
    return False

def part_1(input_lst, shop_dct):
    weps       = shop_dct["Weapons"]
    armors     = shop_dct["Armor"]
    rings      = shop_dct["Rings"]
    poss_rings = [c for c in itertools.combinations(rings, 2)]
    min_gold   = int(1e12)
    for wep in weps:
        for armor in armors:
            for rings in poss_rings:
                curr_gold = wep.cost + armor.cost + rings[0].cost + rings[1].cost
                if sim_battle(Player(wep, armor, rings), Boss(input_lst)):
                    min_gold = min(min_gold, curr_gold)
    return min_gold

def part_2(input_lst, shop_dct):
    weps       = shop_dct["Weapons"]
    armors     = shop_dct["Armor"]
    rings      = shop_dct["Rings"]
    poss_rings = [c for c in itertools.combinations(rings, 2)]
    max_gold   = -1
    for wep in weps:
        for armor in armors:
            for rings in poss_rings:
                curr_gold = wep.cost + armor.cost + rings[0].cost + rings[1].cost
                if not sim_battle(Player(wep, armor, rings), Boss(input_lst)):
                    max_gold = max(max_gold, curr_gold)
    return max_gold

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
