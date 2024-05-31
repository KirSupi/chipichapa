import time
import pygame
from config import config
import units
from ui import UI
from units import Base


class Game(object):
    FPS = 30
    _ui: UI = None
    _left_team: list[units.Base] = []
    _right_team: list[units.Base] = []
    _starting_team: units.Team = units.TEAM_LEFT
    _step_number: int = 0

    def run(self):
        self._ui = UI(self._make_step)

        self._add_unit(units.Archer(units.TEAM_LEFT))
        self._add_unit(units.Healer(units.TEAM_LEFT))
        self._add_unit(units.Warrior(units.TEAM_LEFT))
        self._add_unit(units.Knight(units.TEAM_LEFT))
        self._add_unit(units.Shield(units.TEAM_LEFT))

        self._add_unit(units.Warrior(units.TEAM_RIGHT))
        self._add_unit(units.Warrior(units.TEAM_RIGHT))
        self._add_unit(units.Wizard(units.TEAM_RIGHT))

        # self._left_team[0].start_animation()

        while True:
            if len(self._left_team) == 0:
                return  # todo game over title
            if len(self._right_team) == 0:
                return  # todo game over title

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._ui.handle_click(event)

            self._ui.render()
            time.sleep(1 / self.FPS)

    def _make_step(self):
        self._step_number += 1
        self._ui.lock_menu()

        first_left = self._left_team[0]
        first_right = self._right_team[0]

        if self._starting_team == units.TEAM_LEFT and self._step_number % 2:
            self._ui.start_unit_animation(first_left.id)
            attack_points = first_left.attack()
            if isinstance(first_left, units.IPerker):
                first_left.perk()
            first_right.defense(attack_points)
            self._ui.render()

        # for i in range(max(len(self._left_team), len(self._right_team))):

        self._ui.unlock_menu()

    def _add_unit(self, unit: Base):
        if unit.team == units.TEAM_LEFT:
            self._left_team.insert(0, unit)
        else:
            self._right_team.append(unit)

        self._ui.add_unit(unit)


game = Game()
