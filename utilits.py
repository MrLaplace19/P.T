from scapy.all import TCP,IP,sr1,ICMP



def scan(ip, port):
    port = int(port)
    packet = IP(dst = ip) / TCP(dport = port, flags = "S")
    resp = sr1(packet, timeout = 1,verbose = 0)
    if (resp is None):
        status = "FILTERED"
    elif resp.haslayer(TCP):
        if resp[TCP].flags == 0x12:
            status = "OPEN"
            sr1(IP(dst = str(ip)) / TCP(dport = port, flags = "R"), timeout =1 , verbose = 0)
        elif resp[TCP].flags == 0x14:
            status = "CLOSED"
            sr1(IP(dst = str(ip)) / TCP(dport = port, flags = "R"), timeout =1 , verbose = 0)
    elif resp.haslayer(ICMP):
        status = "CLOSED/FILTERED"
    print(f"Port {port} on {ip} is {status}")
        

