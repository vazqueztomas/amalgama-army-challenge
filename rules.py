from models import Archer, Knight, Pikeman, Unit

TRAINING_RULES: dict[type[Unit], dict[str, int]] = {
    Pikeman: {"gain": 3, "cost": 10},
    Archer: {"gain": 7, "cost": 20},
    Knight: {"gain": 10, "cost": 30},
}

TRANSFORMATION_RULES = {
    Pikeman: {"target": Archer, "cost": 30},
    Archer: {"target": Knight, "cost": 40},
    Knight: {"target": None, "cost": None},
}

CIVILIZATION_START: dict[str, dict[type[Unit], int]] = {
    "Chinese": {Pikeman: 2, Archer: 25, Knight: 2},
    "English": {Pikeman: 10, Archer: 10, Knight: 10},
    "Byzantine": {Pikeman: 5, Archer: 8, Knight: 15},
}
