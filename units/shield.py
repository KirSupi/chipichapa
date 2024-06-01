import copy
import random
import uuid
from abc import ABC

import pygame

from units.base import Base, IBase
from units.types import Team, SPECIALIZATION_SHIELD


class Shield(Base, IBase, ABC):
    SPECIALIZATION = SPECIALIZATION_SHIELD

    def __init__(self, team: Team, hp: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, 0, 0, 0)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points

    @property
    def team(self) -> Team:
        return super().team

    @property
    def id(self) -> uuid.UUID:
        return super().id

    @property
    def hp(self) -> int:
        return super().hp

    @property
    def max_hp(self) -> int:
        return super().max_hp

    @property
    def animated(self) -> bool:
        return super().animated

    @property
    def sprite(self) -> pygame.Surface:
        return super().sprite

    def is_alive(self) -> bool:
        return super().is_alive()

    def start_animation(self):
        super().start_animation()

    def clone(self):
        c = copy.deepcopy(self)
        c._id = uuid.uuid4()
        return c
