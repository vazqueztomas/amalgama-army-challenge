from pydantic import BaseModel

from models.units import Archer, Knight, Pikeman, Unit


class TrainingRule(BaseModel):
    gain: int
    cost: int


class TransformationRule(BaseModel):
    target: type[Unit] | None
    cost: int | None


TRAINING_RULES: dict[type[Unit], TrainingRule] = {
    Pikeman: TrainingRule(gain=3, cost=10),
    Archer: TrainingRule(gain=7, cost=20),
    Knight: TrainingRule(gain=10, cost=30),
}

TRANSFORMATION_RULES: dict[type[Unit], TransformationRule] = {
    Pikeman: TransformationRule(target=Archer, cost=30),
    Archer: TransformationRule(target=Knight, cost=40),
    Knight: TransformationRule(target=None, cost=None),
}

CIVILIZATION_START: dict[str, dict[type[Unit], int]] = {
    "Chinese": {Pikeman: 2, Archer: 25, Knight: 2},
    "English": {Pikeman: 10, Archer: 10, Knight: 10},
    "Byzantine": {Pikeman: 5, Archer: 8, Knight: 15},
}
