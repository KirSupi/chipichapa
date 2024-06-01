import random
from abc import ABC

from .interfaces import IPerker
from .base import Base
from .types import Team, SPECIALIZATION_WIZARD


class Wizard(Base, IPerker):
    SPECIALIZATION = SPECIALIZATION_WIZARD

    def __init__(self, team: Team, hp: int, attack: int, defense: int, dodge: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, attack, defense, dodge)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points

    def perk(self):
        pass
