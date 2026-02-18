# Simple TCP Port Scanner

Basic TCP port scanner built using Python sockets.

---

## Features

- Scan common ports
- Scan custom port range
- Timeout handling
- Graceful exit on Ctrl + C

---

## Run the Script

```bash
python port_scanner.py
```

---

## Example Usage

```bash
Enter target IP or domain: 127.0.0.1
Do you want to scan (1) common ports or (2) custom range? 2
Enter start port: 8000
Enter end port: 8010
```

### Output

```bash
Port 8000 is OPEN
```

---

## Notes

- Sequential scanning (not multi-threaded)
- Large ranges may take time
- Only scan systems you own or have permission
