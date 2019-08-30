import sys
import os
import psutil
from _util import get_sensor, to_mega_byte
import _const as const

def get_disks():

    sensors_space = []
    sensor_usage_values = {}

    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)

        sensor_values = {
            const.SENSOR_NAME_DISKS_TOTAL_SPACE: to_mega_byte(usage.total),
            const.SENSOR_NAME_DISKS_USED_SPACE: to_mega_byte(usage.used),
            const.SENSOR_NAME_DISKS_FREE_SPACE: to_mega_byte(usage.free)
        }

        sensor_name_space = const.SENSOR_NAME_DISKS_SPACE.format(part.device)
        sensors_space.append(get_sensor(sensor_name_space, sensor_values))

        sensor_usage_values[part.device] = usage.percent

    sensors_space.append(get_sensor(const.SENSOR_NAME_DISKS_PERCENT_USED, sensor_usage_values))
    
    return sensors_space
