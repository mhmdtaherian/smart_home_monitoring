import random

def to_mega_byte(byte_value):
    return int(byte_value / 1048576)

def to_giga_byte(byte_value):
    return int(byte_value / 173741824)

def get_sensor(id, value, sensor_type=None, sensor_unit=None, sensor_prefix=None, dt=None):
    sensor = {
        'id': id,
        'data': value
    }
    if sensor_type is not None:
        sensor.type = sensor_type

    if sensor_unit is not None:
        sensor.unit = sensor_unit

    if sensor_prefix is not None:
        sensor.prefix = sensor_prefix

    return sensor

def secs2hours(secs):
    return round(secs / 3600, 1)

def get_value(min, max):
    return random.randint(min,max)