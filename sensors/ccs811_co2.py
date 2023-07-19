import time
import serial
from sensors.driver_ccs811 import CCS811

class CO2_Sensor:
    """
    Using the CCS811 with its custom driver to retrieve the CO2e value of the air.
    As this is an I2C sensor, the cabling is fixed to the corresponding I2C pins of the PSLab.
    """
    dev = CCS811()

    def __init__(self):
        time.sleep(0.05)
        self.dev.app_start()
        time.sleep(1)
        self.dev.set_measure_mode(CCS811.MODE_CONTINUOUS)
        # skip the first 4 results, which are all zeros
        for _ in range(4):
            time.sleep(1)
            self.dev.measure()

    def measure_co2(self):
        try:
            ret = self.dev.measure()
        except serial.SerialException:
            return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
        CO2e = ret['eCO2']
        return CO2e
    
def measure_co2(sensor):
    return sensor.measure_co2()