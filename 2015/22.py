from copy import deepcopy
import heapq

class Player:
    def __init__(self):
        self.hp         = 50
        self.armor      = 0
        self.mana       = 500
        self.mana_spent = 0
        self.state      = {"Shield":None, "Recharge":None}
        self.spell_lst  = {magic_missile:53, drain:73, shield:113, poison:173, recharge:229}

    def update_state(self):
        if self.state["Shield"] != None:
            self.armor = 7
            self.state["Shield"] -= 1
            if self.state["Shield"] == 0:
                self.state["Shield"] = None
                self.armor = 0
        if self.state["Recharge"] != None:
            self.mana += 101
            self.state["Recharge"] -= 1
            if self.state["Recharge"] == 0:
                self.state["Recharge"] = None

class Boss:
    def __init__(self):
        with open("input/input22.txt") as input_file:
            input_lst = []
            for line in input_file:
                input_lst.append(int(line.rstrip().split()[-1]))
            self.hp, self.dmg = input_lst
        self.state   = None
        self.state_t = None

    def update_state(self):
        if self.state == "Poison":
            self.hp -= 3
            self.state_t -= 1
        if self.state_t == 0:
            self.state   = None
            self.state_t = None

def magic_missile(player, boss):
    player.mana       -= 53
    player.mana_spent += 53
    boss.hp           -= 4

def drain(player, boss):
    player.mana       -= 73
    player.mana_spent += 73
    player.hp         += 2
    boss.hp           -= 2

def shield(player, boss):
    player.mana       -= 113
    player.mana_spent += 113
    player.state["Shield"] = 6

def poison(player, boss):
    player.mana       -= 173
    player.mana_spent += 173
    boss.state = "Poison"
    boss.state_t = 6

def recharge(player, boss):
    player.mana       -= 229
    player.mana_spent += 229
    player.state["Recharge"] = 5

def attack(boss, player):
    player.hp -= max(boss.dmg - player.armor, 1)

def state_rep(player, boss, turn):
    str_rep = str(player.hp)+"|"+str(player.mana)+"|"+str(player.state["Shield"])+"|"+str(player.state["Recharge"])+"|"+str(boss.hp)+"|"+str(boss.state_t)+"|"+str(turn)
    return str_rep

def part_1(part_two=False):
    p           = Player()
    b           = Boss()
    queue       = []
    cnt         = 0
    seen_states = {}
    for s in p.spell_lst.keys():
        heapq.heappush(queue, (b.hp, p.mana_spent, cnt, deepcopy(p), deepcopy(b), s, 1))
        cnt += 1
    min_spent = 100000
    while len(queue):
        _, _, _, player, boss, spell, turn = heapq.heappop(queue)

        if player.mana_spent > min_spent:
            continue

        if part_two and turn == 1:
            player.hp -= 1
            if player.hp <= 0:
                continue

        player.update_state()
        boss.update_state()

        if boss.hp <= 0:
            min_spent = min(player.mana_spent, min_spent)

        if turn == 1:
            if player.mana - player.spell_lst[spell] < 0:
                continue
            spell(player, boss)
        elif turn == 0:
            attack(boss, player)
            if player.hp <= 0:
                continue

        if boss.hp <= 0:
            min_spent = min(player.mana_spent, min_spent)

        rep = state_rep(player, boss, turn)
        if rep in seen_states:
            if player.mana_spent < seen_states[rep]:
                seen_states[rep] = player.mana_spent
            else:
                continue
        else:
            seen_states[rep] = player.mana_spent

        for new_spell in player.spell_lst.keys():
            cnt += 1
            if new_spell.__name__ == "shield" and player.state["Shield"] not in [1, None] or new_spell.__name__ == "recharge" and player.state["Recharge"] not in [1, None] or new_spell.__name__ == "poison" and boss.state_t not in [1, None]:
                continue
            heapq.heappush(queue, (boss.hp, player.mana_spent, cnt, deepcopy(player), deepcopy(boss), new_spell, int(not turn)))
    return min_spent

def main():
    print(part_1())
    print(part_1(True))

if __name__ == "__main__":
    main()
