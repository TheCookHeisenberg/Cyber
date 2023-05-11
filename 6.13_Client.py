from scapy.all import *
from scapy.layers.inet import UDP, IP

MY_IP = "127.0.0.1"
DEST_IP = '172.16.12.67'



def encryptMsg(msg):
    for i in msg:
        PortASC = ord(str(i))

        my_packet = IP(dst=DEST_IP) / UDP(sport=24601, dport=PortASC)
        my_packet.show()
        send(my_packet)

    return


#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
while True:
    MSG_Client = input("Enter smth -->")
    print("You: ", MSG_Client)

    encryptMsg(MSG_Client)



