from abc import ABC, abstractmethod

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = SpindlerBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_servie_mileage):
        car_engine = WilloughbyEngine(current_mileage, last_servie_mileage)
        car_battery = SpindlerBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        car_engine = SternmanEngine(warning_light_is_on)
        car_battery = NubbinBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_rorchach(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)

    @staticmethod
    def create_throvex(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)
