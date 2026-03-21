# Port Scanner

Simple multi-threaded TCP port scanner built using Python.

This tool scans a target IP or domain and identifies open ports within a given range.

---

## Features

- Custom port range scanning
- Multi-threaded for faster execution
- Domain to IP resolution
- Saves results to a file

---

## Usage

```bash
python scanner.py -t <target> -p <start-end>
```

Example:

```bash
python scanner.py -t 127.0.0.1 -p 20-100
```

---

## Output

- Displays open ports in terminal
- Saves results in `scan_results.txt`

---

## Notes

- Scans are TCP-based
- Large port ranges may take time
- Use only on systems you own or have permission to test
