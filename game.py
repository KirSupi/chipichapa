import time
import pygame

import unit_factories
from config import config
import units
from ui import UI
from unit_factories.factory import Difficulty
from units import Base


class Game(object):
    FPS = 30
    _ui: UI = None
    _left_team: list[units.Base] = []
    _right_team: list[units.Base] = []
    _starting_team: units.Team = units.TEAM_LEFT
    _step_number: int = 0
    _factory: unit_factories.UnitFactory
    _difficulty: Difficulty = config.difficulty

    def run(self):
        self._ui = UI(self._make_step)

        if not self._difficulty:
            self._ui.run_difficulty_menu(self._set_difficulty)

        self._factory = unit_factories.LiteUnitFactory()

        self._add_unit(self._factory.create_shield(units.TEAM_LEFT))
        self._add_unit(self._factory.create_knight(units.TEAM_LEFT))
        self._add_unit(self._factory.create_warrior(units.TEAM_LEFT))
        self._add_unit(self._factory.create_archer(units.TEAM_LEFT))
        self._add_unit(self._factory.create_healer(units.TEAM_LEFT))

        self._add_unit(self._factory.create_warrior(units.TEAM_RIGHT))
        self._add_unit(self._factory.create_warrior(units.TEAM_RIGHT))
        self._add_unit(self._factory.create_wizard(units.TEAM_RIGHT))

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

        attack_team = self._left_team
        defense_team = self._right_team
        if self._starting_team == units.TEAM_LEFT and not self._step_number % 2:
            attack_team, defense_team = defense_team, attack_team

        first_attack = attack_team[0]
        first_defense = defense_team[0]

        # Ходит первый юнит первой команды
        self._ui.start_unit_animation(first_attack.id)
        attack_points = first_attack.attack()
        first_defense.defense(attack_points)
        self._ui.render(True)

        # Ходит первый юнит второй команды умер, то заменяем его
        if not first_defense.is_alive():
            defense_team.pop(0)
            if not len(defense_team):
                return
            first_defense = defense_team[0]
            self._ui.render()

        # Ходит первый юнит второй команды
        self._ui.start_unit_animation(first_defense.id)
        attack_points = first_defense.attack()
        first_attack.defense(attack_points)
        self._ui.render(True)

        # Запускаем перки у первой команды
        for unit in attack_team:
            if not isinstance(unit, units.IPerker):
                continue

            if unit.perk(attack_team, defense_team):
                self._ui.start_unit_animation(unit.id)
                self._ui.render(True)

        attack_team, defense_team = defense_team, attack_team

        # Запускаем перки у второй команды
        for unit in attack_team:
            if not isinstance(unit, units.IPerker):
                continue

            if unit.perk(attack_team, defense_team):
                self._ui.start_unit_animation(unit.id)
                self._ui.render(True)

        self._ui.unlock_menu()

    def _add_unit(self, unit: Base):
        if unit.team == units.TEAM_LEFT:
            self._left_team.append(unit)
        else:
            self._right_team.append(unit)

        self._ui.add_unit(unit)

    def _set_difficulty(self, difficulty: Difficulty):
        self._difficulty = difficulty


game = Game()
