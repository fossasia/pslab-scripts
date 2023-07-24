# Casing

As part of open source approach, we want to provide a casing for the PSLab Sensor
Boxes that is individually re-creatable and editable at home.
We therefore decided to design 3d printed boxes with a removable side lid.
To securely keep the PSLab and the Raspberry Pi in place, we furthermore designed a
lasercut acrylic shield to attach the technology onto.
This shield can then be slid tightly into the rail system of the box.
As acrylic often slightly varies in thickness there are two slightly different box options with
differing rail sizes: please measure your acrylic first and then print the suitable box for it.

To make the box splashproof, a special sealing was screwed in place for the output point of the sensor cable.
Also, a USB to USB c in socket was installed to simplify attaching the device to a power source.

<p align="center">
    <img src="/docs/images/box_side.jpeg" alt="Casing" width="60%">
</p>

## Required Materials

- An 8x14cm piece of 3mm thick acrylic
- About 100g of (PLA) filament for the boxes' body
- About 25g of (PLA) filament for the boxes' lid
- 4 x M2.5 x 10mm screws to attach the PSLab to the shield
- 4 x M2.5 washers to space the PSLab from the shield
- 4 x M2.5 x 20mm Screws to attach the Raspberry Pi to the shield
- 8 x M2.5 x 5mm or 4 x M2.5 x 10mm spacers to position the Raspberry Pi above the PSLab
- 4 x M2.5 nuts to secure the Raspberry Pi
- Optional: USB to USC c in socket, screwable sealing to output the sensor cable

## Folder Structure

```
📂casing
┣ 📂box_rail_3.5mm               # CAD model of the box made for acrylic shields of a thickness between 3.0 and 3.4 mm.
┃ ┣ 📜prusa_printing_code.gcode # This file can directly be printed on a Prusa i3 MK3S with 0.4 nozzle. Made with Prusa Slicer.
┃ ┗ 📜...
┣ 📂box_rail_3mm                 # CAD model of the box made for acrylic shields of a thickness between 2.5 and 2.9 mm.
┃ ┣ 📜prusa_printing_code.gcode # This file can directly be printed on a Prusa i3 MK3S with 0.6 nozzle. Made with Prusa Slicer.
┃ ┗ 📜...
┣ 📂lid                          # CAD model of the boxes' lid.
┃ ┣ 📜prusa_printing_code.gcode # This file can immediately be printed on a Prusa i3 MK3S with 0.4 nozzle. Made with Prusa Slicer.
┃ ┗ 📜...
┣ 📂shield                       # Lasercut model for the acrylic shield. Designed with Inkscape. Compiled with VisiCad for the lasercutter at FabLab, Berlin.
┗  ━ 📜...
```
