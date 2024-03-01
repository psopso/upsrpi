from __future__ import annotations

"""Platform for sensor integration."""
import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from .readvoltage import readVoltage
from .readcapacity import readCapacity

from .const import DOMAIN

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
    PLATFORM_SCHEMA,
)
from homeassistant.const import UnitOfElectricPotential
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

CONF_VAR1 = "upsrpiaddress"
CONF_VAR2 = "var2"

from homeassistant.const import PERCENTAGE

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
   {
       vol.Required(CONF_VAR1): cv.string,
       vol.Optional(CONF_VAR2, default="df"): cv.string,
   }
   )

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    upsrpiaddress = config[CONF_VAR1];
    add_entities([VoltageSensor(upsrpiaddress),CapacitySensor()])

class VoltageSensor(SensorEntity):
    """Representation of a Sensor."""
    def __init__(self, upsrpiaddress) -> None:
      super().__init__()
      self.upsrpiaddress = upsrpiaddress
    _attr_name = "UPS Voltage"
    _attr_native_unit_of_measurement = UnitOfElectricPotential.VOLT
    _attr_device_class = SensorDeviceClass.VOLTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = readVoltage()
        _LOGGER.warning("Debug Domain: "+DOMAIN+"::"+self.upsrpiaddress)

class CapacitySensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "UPS Capacity"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = readCapacity()
