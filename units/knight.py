import random
from units.base import Base
from units.types import Team, SPECIALIZATION_KNIGHT


class Knight(Base):
    SPECIALIZATION = SPECIALIZATION_KNIGHT

    def __init__(self, team: Team, hp: int, attack: int, defense: int, dodge: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, attack, defense, dodge)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points
