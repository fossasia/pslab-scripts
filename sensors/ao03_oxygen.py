import serial

def measure_oxygen(psl):
    """
    Measuring the percentage of oxygen in the air by integrating the AO-03 sensor
    in a custom amplifier circuit and transforming the output voltage.
    """
    try:
        v_out = psl.multimeter.measure_voltage("CH1")
    except serial.SerialException:
        return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
    oxygen = v_out * 58
    return oxygen
