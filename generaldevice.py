import _const as const
import datetime
from sensor import get_sensor
from _util import get_value
from cpu import get_cpus
from disks import get_disks
from memory import get_memory
from battery import get_battery
from fans import get_fans
from net import get_networks
from temperatures import get_temperatures

def get_general_device():
    sensors = []    
    sensors.append(get_sensor(const.SENSOR_NAME_TEMPERATURE, 4, 0, 2, {"value": get_value(20,30)}))
    sensors.append(get_sensor(const.SENSOR_NAME_HUMIDITY, 5, 0, 20, {"value": get_value(30,40)}))
    sensors.append(get_sensor(const.SENSOR_NAME_LIGHT, 11, 0, 2, {"value": get_value(700,800)}))
    sensors.append(get_sensor(const.SENSOR_NAME_PRESSURE, 12, 2, 19, {"value": get_value(900,950)}))
    sensors.append(get_sensor(const.SENSOR_NAME_SOUND, 16, 0, 22, {"value": get_value(50,65)}))

    return sensors

def get_fridge_device():
    sensors = []    
    sensors.append(get_sensor(const.SENSOR_NAME_TEMPERATURE, 4, 0, 2, {"value": get_value(2,7)}))
    sensors.append(get_sensor(const.SENSOR_NAME_HUMIDITY, 5, 0, 20, {"value": get_value(50,60)}))
    sensors.append(get_sensor(const.SENSOR_NAME_LIGHT, 1, 0, 0, {"value": get_value(0,1)}))

    return sensors

def get_bool_device():
    sensors = []
    now = datetime.datetime.now()
    sunrise = now.replace(hour=6, minute=0, second=0, microsecond=0)
    sunset = now.replace(hour=20, minute=0, second=0, microsecond=0)

    if now > sunrise and now < sunset:
        sensors.append(get_sensor(const.SENSOR_NAME_STATUS, 1, 0, 0, {"value": 1}))
    else:
        sensors.append(get_sensor(const.SENSOR_NAME_STATUS, 1, 0, 0, {"value": 0}))

    return sensors  

def generate_device_list():
    devices = [
        {
        'id': const.SENSOR_NAME_SERVER,
        'sensors': get_memory() + get_disks() + get_cpus() + get_battery() + get_networks() + get_fans() + get_temperatures()
        },
        {
        'id': 'MasterBedRoom',
        'sensors': get_general_device() + [get_sensor(const.SENSOR_NAME_SMOKE, 1, 0, 1, {"value": get_value(3,8)}), get_sensor(const.SENSOR_NAME_DOORLOCK, 1, 0, 1, {"value": 1})]
        },
        {
        'id': 'BedRoom-1',
        'sensors': get_general_device() + [get_sensor(const.SENSOR_NAME_SMOKE, 1, 0, 1, {"value": get_value(3,8)}), get_sensor(const.SENSOR_NAME_DOORLOCK, 1, 0, 1, {"value": 0})]
        },
        {
        'id': 'BedRoom-2',
        'sensors': get_general_device() + [get_sensor(const.SENSOR_NAME_SMOKE, 1, 0, 1, {"value": get_value(3,8)}), get_sensor(const.SENSOR_NAME_DOORLOCK, 1, 0, 1, {"value": 0})]
        },
        {
        'id': 'LivingRoom',
        'sensors': get_general_device() + [get_sensor(const.SENSOR_NAME_SMOKE, 1, 0, 1, {"value": get_value(3,8)})]
        },
        {
        'id': 'BackYard',
        'sensors': get_general_device() + [get_sensor(const.SENSOR_NAME_SMOKE, 1, 0, 1, {"value": get_value(10,20)})]
        },
        {
        'id': 'Fridge',
        'sensors': get_fridge_device()
        },
        {
        'id': 'CoffeeMaker',
        'sensors': get_bool_device()
        },
        {
        'id': 'Dryer',
        'sensors': get_bool_device()
        },
        {
        'id': 'Kettle',
        'sensors': get_bool_device()
        },
        {
        'id': 'Washer',
        'sensors': get_bool_device()
        },
        {
        'id': 'DishWasher',
        'sensors': get_bool_device()
        }]

    return devices


