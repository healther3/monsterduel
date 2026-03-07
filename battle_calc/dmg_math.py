from enums.monster_enums import MoveType,MonsterType

TYPE_CHART = {
    MoveType.WATER: {
        MonsterType.FIRE: 2.0, 
        MonsterType.GRASS: 0.5  
    },
    MoveType.FIRE: {
        MonsterType.GRASS: 2.0,
        MonsterType.WATER: 0.5
    },
    MoveType.GRASS: {
        MonsterType.WATER: 2.0,
        MonsterType.FIRE: 0.5
    }
}

def calculate_type_coefficient(move_type, target_type):
    return TYPE_CHART.get(move_type,{}).get(target_type,1.0)
