# PSLab

This repo is used for scripts and operators to run and collect data of specific sensors connected with the PSLab.

[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab-sister?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Twitter Follow](https://img.shields.io/twitter/follow/pslabio.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/pslabio)

PSLab is a tiny pocket science lab that provides an array of equipment for doing science and engineering experiments. It can function like an oscilloscope, waveform generator, frequency counter, programmable voltage and current source and also as a data logger. Our website is at https://pslab.io

## The PSLab Sensorbox

In this project four, different configurations of the [PSLab version 5](https://pslab.io/wp-content/uploads/PSLab-Data-Sheet.pdf) are created with each one sensor. Besides those sensors, which are described in detail [here](/sensors/), the following components are used:

- Raspberry Pi Zero W: to enable both, the real-time and batch, supply with measurements by integrating its SD card reader and WiFi module. The "Zero" is especially handy here, as it is the most lightweight Raspberry Pi version.
- Button to safely shutdown the Raspberry Pi. It needs to be long pressed for at least one second in order to trigger the device's shutdown. Wiring: one terminal to GPIO pin 27, the other terminal to the ground.
- Real Time Clock (RTC) [DS3231](https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231.pdf)

## Usage

Once a power source (power bank or cord to electricity outlet) is connected to the PSLab sensor box, a new measurement is automatically started. The measurement results can now be obtained in real time from the file server via WiFi:
1. Connect your computer or smartphone to the WiFi Hotspot with the corresponding name (like "PSLab.CO2.01). A detailed manual on how to connect for the first time can be found [here](/docs/connect_lan_device.md).
2. Fetch an CSV data file by accessing the "data" folder
3. The measurement data is now available in the form <timestamp>, <measured_value>, <unit>, <item_name>. The current measurement file is updated automatically every few seconds.

## Buy

* You can get a Pocket Science Lab device from the [FOSSASIA Shop](https://fossasia.com).
* More resellers are listed on the [PSLab website](https://pslab.io/shop/).

## Communication

* The PSLab [chat channel is on Gitter](https://gitter.im/fossasia/pslab).
* Please also join us on the [PSLab Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia).

## Site

The website is hosted on [pslab.io](http://pslab.io).