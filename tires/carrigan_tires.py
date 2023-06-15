from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_sensor_values):
        self.tire_sensor_values = tire_sensor_values
    
    def needs_service(self):
        for value in self.tire_sensor_values:
            if value >= 0.9:
                return True
        return False

