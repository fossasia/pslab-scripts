import time
import pslab

from sensors.ccs811_co2 import measure_co2
from sensors.AO03_oxygen import measure_oxygen
from sensors.GL5528_light import measure_light_intensity
from sensors.HDC1080_temp import measure_temperature

MEASURING_INTERVAL = 1 # in seconds

experiment_options = { # [function_name, unit]
    "co2"       : [measure_co2, "ppm"],
    "oxygen"    : [measure_oxygen, "%"],
    "light"     : [measure_light_intensity, "lux"],
    "temp"      : [measure_temperature, "°C"]
    }
    
def connect_to_pslab():
    """ Establishes the connection to the pslab. """
    try:
        psl = pslab.ScienceLab()
    except serial.SerialException: # device not found
        time.sleep(1)
        try:
            psl = pslab.ScienceLab() # retry: usually it just needs a second chance
        except serial.SerialException: # give up, in case that again did not work
            print("PSLab cannot be accessed.")
            return None
    return psl

def get_data_pslab(connection, experiment_type):
    """ Periodically fetches measurements from the sensor and forwards them via the pipeline. """
    while True:
        psl = connect_to_pslab()
        if psl is None:
            return None
        while True:
            measurement = experiment_options[experiment_type][0](psl)
            if measurement != 0:
                connection.send(measurement)
                time.sleep(MEASURING_INTERVAL)
            else:
                time.sleep(10)
                break # try to reconnect
