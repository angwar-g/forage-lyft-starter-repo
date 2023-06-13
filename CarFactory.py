import Car

from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine
from battery import NubbinBattery
from battery import SpindlerBattery

class CarFactory(Car):

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        Calliope = Car(CapuletEngine, SpindlerBattery)
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        Glissade = Car(WilloughbyEngine, SpindlerBattery)
    def create_palindrome(current_date, last_service_date, warning_light_on):
        Palindrome = Car(SternmanEngine, SpindlerBattery)
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        Rorschach = Car(WilloughbyEngine, NubbinBattery)
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        Thovex = Car(CapuletEngine, NubbinBattery)
