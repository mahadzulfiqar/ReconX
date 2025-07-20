import os

print("=== Custom Recon Tool ===")
target = input("Enter the target (domain or IP): ")

print("\n--- ACTIVE RECON ---")
os.system(f"python active/port_scan.py")
os.system(f"python active/banner_grab.py")
os.system(f"python active/tech_detect.py")

print("\n--- PASSIVE RECON ---")
os.system(f"python passive/whois_lookup.py")
os.system(f"python passive/dns_enum.py")
os.system(f"python passive/subdomain_enum.py")
