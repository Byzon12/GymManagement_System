import nmap
import sys
import datetime

def scan_target(target_ip):
        nm = nmap.PortScanner()
        print(f"[+] Starting Nmap scan on {target_ip}...")

    # Perform aggressive scan with version detection
        nm.scan(hosts=target_ip, arguments='-sS -sV -T4 -O')

        # Save scan output
        filename = f"nmap_scan_{target_ip.replace('.', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            for host in nm.all_hosts():
                f.write(f"\nHost: {host} ({nm[host].hostname()})\n")
                f.write(f"State: {nm[host].state()}\n")

                for proto in nm[host].all_protocols():
                    f.write(f"\nProtocol: {proto}\n")
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        f.write(f"Port: {port}\tState: {nm[host][proto][port]['state']}\tService: {nm[host][proto][port]['name']}\n")

        print(f"[+] Scan completed. Output saved to {filename}")

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python nmap_enum.py <target_ip>")
            sys.exit(1)

        target_ip = sys.argv[1]
        scan_target(target_ip)