import time
import itertools


class Shop:
    def __init__(self):
        self.weapon: int  = 0
        self.armor: int = 0
        self.rings: list = []
        self.income: int = 0

    def set_armor(self, armor):
        self.armor = armor

    def set_ring(self, rings: str):
        self.rings.clear()
        for i in range(len(rings)):
            self.rings.append(rings[i])
        if len(rings) == 1:
            self.rings.append(0)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def reset(self):
        self.income = 0

    def get_dmg(self):
        dmg: int = 0
        match self.weapon:
            case 1:
                dmg += 4
                self.income += 8
            case 2:
                dmg += 5
                self.income += 10
            case 3:
                dmg += 6
                self.income += 25
            case 4:
                dmg += 7
                self.income += 40
            case 5:
                dmg += 8
                self.income += 74
        for ring in self.rings:
            match ring:
                case '0':
                    dmg += 0
                case '1':
                    dmg += 1
                    self.income += 25
                case '2':
                    dmg += 2
                    self.income += 50
                case '3':
                    dmg += 3
                    self.income += 100
        return dmg
    def get_armor(self):
        armor: int = 0
        match self.armor:
            case 0:
                armor += 0
            case 1:
                armor += 1
                self.income += 13
            case 2:
                armor += 2
                self.income += 31
            case 3:
                armor += 3
                self.income += 53
            case 4:
                armor += 4
                self.income += 75
            case 5:
                armor += 5
                self.income += 102

        for ring in self.rings:
            match ring:
                case '0':
                    armor += 0
                case '4':
                    armor += 1
                    self.income += 20
                case '5':
                    armor += 2
                    self.income += 40
                case '6':
                    armor += 3
                    self.income += 80
        return armor



    def get_rings(self):
        return self.rings

class Player:
    def __init__(self, health):
        self.player_hp: int = health
        self.player_dmg: int = 0
        self.player_armor: int = 0
        self.death_player: bool = False

    def get_death_player(self):
        return self.death_player

    def get_player_hp(self):
        return self.player_hp

    def get_player_dmg(self):
        return self.player_dmg

    def take_damage(self, damage):
        if self.player_armor >= damage:
            self.player_hp -= 1
        else:
            self.player_hp -= damage - self.player_armor

    def rest_in_peace(self):
        self.death_player = True

    def revive(self, health: int):
        self.death_player = False
        self.player_hp = health

    def equip_weapon(self, weapon: Shop):
        self.player_dmg = weapon.get_dmg()

    def equip_armor(self, armor: Shop):
        self.player_armor = armor.get_armor()


player = Player(100)
shop = Shop()
weapons: list[int] = [1, 2, 3, 4, 5]
armors: list[int] = [0, 1, 2, 3, 4, 5]
rings01: list[int] = [0, 1, 2, 3, 4, 5, 6]
combinations = itertools.product(weapons, armors, itertools.combinations(rings01, 2))
boss_hp: int = 103
boss_dmg: int = 9
boss_armor: int = 2
death_boss: bool = False
cheat: int = int(input("cheats [1/0] -> "))
looses: list[int] = []
weapon: int
armor: int
rings: str
match cheat:
    case 0:
        weapon = int(input("  Weapons:    Cost  Damage  Armor\n"
              "1 Dagger        8     4       0\n"
              "2 Shortsword   10     5       0\n"
              "3 Warhammer    25     6       0\n"
              "4 Longsword    40     7       0\n"
              "5 Greataxe     74     8       0\n"
              "----- choose your weapon -----\n"
              "⌯⌲  "))

        armor = int(input("\n  Armor:      Cost  Damage  Armor\n"
              "0 Naked         0     0       0\n"
              "1 Chainmail    31     0       2\n"
              "2 Shortsword   10     5       0\n"
              "3 Splint Mail  53     0       3\n"
              "4 Banded Mail  75     0       4\n"
              "5 Plate Mail  102     0       5\n"
              "----- choose your Armor -----\n"
              "⌯⌲  "))

        rings = str(input("\n  Rings:      Cost  Damage  Armor\n"
              "0 Naked         0     0       0\n"
              "1 Damage +1    25     1       0\n"
              "2 Damage +2    50     2       0\n"
              "3 Damage +3   100     3       0\n"
              "4 Defense +1   20     0       1\n"
              "5 Defense +2   40     0       2\n"
              "6 Defense +3   80     0       3\n"
              "----- choose your Rings -----\n"
              "⌯⌲  "))

        shop.set_weapon(weapon)
        shop.set_armor(armor)
        shop.set_ring(rings)

        player.equip_armor(shop)
        player.equip_weapon(shop)

        while not death_boss and not player.get_death_player():
            if boss_armor >= player.get_player_dmg():
                boss_hp -= 1
            else:
                boss_hp -= player.get_player_dmg() - boss_armor
            print(f"Boss HP: {boss_hp}")
            time.sleep(1)
            player.take_damage(boss_dmg)
            print(f"Player HP: {player.get_player_hp()}")
            time.sleep(1)

            if boss_hp <= 0:
                death_boss = True
            elif player.get_player_hp() <= 0:
                player.rest_in_peace()

        if death_boss:
            print("\nBoss is dead")
        elif player.get_death_player():
            print("\nYou're dead")
        elif death_boss and player.get_death_player():
            print("\nBoth died")

        print(f"You spend {shop.income}$")

    case 1:
        rings = "\0"
        for _list in combinations:
            weapon = _list[0]
            armor = _list[1]
            rings = "".join(map(str, _list[2]))
            shop.set_weapon(weapon)
            shop.set_armor(armor)
            shop.set_ring(rings)

            player.equip_armor(shop)
            player.equip_weapon(shop)

            while not death_boss and not player.get_death_player():
                if boss_armor >= player.get_player_dmg():
                    boss_hp -= 1
                else:
                    boss_hp -= player.get_player_dmg() - boss_armor
                player.take_damage(boss_dmg)

                if boss_hp <= 0:
                    death_boss = True
                elif player.get_player_hp() <= 0:
                    player.rest_in_peace()

            if player.get_player_hp() <= 0:
                looses.append(shop.income)
            boss_hp = 103
            death_boss = False
            player.revive(100)
            shop.reset()

        print(max(looses)) #221 too high



