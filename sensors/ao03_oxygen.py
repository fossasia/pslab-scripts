import serial

def measure_oxygen(psl,channel="CH1"):
    """
    Measuring the percentage of oxygen in the air by integrating the AO-03 sensor
    in a custom amplifier circuit and transforming the output voltage.
    The analog output of the sensor is connected to channel 1 by default.
    """
    try:
        v_out = psl.multimeter.measure_voltage(channel)
    except serial.SerialException:
        return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
    oxygen = v_out * 64
    return oxygen
