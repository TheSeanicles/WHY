from scapy.all import *
import time

src = "128.173.54.143"

dst = "10.0.0.1"

send(IP(src=src, dst=dst)/TCP(dport=20, flags="S"), count=20)
time.sleep(5)

src = "128.173.54.101"

send(IP(src=src, dst=dst)/ICMP(type=4, chksum=100), count=35)
time.sleep(5)

send(IP(src=src, dst=dst)/TCP(dport=32700, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32701, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32702, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32703, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32704, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32705, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32706, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32707, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32708, flags="SFR")/"team17")
send(IP(src=src, dst=dst)/TCP(dport=32709, flags="SFR")/"team17")
