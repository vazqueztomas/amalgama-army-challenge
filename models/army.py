from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from helpers.exceptions import InsufficientGold, TransformationError

from .rules import CIVILIZATION_START, TRAINING_RULES, TRANSFORMATION_RULES
from .units import Unit


class BattleRecord(BaseModel):
    timestamp: datetime
    opponent: str
    result: str
    self_strength: int
    opponent_strength: int

    model_config = {
        "validate_assignment": True,
        "frozen": False,
    }


class Army(BaseModel):
    name: str
    civilization: str
    gold: int = 1000
    units: List[Unit] = Field(default_factory=list)
    history: List[BattleRecord] = Field(default_factory=list)

    model_config = {
        "validate_assignment": True,
        "frozen": False,
    }

    def __init__(self, **data):
        super().__init__(**data)

        if len(self.units) == 0:
            if self.civilization not in CIVILIZATION_START:
                raise ValueError(f"Unknown civilization '{self.civilization}'")

            for unit_cls, count in CIVILIZATION_START[self.civilization].items():
                for _ in range(count):
                    self.units.append(unit_cls())

    def total_strength(self) -> int:
        return sum(u.strength for u in self.units)

    def train_unit(self, index: int) -> None:
        unit = self.units[index]
        rule = TRAINING_RULES[type(unit)]
        cost, gain = rule["cost"], rule["gain"]

        if self.gold < cost:
            raise InsufficientGold(
                f"Army '{self.name}' does not have enough gold to train."
            )

        self.gold -= cost
        unit.train(gain)

    def transform_unit(self, index: int) -> None:
        unit = self.units[index]
        rule = TRANSFORMATION_RULES[type(unit)]
        target_cls = rule["target"]
        cost = rule["cost"]

        if target_cls is None:
            raise TransformationError(
                f"{unit.unit_type} cannot be transformed further."
            )

        if self.gold < cost:
            raise InsufficientGold(
                f"Army '{self.name}' does not have enough gold to transform."
            )

        new_unit = target_cls(created_on=unit.created_on)
        self.units[index] = new_unit

        self.gold -= cost

    def _remove_top_units(self, n: int) -> None:
        if not self.units:
            return

        sorted_units = sorted(
            self.units, key=lambda u: (u.strength, u.created_on), reverse=True
        )

        for u in sorted_units[:n]:
            self.units.remove(u)

    def record_battle(
        self, opponent: Army, result: str, own_strength: int, opp_strength: int
    ) -> None:
        self.history.append(
            BattleRecord(
                timestamp=datetime.now(),
                opponent=opponent.name,
                result=result,
                self_strength=own_strength,
                opponent_strength=opp_strength,
            )
        )

    def attack(self, opponent: Army) -> str:
        my_strength = self.total_strength()
        opp_strength = opponent.total_strength()

        if my_strength > opp_strength:
            opponent._remove_top_units(2)
            self.gold += 100
            result = "win"
        elif my_strength < opp_strength:
            self._remove_top_units(2)
            opponent.gold += 100
            result = "loss"
        else:
            self._remove_top_units(1)
            opponent._remove_top_units(1)
            result = "tie"

        self.record_battle(opponent, result, my_strength, opp_strength)
        opponent.record_battle(
            self,
            "win" if result == "loss" else "loss" if result == "win" else "tie",
            opp_strength,
            my_strength,
        )

        return result

    def summary(self) -> str:
        return (
            f"Army {self.name} ({self.civilization}) - "
            f"Units: {len(self.units)}, "
            f"Strength: {self.total_strength()}, "
            f"Gold: {self.gold}"
        )
