from abc import ABC, abstractmethod
from enums.monster_enums import MoveType,MoveCategory
from battle_calc import dmg_math

class BaseMove:
    def __init__(self,pp_cost,move_category):
        self.pp_cost = pp_cost
        self.move_category = move_category
    
    @abstractmethod
    def use(self,user,target):
        pass

class AttackMove(BaseMove):
    def __init__(self,pp_cost,power,move_type):
        super().__init__(pp_cost,move_category=MoveCategory.ATTACK)
        self.power = power
        self.move_type = move_type
    
    def use(self,user,target):
        att_dmg = ((user.stats.attack*self.power)/target.stats.defense)
        dmg_rcv = att_dmg*dmg_math.calculate_type_coefficient(self.move_type,target.monster_type)
        target.stats.hp-=dmg_rcv
