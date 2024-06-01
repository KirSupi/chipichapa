from abc import ABC, abstractmethod

import units


class Difficulty(str):
    pass


DIFFICULTY_LITE = Difficulty('lite')
DIFFICULTY_HEAVY = Difficulty('heavy')


# PATTERN Abstract Factory два режима "силы" юнитов - Lite и Heavy
class UnitFactory(ABC):
    @abstractmethod
    def create_warrior(self, team: units.Team) -> units.Warrior:
        pass

    @abstractmethod
    def create_knight(self, team: units.Team) -> units.Knight:
        pass

    @abstractmethod
    def create_archer(self, team: units.Team) -> units.Archer:
        pass

    @abstractmethod
    def create_wizard(self, team: units.Team) -> units.Wizard:
        pass

    @abstractmethod
    def create_healer(self, team: units.Team) -> units.Healer:
        pass

    @abstractmethod
    def create_shield(self, team: units.Team) -> units.Shield:
        pass
