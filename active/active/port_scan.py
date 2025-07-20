import socket

def scan_ports(host, ports):
    print(f"Scanning ports on {host}")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((host, port))
            print(f"[+] Port {port} is OPEN")
            s.close()
        except:
            pass

if _name_ == "_main_":
    target = input("Enter target host (e.g., example.com): ")
    ports = [21, 22, 80, 443, 8080]
    scan_ports(target, ports)
