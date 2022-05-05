import scapy.all as scapy
import socket
import time
from numpy import random

sleep_time = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_host = s.getsockname()[0]
print(local_host)

# Packet 1

source_hostname = 'ruby.cirt.vt.edu'
src_host = socket.gethostbyname(source_hostname)
print(src_host)

for _ in range(20):
    packet1 = scapy.IP(src=src_host, dst=local_host)/scapy.TCP(sport=random.randint(65534), dport=20, flags='S')
    result1 = scapy.send(packet1, count=1, verbose=False)
    if not(result1 is None):
        if result1.haslayer('TCP'):
            print(result1['TCP'].payload)
    time.sleep(sleep_time)


# Packet 2

source_hostname = 'violet.cirt.vt.edu'
src_host = socket.gethostbyname(source_hostname)
print(src_host)

for _ in range(35):
    packet2 = scapy.IP(src=src_host, dst=local_host)/scapy.ICMP(type=4, chksum=100)
    result2 = scapy.send(packet2, count=1, verbose=False)
    if not(result2 is None):
        if packet2.haslayer('TCP'):
            print(packet2['TCP'].payload)
    time.sleep(sleep_time)


# Packet 3

source_hostname = 'violet.cirt.vt.edu'
src_host = socket.gethostbyname(source_hostname)
print(src_host)

src_p = 32700
msg = 'team17'
for i in range(10):
    packet3 = scapy.IP(src=src_host, dst=local_host)/scapy.TCP(sport=src_p+i, flags="SFR")/msg
    result3 = scapy.send(packet3, count=1, verbose=False)
    if not(result3 is None):
        if packet3.haslayer('TCP'):
            print(packet3['TCP'].payload)
    time.sleep(sleep_time)

