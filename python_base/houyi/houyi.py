from python_base.game import Game


class HouYi(Game):
    def add_defense(self, defense):
        self.defense = defense

    def fight_houyi(self, enemy_hp, enemy_power):

        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            if self.hp <= 0 and enemy_hp > 0:
                print('我输了')
                break
            elif enemy_hp <= 0 and self.hp > 0:
                print('我赢了')
                break
            elif enemy_hp <= 0 and self.hp <= 0:
                print('平局')
                break

houyi = HouYi(1000, 200)
houyi.add_defense(100)
houyi.fight_houyi(1000, 300)
