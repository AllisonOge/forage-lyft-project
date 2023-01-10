import unittest
from datetime import datetime

from ..battery.spindler_battery import SpindlerBattery
from ..battery.nubbin_battery import NubbinBattery

from ..engine.capulet_engine import CapuletEngine
from ..engine.willoughby_engine import WilloughbyEngine
from ..engine.sternman_engine import SternmanEngine

from ..tire.carrigan_tire import CarriganTire
from ..tire.octoprime_tire import OctoprimeTire


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_values = [0.4, 0.5, 0.6, 0.9]
        tire = CarriganTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_values = [0.4, 0.5, 0.6, 0.8]
        tire = CarriganTire(sensor_values)
        self.assertFalse(tire.needs_service())


class TestOptoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_values = [1.0, 1.0, 0.6, 0.4]
        tire = OctoprimeTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_values = [0.0, 0.5, 0.6, 0.9]
        tire = OctoprimeTire(sensor_values)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
