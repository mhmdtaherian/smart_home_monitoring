import _const as const
from _util import get_sensor
import psutil

def get_networks():

    sensors = []

    network_total = psutil.net_io_counters()

    bandwidth_value = {
        const.SENSOR_NAME_NETWORKS_RECV: network_total.bytes_recv,
        const.SENSOR_NAME_NETWORKS_SENT: network_total.bytes_sent
    }

    packet_value = {
        const.SENSOR_NAME_NETWORKS_RECV: network_total.packets_recv,
        const.SENSOR_NAME_NETWORKS_SENT: network_total.packets_sent
    }

    sensors.append(get_sensor(const.SENSOR_NAME_NETWORKS.format(const.SENSOR_NAME_NETWORKS_BANDWIDTH), bandwidth_value))
    sensors.append(get_sensor(const.SENSOR_NAME_NETWORKS.format(const.SENSOR_NAME_NETWORKS_PACKET), packet_value))
    
    return sensors

print(get_networks())