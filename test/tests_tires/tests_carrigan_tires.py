import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_sensor_values = [0.9, 0.9, 0.3, 0.2]
        tires = CarriganTires(tire_sensor_values)
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tire_sensor_values = [0.2, 0.1, 0.3, 0.2]
        tires = CarriganTires(tire_sensor_values)
        self.assertTrue(tires.needs_service())
