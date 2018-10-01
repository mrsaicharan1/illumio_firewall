import csv

class Firewall:
    def __init__(self,path):
        self.csv_path = path

    def accept_packet(self,direction,protocol,port,ip_address):
        line_count = 0 # to omit the column names line
        with open(self.csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",") # loading in the csv file
            header = next(csv_reader)
            for row in csv_reader: # looping through the csv file
                if direction == row[0] and protocol == row[1] and self.valid_port(port,row[2]) and self.valid_ip(ip_address,row[3]):
                    return True
                else:
                    line_count+=1
        return False

    def valid_ip(self,ip_packet,ip_input):
        if '-' in ip_input: # if the IP address is given as a range(csv)
            ip_split = ip_input.split('-') # store min_ip,max_ip in a list

            min_ip = ip_split[0]
            max_ip = ip_split[1]
            # print('Min IP: '+min_ip)
            # print('Type'+str(type(min_ip)))
            # print('Max_IP: '+max_ip)
            # print('Type'+str(type(max_ip)))

            # store individual octets of packet and ranges in a list
            min_ip_octets = min_ip.split('.')
            max_ip_octets = max_ip.split('.')
            ip_packet_octets = ip_packet.split('.')

            octet_valid_min = 0 #initialize number of valid octets greater than min. ip address octets
            octet_valid_max = 0 #initialize number of valid octets lesser than max.ip address octets

            # loop through packet and min.ip for valid octets
            for ip_packet_octet,min_ip_octet in zip(ip_packet_octets,min_ip_octets):
                if int(ip_packet_octet) >= int(min_ip_octet):
                        octet_valid_min+=1

            # loop through packet and max.ip for valid octets
            for ip_packet_octet,max_ip_octet in zip(ip_packet_octets,max_ip_octets):
                if int(ip_packet_octet) <= int(max_ip_octet):
                    octet_valid_max+=1

            # check if IP address is valid by checking octets
            if octet_valid_min ==4 and octet_valid_max ==4:
                return True
            else:
                return False

        else: #if the IP address is not given as a range
            if ip_packet == ip_input:
                return True
            else:
                return False






    def valid_port(self,port_packet,port_input):
        if '-' in port_input: #if port is given as a range(csv)

            # store extremes of port ranges in a list
            port_split = port_input.split('-')

            port_min=port_split[0]
            port_max=port_split[1]


            if int(port_packet)<=int(port_max) and int(port_packet)>=int(port_min): # check if packet port lies in the range
                return True
            else:
                return False

        else: # if port is given as a single value(csv)
            if int(port_packet) == int(port_input):
                return True
            else:
                return False
