import socket
from datetime import datetime
from pathlib import Path
print("=== NetworkChecker ===")
print("welcome to my first cyberscurity project !")
print("status : Ready")


print("----------------------------------------------")


domain = "simayedanesh.ir"
ip = "Not resolved"
dns_status = "FAILED"
try:
    ip = socket.gethostbyname(domain)
    dns_status = "SUCCESS"
    print("DNS lookup successful")
    print("domain:",domain)
    print("IPv4:",ip)
except socket.gaierror as error:
    print("DNS lookup Failed")
    print("reason:",error)
print("-----------------------------------------------")


host = input("Enter host:").strip()
port_Text = input("Enter port:").strip()
tcp_status = "FAILED"
try:
    Port = int(port_Text)
    if not host:
        raise ValueError("Host cannot be empty!")
    if not 1<=Port<=65535:
        raise ValueError("Port must be between 1 and 65535")
    with socket.create_connection((host,Port),timeout = 5):
        tcp_status = "SUCCESS"
        print("TCP Connection Successful !")
        print("host:",host)
        print("port:",Port)
except (ValueError,OSError) as error:
    print("TCP connection Failed")
    print("reason:",error)
print("--------------------------------------------------")


report = (
    "=== NetworkChecker Report ===\n"
    f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"Domain: {domain}\n"
    f"IPv4: {ip}\n"
    f"DNS status: {dns_status}\n"
    f"host: {host}\n"
    f"port: {port_Text}\n"
    f"TCP status: {tcp_status}\n"
)
report_file = Path(__file__).with_name("network_report.txt")
try:
    report_file.write_text(report, encoding= "utf-8")
    print("Report save successfully!")
    print("File:",report_file.name)
except OSError as error:
    print("Report could not be saved!")
    print("reason:", error)