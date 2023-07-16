import serial

def measure_temperature(psl,channel="CH1"):
    """
    Measuring the temperature of the air by using a LM35 sensor.
    According to the sensor's data sheet the output voltage * 100 then equals to
    the temperature in degree Celsius.
    The analog output of the sensor is connected to channel 1 by default.
    """
    try:
        v_out = psl.multimeter.measure_voltage(channel)
    except serial.SerialException:
        return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
    temperature = v_out * 100
    return temperature