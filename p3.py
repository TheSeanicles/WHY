import scapy.all as scapy
import socket
import time

sleep_time = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_host = s.getsockname()[0]
print(local_host)

# Packet 3

source_hostname = 'violet.cirt.vt.edu'
src_host = socket.gethostbyname(source_hostname)
print(src_host)

src_p = 32700
msg = 'team17'
for i in range(10):
    packet3 = scapy.IP(src=src_host, dst=local_host)/scapy.TCP(sport=src_p+i, flags="S")/msg
    result3 = scapy.send(packet3, count=1, verbose=False)
    if not(result3 is None):
        if packet3.haslayer('TCP'):
            print(packet3['TCP'].payload)
    time.sleep(sleep_time)

