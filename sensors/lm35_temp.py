import serial

def measure_temperature(psl):
    """
    Measuring the temperature of the air by using a LM35 sensor.
    According to the sensor's data sheet the output voltage * 100 then equals to
    the temperature in degree Celsius.
    """
    try:
        v_out = psl.multimeter.measure_voltage("CH1")
    except serial.SerialException:
        return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
    temperature = v_out * 100
    return temperature