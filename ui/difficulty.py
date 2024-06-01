import pygame

import unit_factories
from ui import fonts, colors
from ui.button import Button


class DifficultyMenu:
    _screen: pygame.Surface = None
    _title: pygame.Surface = None
    _button_lite: Button = None
    _button_heavy: Button = None
    _set_difficulty_callback: callable

    def __init__(self, screen: pygame.Surface, set_difficulty_callback: callable) -> None:
        self._screen = screen
        self._title = fonts.default.render("Выберите уровень сложности", True, colors.BLACK)
        rect = screen.get_rect()
        self._button_lite = Button(self._screen,
                                   (rect.centerx, rect.centery),
                                   "Lite",
                                   self._on_click_lite)
        self._button_heavy = Button(self._screen,
                                    (rect.centerx, rect.centery + self._button_lite.size[1]),
                                    "Heavy",
                                    self._on_click_heavy)
        self._set_difficulty_callback = set_difficulty_callback

    def render(self) -> None:
        self._screen.blit(self._title,
                          (self._screen.get_rect().centerx - self._title.get_rect().size[0]/2,
                           self._screen.get_rect().centery / 2))
        self._button_lite.render()
        self._button_heavy.render()
        pygame.display.flip()

    def _on_click_lite(self) -> None:
        self._set_difficulty_callback(unit_factories.DIFFICULTY_LITE)

    def _on_click_heavy(self) -> None:
        self._set_difficulty_callback(unit_factories.DIFFICULTY_HEAVY)

    def handle_click(self, event: pygame.event.Event):
        if self._button_lite.click(event):
            self._button_lite.callback()
            return True
        if self._button_heavy.click(event):
            self._button_heavy.callback()
            return True
        return False
