import copy
import random
import uuid
from abc import ABC

import pygame

from units.base import Base, IBase
from units.types import Team, SPECIALIZATION_HEALER


class Healer(Base, IBase, ABC):
    SPECIALIZATION = SPECIALIZATION_HEALER

    def __init__(self, team: Team, hp: int, attack: int, defense: int, dodge: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, attack, defense, dodge)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points

    # Лечение юнита
    def perk(self, attack_team: list[Base], _: list[Base]):
        # Выбираем рандомного юнита и лечим
        return
        # unit = random.choice([i for i in attack_team if i.id != self.id])
        # unit.healable()

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
