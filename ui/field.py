import uuid
import pygame
import units
from config import config
from . import colors


class Field(object):
    _left_team: list[units.IBase] = []
    _right_team: list[units.IBase] = []
    _surface: pygame.Surface = None

    def __init__(self, surface: pygame.Surface):
        self._surface = surface

    def add_unit(self, unit: units.IBase):
        if unit.team == units.TEAM_LEFT:
            self._left_team.append(unit)
        else:
            self._right_team.append(unit)

    def remove_unit(self, unit: units.IBase):
        if unit.team == units.TEAM_LEFT:
            for i in range(len(self._left_team)):
                if self._left_team[i].id == unit.id:
                    self._left_team.pop(i)
                    break
        else:
            for i in range(len(self._right_team)):
                if self._right_team[i].id == unit.id:
                    self._right_team.pop(i)
                    break

    def render(self) -> bool:
        rect = self._surface.get_rect()
        pygame.draw.line(self._surface, (255, 0, 255), rect.midtop, rect.midbottom)

        animated = False

        for i, unit in enumerate(self._left_team):
            animated = animated or unit.animated
            self._surface.blit(self._get_unit_sprite(unit),
                               (rect.centerx - config.sprites_size * (i + 1), rect.centery))

        for i, unit in enumerate(self._right_team):
            animated = animated or unit.animated
            self._surface.blit(self._get_unit_sprite(unit),
                               (rect.centerx + config.sprites_size * i, rect.centery))

        return animated

    @staticmethod
    def _get_unit_sprite(unit: units.IBase) -> pygame.Surface:
        unit_sprite = unit.sprite
        sprite = pygame.Surface(unit_sprite.get_size(), pygame.SRCALPHA, 32)
        sprite.blit(unit_sprite, (0, 0))
        sprite_rect = sprite.get_rect()
        pygame.draw.line(sprite,
                         colors.BLACK,
                         (sprite_rect.bottomleft[0] + 4, sprite_rect.bottomleft[1]),
                         (sprite_rect.bottomright[0] - 4, sprite_rect.bottomright[1]),
                         20)
        pygame.draw.line(sprite,
                         colors.RED,
                         (sprite_rect.bottomleft[0] + 4, sprite_rect.bottomleft[1]),
                         (sprite_rect.bottomright[0] * unit.hp / unit.max_hp - 4, sprite_rect.bottomright[1]),
                         20)
        return sprite

    def start_unit_animation(self, unit_id: uuid.UUID) -> None:
        for unit in self._left_team + self._right_team:
            if unit.id == unit_id:
                unit.start_animation()
                break
