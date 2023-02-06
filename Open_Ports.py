import socket

def scan_ports(ip_address):
    open_ports = []
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((ip_address, port))
            open_ports.append(port)
            print(f"Port {port} is open")
            s.close()
        except:
            pass
    if not open_ports:
        print(f"No open ports found on {ip_address}")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip_address = get_ip()
scan_ports(ip_address)

