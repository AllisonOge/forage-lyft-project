from .interfaces import Serviceable, Engine, Battery, Tire


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine: Engine = engine
        self.battery: Battery = battery
        self.tire: Tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
