from abc import ABC, abstractmethod


class IPerker(ABC):
    @abstractmethod
    def perk(self):
        raise NotImplementedError
