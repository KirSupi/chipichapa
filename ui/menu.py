import pygame

from . import colors
from . import fonts


class Button(object):
    FONT: pygame.font.Font = fonts.default
    PADDING: int = 10

    UNLOCKED_BACKGROUND_COLOR: tuple[int, int, int] = colors.WHITE
    UNLOCKED_TEXT_COLOR: tuple[int, int, int] = colors.BLACK

    LOCKED_BACKGROUND_COLOR: tuple[int, int, int] = colors.LIGHT_GRAY
    LOCKED_TEXT_COLOR: tuple[int, int, int] = colors.GRAY

    _locked: bool = False
    _text_unlocked: pygame.surface.Surface = None
    _text_locked: pygame.surface.Surface = None
    _pos: tuple[int, int] = (0, 0)
    _size: tuple[int, int] = (0, 0)
    _rect: pygame.Rect = None
    _screen: pygame.Surface = None
    _surface_unlocked: pygame.Surface = None
    _surface_locked: pygame.Surface = None
    callback: callable = None

    def __init__(self,
                 _screen: pygame.surface.Surface,
                 pos: tuple[int, int] = (0, 0),
                 text: str = 'Кнопка',
                 callback: callable = None,
                 ) -> None:
        self._screen = _screen
        self._pos = pos
        self.callback = callback
        self._text_unlocked = self.FONT.render(text, True, self.UNLOCKED_TEXT_COLOR)
        self._text_locked = self.FONT.render(text, True, self.LOCKED_TEXT_COLOR)
        text_w, text_h = self._text_unlocked.get_size()
        self._size = (text_w + self.PADDING * 2, text_h + self.PADDING * 2)
        self._rect = pygame.Rect(self._pos[0], self._pos[1], self._size[0], self._size[1])

        # Surface for unlocked state
        self._surface_unlocked = pygame.Surface(self._size)
        self._surface_unlocked.fill(self.UNLOCKED_BACKGROUND_COLOR)
        self._surface_unlocked.blit(self._text_unlocked, (self.PADDING, self.PADDING))
        pygame.draw.rect(
            self._surface_unlocked,
            colors.BLACK,
            self._rect,
            2,
            0,
        )

        # Surface for locked state
        self._surface_locked = pygame.Surface(self._size)
        self._surface_locked.fill(self.LOCKED_BACKGROUND_COLOR)
        self._surface_locked.blit(self._text_locked, (self.PADDING, self.PADDING))
        pygame.draw.rect(
            self._surface_locked,
            colors.BLACK,
            self._rect,
            2,
            0,
        )

    def render(self) -> None:
        if self._locked:
            self._screen.blit(self._surface_locked, self._pos)
        else:
            self._screen.blit(self._surface_unlocked, self._pos)

    def click(self, event: pygame.event.Event) -> bool:
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self._rect.collidepoint(x, y):
            return True

        return False

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def pos(self) -> tuple[int, int]:
        return self._pos


class Menu(object):
    _screen: pygame.Surface = None
    _locked: bool = False

    def __init__(self,
                 screen: pygame.Surface,
                 make_step_callback: callable = None,
                 undo_step_callback: callable = None,
                 redo_step_callback: callable = None,
                 change_strategy_callback: callable = None,
                 ):
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
        print(
            make_step_button.pos,
            undo_step_button.pos,
            redo_step_button.pos,
            change_strategy_button.pos,
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
                button.callback()

    def lock(self):
        self._locked = True
        for button in self._buttons:
            button.lock()

    def unlock(self):
        self._locked = False
