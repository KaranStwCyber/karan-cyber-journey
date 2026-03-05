import socket
import threading
from queue import Queue

print("Advanced TCP Port Scanner")
print("-------------------------")

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

threads = int(input("Enter number of threads (50-200 recommended): "))

print(f"\nScanning target: {target_ip}")
print(f"Port range: {start_port}-{end_port}")
print(f"Threads: {threads}\n")

queue = Queue()
open_ports = []


def banner_grab(sock):
    try:
        sock.send(b"HELLO\r\n")
        banner = sock.recv(1024)
        return banner.decode().strip()
    except:
        return None


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = socket.getservbyport(port, "tcp")
            banner = banner_grab(sock)

            print(f"Port {port} OPEN ({service})")

            if banner:
                print(f"Banner: {banner}")

            open_ports.append(port)

        sock.close()

    except:
        pass


def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()


for port in range(start_port, end_port + 1):
    queue.put(port)

thread_list = []

for _ in range(threads):
    t = threading.Thread(target=worker)
    t.start()
    thread_list.append(t)

queue.join()

print("\nScan Completed.")

if open_ports:
    print("\nOpen Ports Found:")
    for port in open_ports:
        print(port)
else:
    print("No open ports detected.")
