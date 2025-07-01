# Automation Scripts for Ethical Hacking

This repository contains a collection of Python scripts tailored for automation in ethical hacking workflows. Each script targets a specific task like port scanning, hash cracking, banner grabbing, and basic keylogging.

## 📂 Scripts Included

| Script Name                | Description |
|---------------------------|-------------|
| `filedownloader.py`       | Downloads a ZIP payload from a given URL (e.g., SysInternals tools). |
| `grab_banner.py`          | Banner grabbing tool that scans for service banners on open ports. |
| `hashcracker.py`          | Cracks MD5 hashes using a user-provided wordlist. |
| `keylogger_script.py`     | Sends logged keystrokes to a remote server using sockets. |
| `keylogger_server.py`     | Receives logs from `keylogger_script.py` and prints them. |
| `networkscanner.py`       | ARP-based network scanner using Scapy. |
| `portscanner.py`          | Multi-port TCP scanner with ASCII UI. |
| `simplekeylogger.py`      | Minimal keylogger using `keyboard` module that plays back keystrokes. |
| `subdomain_enumerator.py` | Subdomain brute-forcer using a wordlist and HTTP requests. |

> ⚠️ These scripts are for educational and ethical hacking purposes **only**. Always ensure you have permission before scanning or logging any system.

## 📦 Requirements

Some scripts require third-party libraries:
- `scapy`
- `keyboard`
- `pyfiglet`
- `pynput`
- `requests`

Install with:

```bash
pip install -r requirements.txt
