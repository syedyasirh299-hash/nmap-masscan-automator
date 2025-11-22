import subprocess as sp
from plyer import notification
import time
import re

# ===== ANSI COLORS =====
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"

# ===== ASCII BANNER =====
BANNER = f"""
{GREEN}{BOLD}
 _   _ _   _    _    _____ 
| \\ | | \\ | |  / \\  | ____|
|  \\| |  \\| | / _ \\ |  _|  
| |\\  | |\\  |/ ___ \\| |___ 
|_| \\_|_| \\_/_/   \\_\\_____|
       N M A P   T O O L K I T
{RESET}{CYAN}  made-by-syedyasirhassan nslookup + Masscan Added {RESET}
"""

# ===== 20 RECON SCANS =====
SCANS = [
    ("1", "TCP Connect Scan", "-sT -sV -O", "Full connect scan + version + OS"),
    ("2", "SYN Stealth Scan", "-sS -sV -O", "Stealth scan + version + OS"),
    ("3", "UDP Service Scan", "-sU -sV", "UDP service enumeration"),
    ("4", "Aggressive TCP Scan", "-sT -A", "TCP aggressive recon"),
    ("5", "Aggressive SYN Scan", "-sS -A", "SYN aggressive recon"),
    ("6", "No Ping Version Scan", "-sV -Pn", "Scan hosts blocking ICMP"),
    ("7", "Default Script Scan", "-sC -sV", "Default NSE scripts + version"),
    ("8", "Full Port Scan", "-p- -sV", "Scan all 65535 ports"),
    ("9", "Top 100 Ports Scan", "--top-ports 100 -sV", "Common ports quick recon"),
    ("10", "Fast Scan", "-F -sV", "Fast scan limited ports"),
    ("11", "OS Fingerprint Only", "-O", "OS fingerprinting only"),
    ("12", "Version Only", "-sV", "Service version discovery"),
    ("13", "Script Vulnerability Scan", "--script vuln", "Basic vuln scripts"),
    ("14", "HTTP Enum", "--script http-enum", "Enumerate HTTP endpoints"),
    ("15", "SMB Enum", "--script smb-enum-shares,smb-enum-users", "SMB discovery"),
    ("16", "DNS Brute Force", "--script dns-brute", "DNS subdomain brute force"),
    ("17", "FTP Brute Force", "--script ftp-brute", "FTP login brute forcing"),
    ("18", "SSH Brute Force", "--script ssh-brute", "SSH login brute forcing"),
    ("19", "SSL Info", "--script ssl-cert,ssl-enum-ciphers", "SSL/TLS certificate + cipher info"),
    ("20", "Comprehensive Recon", "-A -sS -sC -sV", "Full recon (heavy)"),
    ("21", "FAST Masscan Open Ports", "masscan", "Ultra-fast open port scan")
]


def print_menu():
    print(BANNER)
    print(f"{BLUE}{BOLD}============= Available Recon Scans (1–21) ============={RESET}\n")

    for scan_id, name, cmd, desc in SCANS:
        print(f"{YELLOW}{scan_id:>2} - {name:<27}{RESET}: {CYAN}{desc}{RESET}")

    print(f"\n{BLUE}{BOLD}======================================================={RESET}")


# ------------------------------------------------------------
# nslookup resolver
# ------------------------------------------------------------
def resolve_domain(target):
    """Resolve domain to IP using nslookup."""
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", target):
        return target

    print(f"{CYAN}[*] Resolving domain with nslookup...{RESET}")

    try:
        result = sp.check_output(["nslookup", target]).decode()

        # Find ALL Address: lines that contain IPv4
        addresses = re.findall(r"Address:\s*([\d\.]+)", result)

        # The last one is the resolved domain IP
        if addresses:
            ip = addresses[-1]
            print(f"{GREEN}[+] Domain resolved: {target} → {ip}{RESET}")
            return ip

        print(f"{RED}[-] Could not resolve domain!{RESET}")
        return None

    except Exception:
        print(f"{RED}[-] nslookup failed!{RESET}")
        return None


# ------------------------------------------------------------
# Notifications
# ------------------------------------------------------------
def send_notification(title, message):
    notification.notify(title=title, message=message, timeout=5)
    time.sleep(1)


# ------------------------------------------------------------
# Run Nmap or Masscan
# ------------------------------------------------------------
def run_nmap_scan(choice: str):
    matching = next((s for s in SCANS if s[0] == choice), None)
    if matching is None:
        print(f"{RED}[-] Invalid choice (1–21){RESET}")
        return

    scan_id, name, cmd, _ = matching

    # Get user input
    target = input("Enter target IP or DOMAIN: ").strip()
    ip = resolve_domain(target)
    if not ip:
        return

    port = input("Enter port (leave blank for default 1–1000): ").strip()

    print(f"\n{GREEN}[+] Running: {name}{RESET}")

    # MASSCAN (Option 21)
    if scan_id == "21":
        cmd_list = ["sudo", "masscan", ip, "--rate", "5000"]

        if port:
            cmd_list += ["-p", port]
        else:
            cmd_list += ["-p1-1000"]

        sp.run(cmd_list)

        send_notification("Masscan Completed", f"Fast scan finished for {ip}")
        return

    # Normal Nmap scans
    cmd_list = ["nmap"]

    # Default port handling
    cmd_list += ["-p", port] if port else ["-p", "1-1000"]

    cmd_list += cmd.split()
    cmd_list.append(ip)

    sp.run(cmd_list)

    send_notification("Nmap Scan Completed", f"Scan '{name}' finished!")


# ------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("\nEnter your scan choice (1–21) or 'q' to quit: ").strip()
        if choice.lower() == "q":
            print("Exiting Nmap Toolkit...")
            break
        run_nmap_scan(choice)
