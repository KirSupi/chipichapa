import units
from .factory import UnitFactory


class LiteUnitFactory(UnitFactory):
    def create_warrior(self, team: units.Team) -> units.Warrior:
        return units.Warrior(team, 50, 20, 0, 20)

    def create_knight(self, team: units.Team) -> units.Knight:
        return units.Knight(team, 100, 30, 100, 5)

    def create_archer(self, team: units.Team) -> units.Archer:
        return units.Archer(team, 50, 15,  30)

    def create_wizard(self, team: units.Team) -> units.Wizard:
        return units.Wizard(team, 50, 5, 0, 0)

    def create_healer(self, team: units.Team) -> units.Healer:
        return units.Healer(team, 50, 0, 0, 0)

    def create_shield(self, team: units.Team) -> units.Shield:
        return units.Shield(team, 300)
