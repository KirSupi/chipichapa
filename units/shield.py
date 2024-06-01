import random
from units.base import Base
from units.types import Team, SPECIALIZATION_SHIELD


class Shield(Base):
    SPECIALIZATION = SPECIALIZATION_SHIELD

    def __init__(self, team: Team, hp: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, 0, 0, 0)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points
