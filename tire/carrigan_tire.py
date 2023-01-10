from ..interfaces import Tire

class CarriganTire(Tire):
    def __init__(self, sensor_values):
        self.sensor_values = sensor_values
        
    def needs_service(self):
        counts = len([val for val in self.sensor_values if val >= 0.9])
        if counts >= 1:
            return True
        else:
            return False