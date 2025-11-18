from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Unit(BaseModel):
    created_on: date = Field(default_factory=date.today)
    strength: int = 0

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
        self.strength += points


class Pikeman(Unit):
    strength: int = 5


class Archer(Unit):
    strength: int = 10


class Knight(Unit):
    strength: int = 20
