import _const as const
from _util import get_sensor
import psutil

def get_cpus():
    return [get_sensor(const.SENSOR_NAME_CPU_USAGE, psutil.cpu_percent())]