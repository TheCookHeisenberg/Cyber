from scapy.all import *
from scapy.layers.inet import UDP, IP

MY_IP = "127.0.0.1"
DEST_IP = '172.16.13.198'
#---------------------------------------------------------------------------------------------------
def isPacketEmpty():
    return Raw in packet
#---------------------------------------------------------------------------------------------------
def decryptMsg():
    packets = sniff(count=1, lfilter = isPacketEmpty())

    [print(str(packet[UDP].dport), end="") for packet in packets]
#---------------------------------------------------------------------------------------------------

def Main():
    decryptMsg()

if __name__ == "__Main__":
    Main()