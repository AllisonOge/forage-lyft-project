from ..interfaces import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensor_values):
        self.sensor_values = sensor_values

    def needs_service(self):
        if sum(self.sensor_values) >= 3.0:
            return True
        else:
            return False