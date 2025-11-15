from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field


class Unit(BaseModel):
    created_on: date = Field(default_factory=date.today)
    strength: int = 0

    @property
    def unit_type(self) -> str:
        return self.__class__.__name__

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
