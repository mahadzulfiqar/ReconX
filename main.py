from active.banner_grab import grab_banner
from active.port_scan import scan_ports
from active.tech_detect import detect_tech
from passive.dns_enum import get_dns_records
from passive.subdomain_enum import get_subdomains
from passive.whois_lookup import whois

def run_all(target):
    print("\n--- Active Recon ---")
    scan_ports(target, [21, 22, 80, 443, 8080])
    grab_banner(target, 80)
    detect_tech(f"http://{target}")

    print("\n--- Passive Recon ---")
    get_dns_records(target)
    get_subdomains(target)
    print(whois(target))
Added main.py controller
