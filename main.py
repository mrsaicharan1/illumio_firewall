from firewall import *

fw = Firewall('input.csv')

print(fw.accept_packet('inbound','udp','80','0.0.0.0'))
