import scapy.all as scapy
import socket
import time

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
    packet1 = scapy.IP(src=src_host, dst=local_host)/scapy.TCP(sport=25385, dport=20, flags='S')
    result1 = scapy.send(packet1, count=1, verbose=False)
    if not(result1 is None):
        if result1.haslayer('TCP'):
            print(result1['TCP'].payload)
    time.sleep(sleep_time)
