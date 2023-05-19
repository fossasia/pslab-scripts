#!/usr/bin/python3
# pslab-scripts/sensors/ccs811_co2.py.py

import time

from pslab.external.ccs811 import CCS811
dev = CCS811()
time.sleep(0.05)


print('dev.appStart()')
dev.appStart()
sleep_time = 1
print(f"sleep {sleep_time} seconds")
time.sleep(sleep_time)

# time.sleep(1)
print("dev.setMeasureMode(CCS811.MODE_CONTINUOUS)")
dev.setMeasureMode(CCS811.MODE_CONTINUOUS)

# skip the first 4 results, which are all zeros
for i in range(4):
    time.sleep(1)
    dev.measure()

while (1):
    time.sleep(1)
    ret = dev.measure()
    status = ret['status']
    print("eCO2 = %f, eTVOC = %f)" % (ret['eCO2'], ret['eTVOC']))
    print(dev.decodeStatus(status))
