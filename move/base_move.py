from abc import ABC, abstractmethod
from enum import Enum

class MoveType(Enum):
    ATTACK = "Attack"
    HEAL = "Heal"
    STATUS = "Status"


class BaseMove:
    def __init__(self,pp_cost,move_type):
        self.pp_cost = pp_cost
        self.move_type = move_type
    
    @abstractmethod
    def use(self,user,target):
        pass

class AttackMove(BaseMove):
    def __init__(self,pp_cost,power,attack_type):
        super().__init__(pp_cost,move_type=MoveType.ATTACK)
        self.power = power
        self.attack_type = attack_type
    
    def use(self,user,target):
        att_dmg = ((user.stats.attack*self.power)/target.stats.defense)
        dmg_rcv = att_dmg*CalculateTypeCoefficient(user.monster_type,target.monster_type)
        target.stats.hp-=dmg_rcv
