import psutil
import _const as const
from _util import get_sensor, to_mega_byte

def get_sensors_for_memory(nt, prefix):
    sensors = []
    space_values = {}
    for name in nt._fields:
        value = getattr(nt, name)
        
        if name != 'percent':
            space_values[name.capitalize()] = to_mega_byte(value)
        else:
            percent_value = value
        
    sensors.append(get_sensor(prefix + const.SENSOR_NAME_MEMORY_SPACE, space_values))
    sensors.append(get_sensor(prefix + const.SENSOR_NAME_MEMORY_PERCENT, percent_value))

    return sensors


def get_memory():
    sensors_virtual = get_sensors_for_memory(psutil.virtual_memory(), const.DEVICE_NAME_MEMORY_VIRTUAL)
    sensors_swap = get_sensors_for_memory(psutil.swap_memory(), const.DEVICE_NAME_MEMORY_SWAP)
    return sensors_virtual + sensors_swap
