from enum import Enum

class MonsterType(Enum):
    NORMAL = "NORMAL"
    WATER = "Water"
    FIRE = "Fire"
    GRASS = "Grass"

class MoveType(Enum):
    NORMAL = "NORMAL"
    WATER = "Water"
    FIRE = "Fire"
    GRASS = "Grass"

class MoveCategory(Enum):
    ATTACK = "Attack"
    SPECIAL = "SPECIAL"
    STATUS = "Status"
