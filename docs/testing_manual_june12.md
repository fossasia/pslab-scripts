# Manual for Testing the PSLab Sensor Box Prototypes

The received parcel contains four different cardboard boxes with each one device:

- one PSLab Sensor Box to [measure Oxygen](./sensors.md#oxygen-sensor-ao-03)
- one PSLab Sensor Box to [measure CO2](./sensors.md#co2e-sensor-ccs811)
- one PSLab Sensor Box to [measure the temperature](./sensors.md#temperature-sensor-lm35)
- one PSLab Sensor Box to [measure light intensity in Lux](./sensors.md#light-intensity-sensor-gl5528)

For each of them the following steps can be executed to test their functionality:

## Opening the Boxes

After opening the paper box, the plastic boxes need to be opened, in order to access the
USB charging connector, the sensor and the power off button. In the final version, those
three items will be exposed outside the box, however right now they are still hidden inside. Opening the plastic box can seem a bit tricky at first, but by angling out the lid from the lower edge (see the description [here](../README.md#advanced-usage)) it becomes fairly easy.

<p align="center">
    <img src="./images/exposed_connections.jpeg" alt="Exposed Connections" width="50%">
</p>

## Startup and Establishing a Connection

- Once the box is open and the important parts are exposed, an electricity supply can
be connected to the USB plug. This can for example be a power bank or a laptop.
- The Raspberry Pi now boots. Please wait a minute for this process to finish.
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

## Collecting Measurement Data

- When booting, the Raspberry Pi created a new measurement file for this session
and directly began to add a new measurement value every second. This file can be found
when accessing the "data" folder within the shared directory of the PSLab sensor box.
More information on this can be found [here](../README.md#basic-usage).
- Now identify the most recent measurement by looking for the file name with the
highest number.
- Test the continuous data serving functionality by opening thus current measurement
file, scrolling down to check the last time stamp, closing the file and opening it again
after a few seconds to check & compare the last time stamp.

## Ending the Measurement

To finish the measurement session, the device needs to be shut down. This can
simply be done by just unplugging the power source, however in the long term,
this technique can be harmful for the Raspberry Pi's file system. We therefore decided to
attach a button to the PSLab Sensor Box. Please press this button for one to two seconds
to trigger the shutdown process of the Raspberry Pi. As that process needs 20-30 seconds,
it is important to wait a bit (until the Raspi's lights went off)
before finally unplugging the electricity source.

## Up Next

- Detailed information on accessing/ modifying the code and debugging can be found [here](../README.md#advanced-usage).
- Please report all detected bugs and problems to our team.
- We are currently working on the next version of the PSLab Sensor Boxes that will support the OSC protocol, as
well as the functionality to connect multiple devices at once to a (public)
WiFi network. This new version will arrive in Weimar until June 17.
- Once this OSC version is ready, we are eager to come over to Weimar to resolve any
remaining issues and give a workshop on how to use the device's full potential.
