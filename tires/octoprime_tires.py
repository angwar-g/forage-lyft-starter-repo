from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_sensor_values):
        self.tire_sensor_values = tire_sensor_values
    
    def needs_service(self):
        sum = 0 
        for value in self.tire_sensor_values:
            sum = sum + value
        if sum >= 3:
            return True
        else:
            return False