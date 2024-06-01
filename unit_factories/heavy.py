import units
from .factory import UnitFactory


class HeavyUnitFactory(UnitFactory):
    def create_warrior(self, team: units.Team) -> units.Warrior:
        return units.Warrior(team, 150, 120, 0, 120)

    def create_knight(self, team: units.Team) -> units.Knight:
        return units.Knight(team, 500, 150, 300, 20)

    def create_archer(self, team: units.Team) -> units.Archer:
        return units.Archer(team, 100, 15, 30)

    def create_wizard(self, team: units.Team) -> units.Wizard:
        return units.Wizard(team, 200, 5, 0, 0)

    def create_healer(self, team: units.Team) -> units.Healer:
        return units.Healer(team, 250, 0, 0, 0)

    def create_shield(self, team: units.Team) -> units.Shield:
        return units.Shield(team, 1000)
