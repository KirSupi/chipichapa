import pygame

from . import colors
from . import fonts
from .button import Button


class Menu(object):
    _screen: pygame.Surface = None
    _locked: bool = False

    def __init__(self,
                 screen: pygame.Surface,
                 make_step_callback: callable = None,
                 undo_step_callback: callable = None,
                 redo_step_callback: callable = None,
                 change_strategy_callback: callable = None):
        self._screen = screen

        make_step_button = Button(
            screen,
            (0, 0),
            'Сделать ход',
            make_step_callback,
        )
        undo_step_button = Button(
            screen,
            (make_step_button.pos[0] + make_step_button.size[0], 0),
            'Назад',
            undo_step_callback,
        )
        redo_step_button = Button(
            screen,
            (undo_step_button.pos[0] + undo_step_button.size[0], 0),
            'Вперёд',
            redo_step_callback,
        )
        change_strategy_button = Button(
            screen,
            (redo_step_button.pos[0] + redo_step_button.size[0], 0),
            'Перестроиться',
            change_strategy_callback,
        )
        self._buttons: list[Button] = [
            make_step_button,
            undo_step_button,
            redo_step_button,
            change_strategy_button,
        ]

    def render(self):
        for button in self._buttons:
            button.render()

    def handle_click(self, event: pygame.event.Event):
        if self._locked:
            return

        for button in self._buttons:
            if button.click(event):
                if button.callback is not None:
                    button.callback()

    def lock(self):
        self._locked = True
        for button in self._buttons:
            button.lock()

    def unlock(self):
        self._locked = False
