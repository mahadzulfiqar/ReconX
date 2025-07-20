import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        print(f"[+] Banner from {ip}:{port} - {banner.decode().strip()}")
    except:
        print(f"[-] Failed to grab banner from {ip}:{port}")
    finally:
        s.close()

if _name_ == "_main_":
    ip = input("Enter IP: ")
    port = int(input("Enter Port: "))
    grab_banner(ip, port)
