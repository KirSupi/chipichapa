import random
from units.base import Base
from units.types import Team, SPECIALIZATION_HEALER


class Healer(Base):
    MAX_HP = 50
    MAX_POWER = 0
    SPECIALIZATION = SPECIALIZATION_HEALER

    def __init__(self, team: Team):
        Base.__init__(self, team, self.SPECIALIZATION, self.MAX_HP)

    def attack(self) -> int:
        return random.randint(0, self.MAX_POWER)

    def defense(self, hit_points: int):
        self._hp -= hit_points
