# Smart Home Monitoring
This simulator will send data related to a smart home. This home contains 1 living room, 3 bedrooms, invironmental information from back yard, smart device including fridge, kettle, washer, dryer, dish washer, coffee maker and a local computer.

Data will be sent by default every 10 seconds but you can change the interval.

## Instruction:
* In command prompt run: pip install psutil
* Create a gateway (Type: uBeac Multiple Devices)
* Update or get the gateway's URL, your device friendly name, and sent data interval in main.py.
* Run main.py.
* Go to the gateway info page and you should see the live requests. You can click on info icon for each request to see the sensors data.
* Go to the devices page. You should see a device with name: your device friendly name
* Update the details for the sensors (units,...)
* Go to dashboard and drag & drop an indicator. In the setting for the indicator, select the sensor you want to show data.
