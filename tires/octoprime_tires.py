from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_sensor_values):
        self.tire_sensor_values = tire_sensor_values
    
    def needs_service(self):
        return sum(self.tire_sensor_values) >= 3.0