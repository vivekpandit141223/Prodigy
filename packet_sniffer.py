import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        proto = packet[scapy.IP].proto

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {proto}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload}")

def main():
    print("Packet Sniffer started...")

    # sniff packets with a packet callback function
    scapy.sniff(prn=packet_callback, store=False, iface="eth0") 
main()
