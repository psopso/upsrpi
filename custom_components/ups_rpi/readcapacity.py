#!/usr/bin/env python

import struct
import sys
import time
#import smbus
from smbus2 import SMBus


def readCapacity():
     bus = SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
     address = 0x36
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

#print ("%5.2f" % readCapacity(bus))
