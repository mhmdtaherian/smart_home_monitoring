
def get_sensor(sensor_uid, sensor_type, sensor_prefix, sensor_unit, values):    
    sensor = {
        "uid": sensor_uid,
        "type": sensor_type,
        "prefix": sensor_prefix,
        "unit": sensor_unit,
        "data": values
    }
    return sensor
        