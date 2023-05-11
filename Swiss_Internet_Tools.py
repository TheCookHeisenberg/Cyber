from scapy.all import *
from scapy.layers.inet import IP, ICMP

def ping(dst_ip):
    request_packet = IP(dst = dst_ip)/ICMP(type = "echo-request")/"Nate Higgers"
   
    response_packet = sr1(request_packet)
    ernik = response_packet[IP].sent_time
    nickur =  response_packet[IP].time
    print (ernik, nickur)
    #print("Reply from ",response_packet[IP].src,": bytes = ",response_packet[IP].len, "time = ",)
    
    
    


#Main: 
toolChoice = input("Pick your tool: [1] ping | [2]  smth idk")

dst_ip = input("Enter an IP address: ")

#Ping method:
if toolChoice == "1":
    ping(dst_ip)




















