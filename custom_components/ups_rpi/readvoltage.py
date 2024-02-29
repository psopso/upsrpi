#!/usr/bin/env python

import logging
import struct
import sys
import time

from smbus2 import SMBus

_LOGGER = logging.getLogger(__name__)

bus = SMBus(1)

_LOGGER.warning("Debug readvoltage")