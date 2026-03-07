class Stats:
    def __init__(self, attack, defense, speed,special_attack ,special_defense, hp, pp):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.specialAttack = special_attack
        self.specialDefense = special_defense
        self.pp = pp
        self.hp = hp

class BaseMonster:
    def __init__(self,stats:Stats,monster_type,monster_moves):
        self.stats = stats
        self.type = type
    
    def use_move(target, monster_move):
        monster_move.use()
        