import copy
import random
import uuid
from abc import ABC

import pygame

from .interfaces import IPerker
from .base import Base, IBase
from .types import Team, SPECIALIZATION_WIZARD


class Wizard(Base, IBase, IPerker, ABC):
    SPECIALIZATION = SPECIALIZATION_WIZARD

    def __init__(self, team: Team, hp: int, attack: int, defense: int, dodge: int) -> None:
        Base.__init__(self, team, self.SPECIALIZATION, hp, attack, defense, dodge)

    def attack(self) -> int:
        return random.randint(0, self._attack)

    def defense(self, hit_points: int):
        self._hp -= hit_points

    # Клонирование юнита
    def perk(self, attack_team: list[Base], _: list[Base]):
        return
        # Ищем свой индекс
        self_index = None
        for i, unit in enumerate(attack_team):
            if self.id == unit.id:
                self_index = i
                break
        if self_index is None:
            raise IndexError

        # Выбираем рандомного юнита, клонируем и ставим перед собой
        # prototype_index = random.choice([i for i in range(len(attack_team)) if i != self_index])
        # clone = attack_team[prototype_index].clone()
        # attack_team.insert(self_index, clone)

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
