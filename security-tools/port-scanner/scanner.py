# Simple Multi-threaded TCP Port Scanner

import socket
import argparse
import threading

# Argument parsing
parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
parser.add_argument("-p", "--ports", required=True, help="Port range (e.g. 20-100)")

args = parser.parse_args()

target = args.target
port_range = args.ports

# Resolve domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

# Parse port range
try:
    start_port, end_port = map(int, port_range.split("-"))
except:
    print("Invalid port range format. Use like 20-100")
    exit()

print(f"\nScanning target: {target_ip}")
print(f"Port range: {start_port}-{end_port}\n")

open_ports = []
lock = threading.Lock()

# Scan function
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        with lock:
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    sock.close()

# Threading
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Save results
with open("scan_results.txt", "w") as f:
    for port in open_ports:
        f.write(f"Port {port} is OPEN\n")

print("\nScan Completed.")
print("Results saved to scan_results.txt")
