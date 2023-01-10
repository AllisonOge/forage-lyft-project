from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from .car import Car


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
