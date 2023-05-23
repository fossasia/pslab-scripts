# PSLab

This repo is used for scripts and operators to run and collect data of specific sensors connected with the PSLab.

[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab-sister?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Twitter Follow](https://img.shields.io/twitter/follow/pslabio.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/pslabio)

PSLab is a tiny pocket science lab that provides an array of equipment for doing science and engineering experiments. It can function like an oscilloscope, waveform generator, frequency counter, programmable voltage and current source and also as a data logger. Our website is at https://pslab.io

## The PSLab Sensor Box

<p align="center">
    <img src="/docs/images/phone_connections.jpg" alt="PSLab Sensor Box" width="75%">
</p>

In this project four different experimental setups of the [PSLab v5](https://pslab.io/wp-content/uploads/PSLab-Data-Sheet.pdf) are created, each incorporating a different sensor. Besides those sensors, which are described in detail [here](/sensors/), the following **hardware components** are connected to the PSLabs:

- A **Raspberry Pi Zero W** to store the sensor data permanently on an SD card and at the same time make this data available via the Raspberry Pi's WiFi module. The "Zero" is especially handy here, as it is the most lightweight Raspberry Pi version.
- A **Button** to safely shutdown the Raspberry Pi. It needs to be long pressed for at least one second in order to trigger the device's shutdown. Here, one button terminal is plugged into GPIO pin 27, while the other terminal is plugged to the ground.
- The high accuracy I²C **real time clock (RTC)** model [DS3231](https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231.pdf). It contains a small battery and ensures that the device's time progresses, even if the main power source is unavailable. This RTC therefore makes timestamps in the output data possible, even during times where the PSLab sensor box can not access the internet. The five pins of this Pi HAT are plugged into pins 1 (3.3V power), 3 (SDA I²C), 5 (SCL I²C), 7 and 9 (ground) of the Raspberry Pi Zero W.

Additionally the following **features** are implemented:
- Each PSLab sensor box automatically opens its own WiFi Hotspot, once the system is connected to an energy source and finished its booting process (which may take one or two minutes).
- Additionally, the measurement it triggered automatically after startup. This is done by a custom [systemd](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/) service.
- Each measured data point is then written into the CSV file of this measurement session. The file is structured as `<timestamp>, <measured_value>, <unit>, <item_name>`.
- A [samba file sharing server](https://raspberrypi-guide.github.io/filesharing/filesharing-raspberry-pi) makes the folder "/home/foss/data" of the Raspberry Pi publicly available to all devices within its WiFi Hotspot. This also enables users to modify or delete the measurement data within this folder remotely via their PC or mobile phone.
- The measurements are provided to this file sharing server in real-time, however they are also stored there permanently via the SD card. The user can thus combine the benefits of both measurement forms.
- The Raspberry Pi itself is currently running the code from the master branch this Github repository. This makes code updates easy to distribute on all devices. All PSLab sensor boxes run the exact identical code, with the only difference being the experiment type parameter with which `init_pipe.py` is called in the systemd service.

## Basic Usage

Once a power source (power bank or cord to electricity outlet) is connected to the PSLab sensor box and the device has fully booted, a new measurement is automatically started. The measurement results are now collected in a CSV and can be exported in real time from the file server via WiFi:
1. Connect your computer or smartphone to the WiFi Hotspot with the corresponding name (like "PSLab.Light.01"). A detailed manual on how to connect for the first time can be found [here](/docs/network_connection_manual.md).
2. Access the "data" folder and fetch some CSV measurement data file. This file can for example be opened by Excel or just a normal text editor. The current measurement file is updated automatically every few seconds.
3. Analysis tasks can now be performed on this data, for example importing it into [Jupyter Notebook](https://jupyter.org/).

To trigger the shut down process of the PSLab sensor box, please press the attached button for one to two seconds.

## Advanced Usage

First of all, as part of the open hardware approach, we obviously want you to be able to check out the electronics inside the device. As as a disclaimer: do **not** open the box with brute force. There is a trick in opening it by angling out the lid from the lower side. This works even better when using a screw driver.
<p align="center">
    <img src="/docs/images/open_box.jpeg" alt="Opening the Lid" width="50%">
</p>

In order to modify the software, the data on the Raspberry Pi's SD card needs to be accessed, as all the scrips for the PSLab are stored on there. This can either be done by plugging the SD card into a computer or by using the Raspberry Pi as a computer itself: connect a monitor to the microHDMI slot and mouse + keyboard via an USB hub to the inner microUSB slot of the Raspberry Pi. As the second option provides a graphical user interface for editing and debugging, it is usually preferable for beginners. In any case, the SD card should never be cleared fully, because this would delete the operating system and therefore stop the Raspberry Pi from working.

As python3 and the pslab-python package are already installed on the Raspberry Pi, no additional installation is needed here. To debug the python scrips, the full code can be run by typing `python3 /home/foss/code/init_pipe.py <experiment type>` in the terminal and watching the outcomes. Some small custom modifications could for example be:

### Adjusting the measurement interval
Currently a new data point is retrieved from the sensor every second. This can be changed by adjusting the measuring_interval parameter in [measure.py](/measure.py). The file can be found at `/home/foss/pslab-scripts/measure.py` on the Raspberry Pi.

### Adjusting the flushing interval
The data points are flushed into the CSV file after every 10 measurements in the current implementation. To change this, the flushing_threshold parameter in [store_data.py](/store_data.py) at `/home/foss/pslab-scripts/store_data.py` can be adjusted.

### Accessing the continuous measurement data stream via an API
As of now, the measurement data is redirected into a CSV file by the pipe function in [init_pipe.py](/init_pipe.py). This can however be modified freely, for example by replacing the "storing" process, with a process that transforms the data and directly outputs it. This new process will always receive the measurement data points via its connection parameter (see [store_data.py](/store_data.py)).

### Fetching a software update from Github
1. Open the terminal.
2. Open the folder "pslab-scripts" by typing `cd /home/foss/pslab-scripts`.
3. Disconnect from the PSLab sensor boxes' WiFi Hotspot and connect the device to a WiFi that actually provides internet. Don't forget to eventually re-connect to its own WiFi Hotspot again, as the file server will otherwise not be accessible.
4. Enter `git pull` in the terminal to fetch the new changes in software.

### Changing the sensor type
By adjusting the experiment type parameter in the systemd service "startup.service", the supported sensor type of this specific PSLab sensor box can be changed easily:
1. Open a terminal.
2. Type `sudo nano /lib/systemd/system/startup.service`.
3. The "startup.service" file is now opened in a simple text editor. Here, you can adjust the experiment type parameter, e.g. from "light" to "co2", in case the PSLab sensor box for light shall now be used with a CO2 sensor. The full list of currently supported parameters can be found [here](/measure.py).
4. Save the changes by pressing Ctrl+o. Exit the editor by pressing Ctrl+x.
5. The changes take effect once the device is rebooted. This can for example be done by `sudo reboot`.

In case of unexpected errors, the logs of the startup script can be obtained by entering `journalctl -u startup.service -n` in the terminal.

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