from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re

fd = open(r'C:\Users\J0000049\NewdayTest.txt','w')
old_stdout = sys.stdout
sys.stdout = fd
platform = 'cisco_ios'
username = 'admin-j0000049'
password = 'ti$$$1n414DULE'

ip_add_file = open(r'C:\Users\J0000049\DC Switchevi.txt','r')

for host in ip_add_file:
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('terminal length 0')
    output = device.send_command('enable')
    print('##############################################################\n')
    print('...................CISCO COMMAND SHOW UPTIME......................\n')
    output = device.send_command('sh ver | include uptime')
    print(output)
    print('...................CISCO COMMAND SHOW IP NAME SERVER...............\n')
    output = device.send_command('sh ip name-server')
    print('##############################################################\n')
    print(output)

fd.close()