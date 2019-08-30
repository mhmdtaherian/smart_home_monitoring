import json 
import threading
import http.client
from generaldevice import generate_device_list

# Configuration section
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = '/Gateway'
SENT_INTERVAL = 10 # Sent data interval in second

def main():
    threading.Timer(SENT_INTERVAL, main).start()
    devices = generate_device_list()
    
    connection = http.client.HTTPSConnection(UBEAC_URL)
    connection.request('POST', GATEWAY_URL, json.dumps(devices))
    response = connection.getresponse()
    print(response.read().decode())
   

if __name__ == '__main__':
    main()