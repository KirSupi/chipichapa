import random
from units.base import Base
from units.types import Team, SPECIALIZATION_ARCHER


class Archer(Base):
    SPECIALIZATION = SPECIALIZATION_ARCHER

    def __init__(self, team: Team, hp: int, attack: int, dodge: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, attack, 0, dodge)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points
