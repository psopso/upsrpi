DOMAIN = "ups_rpi"
_LOGGER = logging.getLogger(__name__)

import logging
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import threading

CONF_VAR1 = "var1"
CONF_VAR2 = "var2"

REQ_LOCK = threading.Lock()
CONFIG_SCHEMA = vol.Schema(
	{
		DOMAIN: vol.Schema({
			vol.Required(CONF_VAR1): cv.string,
			vol.Optional(CONF_VAR2, default=9600): cv.positive_int,
		})
	},
	extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass, config):
    conf = config[DOMAIN]
	var1 = conf.get(CONF_VAR1)
	var2 = conf.get(CONF_VAR2)
    print("Debug: "+var1) 
#    hass.states.async_set("hello_state.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
