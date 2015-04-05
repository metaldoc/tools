'''
Created on 2014-11-23

@author: metaldoc
'''

import socket
from datetime import datetime

addresses_list = []
tmp_array = []
time_now = str(datetime.now().strftime("%Y%m%d-%H%M%S"))

def is_ipv4_address_valid(prompt):
    while True:
        try:
            address = raw_input(prompt)
            socket.inet_aton(address)
        except socket.error:
            print "not ipv4 address"
            continue
        if address.count('.') != 3:
            print "not ipv4 address(dots missed)"
            continue
        else:
            break
    print "ipv4 address"  , address , "is valid"
    addresses_list.append(address)
    return True

is_ipv4_address_valid("Input first IPv4 address in range: ")
is_ipv4_address_valid("Input last IPv4 address in range: ")
is_ipv4_address_valid("Input netmask: ")
nw_IF = raw_input("Input network interface: ")
alias_adjusted = raw_input("Input existing alias amount for IF: ") or '0'

for ip_addr in addresses_list:
    tmp_array.append(ip_addr.rsplit(".", 1)[1])

IP_range = int(tmp_array[1]) - int(tmp_array[0]) + 1
IP_left = addresses_list[0].rsplit(".", 1)[0] 
IP_right = addresses_list[0].rsplit(".", 1)[1]
netmask = str(addresses_list[2])

out_file = open("IP_list_"+time_now+".txt", "w+")
for i in range(IP_range):
    print >> out_file, ('sudo ifconfig ' + nw_IF + ' inet ' + IP_left + '.' +
                        str((int(IP_right) + i)) + ' netmask ' +
                        netmask + ' alias')
for i in range(IP_range):
    print >> out_file, ('ifconfig_' + nw_IF + '_alias' + 
                        str(i + int(alias_adjusted)) + 
                        '="inet ' + IP_left + '.' 
                        + str((int(IP_right) + i))
                         + ' netmask ' + netmask + '"')

out_file.close()
print "IPs generated in "+"IP_list_"+time_now+".txt"+" file"