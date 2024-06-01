from abc import ABC, abstractmethod

from units import Base


class IPerker(ABC):
    @abstractmethod
    def perk(self, attack_team: list[Base], defense_team: list[Base]) -> bool:
        raise NotImplementedError
