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
        self.monster_moves = monster_moves
        self.monster_type = monster_type
    
    def use_move(self, target, move_idx):
        self.monster_moves[move_idx].use()
        