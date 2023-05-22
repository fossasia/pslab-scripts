# PSLab

This repo is used for scripts and operators to run and collect data of specific sensors connected with the PSLab.

[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab-sister?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Twitter Follow](https://img.shields.io/twitter/follow/pslabio.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/pslabio)

PSLab is a tiny pocket science lab that provides an array of equipment for doing science and engineering experiments. It can function like an oscilloscope, waveform generator, frequency counter, programmable voltage and current source and also as a data logger. Our website is at https://pslab.io

## The PSLab Sensor Box

![PSLab Sensor Box](/docs/images/phone_connections.jpg)

In this project four different experimental setups of the [PSLab version 5](https://pslab.io/wp-content/uploads/PSLab-Data-Sheet.pdf) are created with each one sensor. Besides those sensors, which are described in detail [here](/sensors/), the following **hardware components** are connected to the PSLabs:

- A **Raspberry Pi Zero W** to store the sensor data permanently on an SD card and at the same time make this data available via the Raspberry Pi's WiFi module. The "Zero" is especially handy here, as it is the most lightweight Raspberry Pi version.
- A **Button** to safely shutdown the Raspberry Pi. It needs to be long pressed for at least one second in order to trigger the device's shutdown. Here, one terminal is plugged into GPIO pin 27, while the other terminal is plugged to the ground (**black** marked pins).
- The high accuracy I2C **real time clock (RTC)** model [DS3231](https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231.pdf). It contains a small battery and ensures that the device's time progresses, even if the main power source is unavailable. This RTC therefore makes timestamps in the output data possible, even during times where the PSLab sensor box can not access the Internet. The five pins of this pi hat are plugged into the **red** marked pins.

<img src="/docs/images/raspiZero_coloured_pins.png" alt="Color coded button + rtc connection" width="70%">

Additionally the following **features** are implemented:
- Each PSLab sensor box automatically opens its own WiFi Hotspot once the system is connected to an energy source and finished the booting process (which may take one or two minutes).
- Also, the measurement it triggered automatically after startup. This is done by a custom [systemd](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/) service.
- Each measured data point is then written into a CSV file with the structure `<timestamp>, <measured_value>, <unit>, <item_name>`.
- A samba file sharing server that makes the folder "/home/foss/data" of the Raspberry Pi publicly available to all devices within the PSLab Box' WiFi Hotspot. This also enables the user to modify or delete the measurement data on the PSLab sensor box right via their PC or mobile phone.
- The measurements are supplied to the file sharing server in real-time, however they are also stored there permanently via the SD card. The user can thus combine the benefits of both measurement forms.
- The Raspberry Pi itself is currently running the code from the master branch this Github repository. So in case of code changes, a simple "git pull" on the device (while it's connected to the internet) will update all code accordingly.

## Basic Usage

Once a power source (power bank or cord to electricity outlet) is connected to the PSLab sensor box and the device has fully booted, a new measurement is automatically started. The measurement results are now collected in a CSV and can be exported in real time from the file server via WiFi:
1. Connect your computer or smartphone to the WiFi Hotspot with the corresponding name (like "PSLab.Light.01"). A detailed manual on how to connect for the first time can be found [here](/docs/network_connection_manual.md).
2. Access the "**data**" folder and fetch some CSV measurement data file. This file can for example be opened by Excel or just a normal text editor. The current measurement file is updated automatically every few seconds.
3. This data can now for example be imported into Jupiter Notebooks to perform some analysis tasks.

To trigger the shut down of the PSLab sensor box, please press the attached button for one to two seconds.

## Advanced Modifications/ Usage

First of all, as part of the open hardware approach we obviously want you to be able to check out the electronics inside the device. As as a disclaimer: do **not** open the box with brute force. There is a trick in opening it by angling out the lid from the lower side. This works even better when using a screw driver.
<img src="/docs/images/open_box.jpeg" alt="Opening the Lid" width="70%">

In order to modify the software, the data on the Raspberry Pi's SD card needs to be accessed, as all the scrips for the PSLab are stored on there. This can either be done by plugging the SD card into a computer or by connecting a monitor (to the microHDMI slot), mouse and keyboard (usually via and USB hub to the inner microUSB slot) to the Raspberry Pi. As the SD card stored the whole Raspberry Pi operating system and not just single files, the second option is usually preferable. In any case, the SD card should never be cleared fully, as this would delete the operating system and therefore stop the Raspberry Pi from working.

As the pslab-python package is already installed on the device, no more preparation is needed. To debug the python scrips, they can just be run by typing `“python3 /home/foss/code/init_pipe.py <experiment type>”` in the terminal and watching the outcomes. Some small custom modifications could for example be:

### Adjusting the measurement interval
Currently a new data point is retrieved from the sensor every second. This can be changed by adjusting the measuring_interval parameter in [measure.py](/measure.py). The file can be found at `/home/foss/pslab-scripts/measure.py` on the Raspberry Pi.

### Adjusting the flushing interval
Currently the data points are flushed into the CSV file after every 10 measurements. This can be changed by adjusting the flushing_threshold parameter in [store_data.py](/store_data.py). The file can be found at `/home/foss/pslab-scripts/store_data.py` on the Raspberry Pi.

### Fetching a software update from Github
1. Open a terminal and the folder "pslab-scripts" by typing `cd /home/foss/pslab-scripts`
2. Disconnect from the PSLab sensor boxes' WiFi Hotspot and connect the device to a WiFi that actually provides internet. Don't forget to eventually re-connect to its own WiFi Hotspot again, as the file server will otherwise not be accessible.
3. Type `git pull` in the terminal to fetch the new changes in software

### Changing the sensor type
By adjusting the experiment type parameter in the systemd service "startup.service", the supported sensor type of this PSLab sensor box can be changed easily:
1. Open a terminal.
2. Type `sudo nano /lib/systemd/system/startup.service`.
3. The "startup.service" file is now opened in a simple text editor. Here, you can now adjust the experiment type parameter, eg. from "light" to "CO2", in case the PSLab sensor box for light shall now be used with a CO2 sensor. The full list of currently supported parameters can be found [here](/measure.py).
4. Save the changes by Ctrl+o. Exit the editor by Ctrl+x.
5. The changes take effect once the device is rebooted. This can for example be done by `sudo reboot`.
In case of unexpected errors, the logs of the startup script can then be obtained by `journalctl -u startup.service -n`.

## Repository Structure

```
📦pslab-scripts
 ┣ 📂docs                                   # Supplementary material
 ┃ ┣ 📂ao-03_amplifier_circuit_design       # Design files of the custom circuit board for the AO-03 sensor
 ┃ ┃ ┗ 📜 ...
 ┃ ┣ 📂images
 ┃ ┃ ┗ 📜 ...
 ┃ ┣ 📜network_connection_manual.md         # Manual on how to connect a device to the PSLab's file server
 ┃ ┗ 📜sensor_logos.svg                     # Stickers for the boxes (made with Inkscape)
 ┣ 📂sensors                                # Contains a specific run script for every sensor
 ┃ ┣ 📜ao03_oxygen.py
 ┃ ┣ 📜ccs811_co2.py
 ┃ ┣ 📜gl5528_light.py
 ┃ ┗ 📜lm35_temp.py
 ┣ 📜init_pipe.py                           # Main project file
 ┣ 📜measure.py
 ┣ 📜store_data.py
 ┗ 📜shutdown.py                            # Script for the button logic
```
## Buy

* You can get a Pocket Science Lab device from the [FOSSASIA Shop](https://fossasia.com).
* More resellers are listed on the [PSLab website](https://pslab.io/shop/).

## Communication

* The PSLab [chat channel is on Gitter](https://gitter.im/fossasia/pslab).
* Please also join us on the [PSLab Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia).

## Site

The website is hosted on [pslab.io](http://pslab.io).