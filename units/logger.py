import uuid
from abc import ABC

import pygame

from units import Team
from units.base import IBase, Base


# PATTERN Decorator помогает логгировать действия юнитов
class Logger(IBase, ABC):
    def __init__(self, unit: Base):
        self._unit = unit

    @property
    def team(self) -> Team:
        return self._unit.team

    def attack(self) -> int:
        print(f'Unit {self._unit.id} ({self._unit.team}) attacking...')
        return self._unit.attack()

    def defense(self, hit_points: int):
        print(f'Unit {self._unit.id} ({self._unit.team}) defended...')
        return self._unit.defense(hit_points)

    @property
    def id(self) -> uuid.UUID:
        return self._unit.id

    @property
    def hp(self) -> int:
        return self._unit.hp

    @property
    def max_hp(self) -> int:
        return self._unit.max_hp

    @property
    def animated(self) -> bool:
        return self._unit.animated

    @property
    def sprite(self) -> pygame.Surface:
        return self._unit.sprite

    def is_alive(self) -> bool:
        return self._unit.is_alive()

    def start_animation(self):
        print(f'Unit {self._unit.id} ({self._unit.team}) starts animation...')
        self._unit.start_animation()

    def clone(self):
        return self._unit.clone()
