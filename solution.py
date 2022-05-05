from scapy.all import *
import time

src = '128.173.54.143'

dst = '10.0.0.1'

send(IP(src=src,dst=dst)/TCP(dport=20, flags='S'), count=20)
time.sleep(5)

src = '128.173.54.101'

send(IP(src=src, dst=dst)/ICMP(type=4, chksum=100), count=35)
time.sleep(5)

port = 32700
for i in range(10):
    send(IP(src=src, dst=dst)/TCP(dport=port+i, flags='SFR')/'team17')