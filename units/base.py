import pathlib
import uuid
from abc import ABC, abstractmethod

import pygame

from config import config
from .types import Team, Specialization

class IBase(ABC):
    @abstractmethod
    @property
    def team(self) -> Team:
        raise NotImplementedError


class Base(object):
    _id: uuid.UUID = uuid.uuid4()
    _team: Team = None
    _max_hp: int = 0
    _hp: int = 0
    _attack: int = 0
    _defense: int = 0
    _dodge: int = 0
    _spec: Specialization = None
    _MAX_ANIMATION_FRAMES: int = 15
    _animation_frame: int | None = None
    _sprite: pygame.Surface = None

    def __init__(self, team: Team, spec: Specialization, hp: int):
        self._team = team
        self._max_hp = hp
        self._hp = hp
        self._spec = spec

    @property
    def team(self) -> Team:
        return self._team

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    # PATTERN Lasy Initialization
    @property
    def sprite(self) -> pygame.Surface:
        if self._sprite is None:
            file_name = self._spec + '.' + config.sprites_format
            self._sprite = pygame.image.load(
                str(pathlib.Path(config.sprites_directory).joinpath(self._team, file_name)),
            )

        # Animation

        # if self._animation_frame is not None and self._animation_frame >= self._MAX_ANIMATION_FRAMES:
        #     self._animation_frame = None

        sprite = self._sprite.copy()
        if self._animation_frame is not None:
            self._animation_frame += 1
            # from 0.1 to 1.0

            animation_progress = (100 + (255 - 100)
                                  / (self._MAX_ANIMATION_FRAMES - 1)
                                  * (self._animation_frame % self._MAX_ANIMATION_FRAMES - 1))
            sprite.set_alpha(int(animation_progress))

        return sprite

    def attack(self) -> int:
        pass

    def defense(self, hit_points: int):
        pass

    def is_alive(self) -> bool:
        return self._hp > 0

    def start_animation(self):
        self._animation_frame = 0
