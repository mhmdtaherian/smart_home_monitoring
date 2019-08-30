import _const as const
import sys
import psutil
from _util import get_sensor, secs2hours 

def get_battery():

    if not hasattr(psutil, 'sensors_battery'):
        return []
    batt = psutil.sensors_battery()
    if batt is None:
        return []

    sensors = []
    sensors.append(get_sensor(const.SENSOR_NAME_BATTERY_PERCENT, round(batt.percent, 2)))

    if batt.power_plugged:
        sensors.append(get_sensor(const.SENSOR_NAME_BATTERY_POWER_PLUGGED, 1))
    else:
        sensors.append(get_sensor(const.SENSOR_NAME_BATTERY_POWER_PLUGGED, 0))
        sensors.append(get_sensor(const.SENSOR_NAME_BATTERY_LEFT, secs2hours(batt.secsleft)))

    return sensors
