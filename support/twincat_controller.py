import pyads
from ctypes import sizeof


ads_net_id = '192.168.2.123.1.1'
ip_address = '192.168.2.123'


plc = pyads.Connection(ads_net_id, pyads.PORT_TC3PLC1)
# plc = pyads.Connection(ads_net_id, pyads.PORT_TC3PLC1, ip_address)
print('Connecting to TwinCAT PLC..')
plc.open()
print('Current Status:', plc.is_open)
print('Current Status:', plc.read_state())

# print('Closing the Connections..')
# plc.close()
# print('Current Status:', plc.is_open)
