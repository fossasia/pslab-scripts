import math
import serial

V_IN = 3.3
R2 = 10000 # ohm of the second resistor

def measure_light_intensity(psl):
    """
    Measuring the light intensity in lux by integrating the GL5528
    photo-resistor into a voltage divider circuit and transforming the output voltage.
    The lux formula is derived by measuring r1 at known levels of light intensity and deriving
    the parameters a&b to form a logarithmic function (as described in the sensor's data sheet).
    """
    try:
        v_out = psl.multimeter.measure_voltage("CH1")
    except serial.SerialException:
        return 0 # measurement is still continued, even if an exception occurred (usually just a temporary error)
    r1 = R2 * v_out / (V_IN - v_out)
    if r1 < 0:
        return 0
    else:
        lux = math.pow(math.e, 14.3316 - 1.1713 * math.log(r1, math.e))
    return lux
