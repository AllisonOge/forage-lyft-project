from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

