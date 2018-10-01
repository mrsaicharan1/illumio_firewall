from firewall import *

fw = Firewall('input.csv')

print(fw.accept_packet('inbound','udp','80','192.168.1.5'))
