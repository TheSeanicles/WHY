from scapy.all import *
import time

src1 = "128.173.54.143"

dst = "10.0.0.2"

send(IP(src=src1, dst=dst)/TCP(dport=20, flags="S"), count=20)
time.sleep(5)

src2 = "128.173.54.101"

send(IP(src=src2, dst=dst)/ICMP(type=4, chksum=100), count=35)
time.sleep(5)

port = 32700
for i in range(10):
    send(IP(src=src2, dst=dst)/TCP(sport=port+i, flags="SFR")/"team17")

