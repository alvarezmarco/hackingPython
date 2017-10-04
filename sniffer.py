
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

paquetes = sniff (iface="wlan0", count=20)
print paquetes

paquetesicmp = sniff (iface="wlan0", filter = "icmp", count=5,prn=lambda x: x.show())

paquetestcp = sniff (iface="wlan0", filter = "tcp", count=2,prn=lambda x: x.show())



