# Simple TCP Port Scanner
# Built to understand basic socket programming and port scanning logic

import socket

print("\nSimple TCP Port Scanner")
print("-" * 25)

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

print(f"\nScanning target: {target_ip}")

choice = input("Do you want to scan (1) common ports or (2) custom range? Enter 1 or 2: ")

if choice == "1":
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 8080, 2220, 8282, 8000]

elif choice == "2":
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 0 or end_port > 65535:
            print("Port numbers must be between 0 and 65535.")
            exit()

        if start_port > end_port:
            print("Start port cannot be greater than end port.")
            exit()

        ports_to_scan = range(start_port, end_port + 1)

    except ValueError:
        print("Please enter valid numbers.")
        exit()

else:
    print("Invalid choice.")
    exit()

print(f"\nScanning ports from {min(ports_to_scan)} to {max(ports_to_scan)}")
print("Scanning...\n")

try:
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()

except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    exit()

print("\nScan Completed.")
