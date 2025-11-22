# nmap-masscan-automator
# 🕵️‍♂️ Nmap Recon Toolkit

### Advanced Network Scanning Suite (Nmap + Masscan + DNS Resolver)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg) ![Tool Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

A powerful and automated **Network Reconnaissance Toolkit** built for penetration testers, red teamers, bug bounty hunters, and security researchers. This CLI tool integrates **Nmap**, **Masscan**, and **nslookup** into one unified scanning engine featuring **21 automated recon modes**, fast domain resolving, and instant desktop scan notifications.

---

## ✨ Features

* ✔️ 21 fully automated reconnaissance scan profiles
* ✔️ Integrated **Masscan** for ultra-fast port scanning
* ✔️ Built-in **nslookup resolver** for domain → IP mapping
* ✔️ Scan completion **desktop notifications (plyer)**
* ✔️ Supports **TCP, UDP, SYN, aggressive & vulnerability scans**
* ✔️ Built-in brute-force NSE script hooks (SSH/FTP)
* ✔️ DNS brute forcing + SSL enumeration
* ✔️ Full-port scanning (1–65535)
* ✔️ Professional ASCII hacker banner included
* ✔️ Clean interactive CLI menu

---

## 📡 Scan Modes (1–21)

| ID | Scan Type             | Description            |
| -- | --------------------- | ---------------------- |
| 1  | TCP Connect           | Service + OS detect    |
| 2  | SYN Stealth           | Silent SYN scan        |
| 3  | UDP Services          | UDP enumeration        |
| 4  | Aggressive TCP        | Heavy recon            |
| 5  | Aggressive SYN        | Heavy stealth recon    |
| 6  | No Ping               | For ICMP-blocked hosts |
| 7  | Default Scripts       | NSE + versions         |
| 8  | Full Port Scan        | 1–65535                |
| 9  | Top 100 Ports         | Fast & quick           |
| 10 | Fast Scan             | Lightweight            |
| 11 | OS Detection          | OS only                |
| 12 | Version Detect        | Services               |
| 13 | Vuln Scripts          | Vulnerability scan     |
| 14 | HTTP Enum             | Web paths              |
| 15 | SMB Enum              | SMB users/shares       |
| 16 | DNS Brute             | Subdomain brute force  |
| 17 | FTP Brute             | FTP login attempts     |
| 18 | SSH Brute             | SSH login attempts     |
| 19 | SSL Info              | Certs & ciphers        |
| 20 | Full Recon            | Aggressive + scripts   |
| 21 | **Masscan Fast Scan** | Ultra-fast port sweep  |

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/nmap-recon-toolkit.git
cd nmap-recon-toolkit
```

### 2. Install Python dependencies

```bash
pip install plyer
```

> If you plan to use desktop notifications on Linux, ensure you have a notification daemon running (most desktop environments include one). On headless servers, desktop notifications will not appear.

### 3. Install Nmap & Masscan (Linux/Kali/Ubuntu)

```bash
sudo apt update && sudo apt install nmap masscan -y
```

---

## ▶️ Usage

Run the tool:

```bash
python3 recon_toolkit.py
```

You will see an interactive menu:

```
============= Available Recon Scans (1–21) =============
Enter your scan choice:
```

Enter a scan ID → enter target IP/domain → optional ports → done.

The scanner will:

* Resolve domains automatically
* Run the selected scan
* Show results in terminal
* Send a desktop notification

---

## 🔧 Configuration & Tips

* **Run Masscan with sudo**: Masscan usually requires root privileges for raw packet sending.
* **Adjust Masscan rate**: Edit the `--rate` parameter in the Masscan invocation to avoid network congestion.
* **Use responsibly**: Aggressive scans can trigger intrusion detection/prevention systems.

---

## 📸 Screenshots (Optional)


## ⚠️ Legal Disclaimer

This tool is built **strictly for:**

* Ethical hacking
* Security testing (with permission)
* Research
* Education

Do **NOT** scan systems you do not own or have explicit permission to test. The author is **not responsible** for any misuse or illegal activity.

---

## 👨‍💻 Author

**Syed Yasir Hassan**
Red Team Automation • Ethical Hacking • Python Security Tools
GitHub:  (https://github.com/syedyasirh299-hash)

---

## 📦 License

MIT License — see `LICENSE` for details.

---

If you want a matching **project banner**, **logo**, or a ready-made **LICENSE** file, tell me which license you prefer and I will add it.
