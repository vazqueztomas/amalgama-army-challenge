from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Unit:
    created_on: date = field(default_factory=lambda: date.today())
    strenght: int = 0

    @property
    def unit_type(self) -> str:
        return self.__class__.__name__

    def years_of_life(self, today: Optional[date] = None) -> int:
        today = today or date.today()
        years = today.year - self.created_on.year
        if (today.month, today.day) < (self.created_on.month, self.created_on.day):
            years -= 1
        return max(0, years)

    def train(self, points: int) -> None:
        if points < 0:
            raise ValueError("Training points must be non-negative")
        self.strenght += points


@dataclass
class Pikeman(Unit):
    strenght: int = 5


@dataclass
class Archer(Unit):
    strenght: int = 10


@dataclass
class Knight(Unit):
    strenght: int = 20
