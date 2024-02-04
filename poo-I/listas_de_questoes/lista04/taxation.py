from abc import ABC, abstractmethod


class Taxation(ABC):
    @abstractmethod
    def calculate_taxation():
        pass
