import random
from abc import ABC

from .interfaces import IPerker
from .base import Base
from .types import Team, SPECIALIZATION_WIZARD


class Wizard(Base, IPerker):
    MAX_HP = 50
    MAX_POWER = 0
    SPECIALIZATION = SPECIALIZATION_WIZARD

    def __init__(self, team: Team):
        Base.__init__(self, team, self.SPECIALIZATION, self.MAX_HP)

    def attack(self) -> int:
        return random.randint(0, self.MAX_POWER)

    def defense(self, hit_points: int):
        self._hp -= hit_points

    def perk(self):
        pass
