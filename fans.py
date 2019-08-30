import _const as const
import psutil
from _util import get_sensor, secs2hours 

def get_fans():

    sensors = [] 

    if not hasattr(psutil, "sensors_fans"):
        return sensors
    fans = psutil.sensors_fans()
    if not fans:
        return sensors

    sensor_values = {}

    for name, entries in fans.items():
        for entry in entries:
            sensor_values[const.SENSOR_NAME_FANS_FORMAT.format(name, entry.label)] = entry.current
    
    sensors.append(get_sensor(const.SENSOR_NAME_FANS, sensor_values))

    return sensors
