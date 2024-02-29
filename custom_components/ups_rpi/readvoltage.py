#!/usr/bin/env python

import struct
#import smbus
import sys
import time
from smbus2 import SMBus

def readVoltage(bus):
     address = 0x36
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage


bus = SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
#print ("%5.2f" % readVoltage(bus))