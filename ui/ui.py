import pathlib
import uuid

import pygame
from config import config
from units import Base
from .menu import Menu
from .field import Field
from . import colors


class UI(object):
    _screen: pygame.Surface = None
    _field: Field = None
    _menu: Menu = None
    _bg_width: int = 0
    _bg_height: int = 0
    _screen_rect: pygame.Rect = None
    _background_image: pygame.Surface = None

    def __init__(self,
                 make_step_callback: callable = None,
                 undo_step_callback: callable = None,
                 redo_step_callback: callable = None,
                 change_strategy_callback: callable = None):
        pygame.init()
        self._screen = pygame.display.set_mode((1200, 800))
        self._field = Field(self._screen)
        self._menu = Menu(
            self._screen,
            make_step_callback,
            undo_step_callback,
            redo_step_callback,
            change_strategy_callback,
        )

        # Загрузка фонового изображения
        self._background_image = pygame.image.load(
            pathlib.Path(config.sprites_directory).joinpath(config.background_sprite),
        ).convert()

        # Получение размеров изображения и экрана
        self._bg_width, self._bg_height = self._background_image.get_size()
        self._screen_rect = self._screen.get_rect()

    def render(self) -> None:
        self._screen.fill(colors.WHITE)

        # Заполнение экрана фоновой картинкой
        for y in range(0, self._screen_rect.height, self._bg_height):
            for x in range(0, self._screen_rect.width, self._bg_width):
                self._screen.blit(self._background_image, (x, y))

        self._field.render()
        self._menu.render()
        pygame.display.flip()

    def add_unit(self, unit: Base) -> None:
        self._field.add_unit(unit)

    def remove_unit(self, unit: Base) -> None:
        self._field.remove_unit(unit)

    def handle_click(self, event: pygame.event.Event) -> None:
        self._menu.handle_click(event)

    def unlock_menu(self) -> None:
        self._menu.unlock()

    def lock_menu(self) -> None:
        self._menu.lock()

    def start_unit_animation(self, unit_id: uuid.UUID) -> None:
        self._field.start_unit_animation(unit_id)

