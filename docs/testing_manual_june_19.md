# Manual for Testing the PSLab Sensor Box Prototypes

The received parcels contain different cardboard boxes with each one device. There are:

- PSLab Sensor Box to [measure Oxygen](./sensors.md#oxygen-sensor-ao-03)
- PSLab Sensor Box to [measure CO2](./sensors.md#co2e-sensor-ccs811)
- PSLab Sensor Box to [measure the temperature](./sensors.md#temperature-sensor-lm35)
- PSLab Sensor Box to [measure light intensity in Lux](./sensors.md#light-intensity-sensor-gl5528)

For each of them the following steps can be executed to test their functionality:

## Opening the Boxes

After opening the paper box, the plastic boxes need to be opened, in order to access the
USB charging connector, the sensor and the power off button. In the final version, those
three items will be exposed outside the box, however right now they are still hidden inside. Opening the plastic box can seem a bit tricky at first, but by angling out the lid from the lower edge (see the description in [advanced usage](../README.md#advanced-usage)) it becomes fairly easy.

<p align="center">
    <img src="./images/exposed_connections.jpeg" alt="Exposed Connections" width="50%">
</p>

## Measuring and Evaluating the Data

Once the box is open and the important parts are exposed, an electricity supply can
be connected to the USB plug. This can for example be a power bank or a laptop. The Raspberry Pi now boots. Please wait a minute for this process to finish.

While the first four devices still use the mechanism to store the measurement data in a CSV
file, those newer devices directly send the data over to a receiver device via the OSC protocol. Therefore the two charges of devices have to be handled differently:

### Older Devices from June 12

- The successfully finished booting process is indicated by a WiFi Hotspot opening up: Please check
on your phone or PC for a new WiFi access point named "PSLab<...>".
- If there is no such WiFi Hotspot visible: Try using another power source for the
PSLab Sensor Box and maybe even another USB charging cable. Please note, that the
glowing lights on the PSLab/ Raspberry Pi do not guarantee a sufficient electricity
supply for all of the device's functionalities.
- Once this WiFi Hotspot can be detected, a connection needs to be established by following the
[connection guide](./network_connection_manual.md). Please make sure to read the
[general disclaimers](./network_connection_manual.md#general-disclaimers) thoroughly,
as those tips can prevent most common issues.

- When booting, the Raspberry Pi created a new measurement file for this session
and directly began to add a new measurement value every second. This file can be found
when accessing the "data" folder within the shared directory of the PSLab sensor box.
More information on this can be found [here](../README.md#basic-usage).
- Now identify the most recent measurement by looking for the file name with the
highest number.
- Test the continuous data serving functionality by opening thus current measurement
file, scrolling down to check the last time stamp, closing the file and opening it again
after a few seconds to check & compare the last time stamp.

### Newer Devices from June 19

- In this version, the device does not open an own WiFi Hotspot, but instead connects to a public
WiFi, in order to make multiple devices accessible at once within one network. Therefore, the devices first need to be connected to a common WiFi access point. This connection is automatically done, once the Raspberry Pi remembers the WiFi, however the first setup needs to be executed manually by connecting the Raspberry Pi to a monitor (as explained [here](../README.md#using-the-raspberry-pi-as-an-independent-computer)) and adding the new network.
- Alternatively, a dummy connection with the credentials "myHotspot" as the SSID and "password123" as the password is already set up. Therefore the device can be tested by just opening a Hotspot from your phone/PC with those credentials. The PSLab Sensor Box will then automatically connect with this network, no monitor connection needed. In case of connection errors, try restarting the Raspberry Pi.
- The PSLab Sensor Box now sends OSC data within this WiFi network. Currently, the receiver of this OSC data is at IP address 192.168.173.152, however this can be edited in the osc_sharing.py file (by connecting the PSLab Sensor Box to a monitor or accessing it via SSH, as described [here](../README.md#accessing-the-data-on-the-raspberry-pi)). A simple server to receive the OSC messages on a PC using python is explained [here](../README.md#receiving-the-osc-messages).

## Up Next

- Detailed information on accessing/ modifying the code and debugging can be found [here](../README.md#advanced-usage).
- Please report all detected bugs and problems to our team.
- We are eager to come over to Weimar to resolve any
remaining issues and give a workshop on how to use the device's full potential.
