from abc import ABC, abstractmethod

class BaseMove:
    def __init__(self,pp_cost,move_type):
        self.pp_cost = pp_cost
        self.move_type = move_type
    
    @abstractmethod
    def use(self):
        pass