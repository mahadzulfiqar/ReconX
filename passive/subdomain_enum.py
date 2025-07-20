# subdomain_enum.py

import requests
import json

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    print(f"\n[Subdomain Enumeration using crt.sh for: {domain}]")
    print("----------------------------------------------------")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("[-] Failed to fetch data from crt.sh")
            return

        data = response.json()
        subdomains = set()

        for entry in data:
            name_value = entry.get('name_value')
            if name_value:
                names = name_value.split('\n')
                for name in names:
                    if domain in name:
                        subdomains.add(name.strip())

        if subdomains:
            print(f"\n[+] Found {len(subdomains)} unique subdomains:")
            for sub in sorted(subdomains):
                print(f" - {sub}")
        else:
            print("[-] No subdomains found.")

    except Exception as e:
        print(f"Error during subdomain enumeration: {e}")

# Test directly
if _name_ == "_main_":
    domain = input("Enter domain for subdomain enumeration: ")
    get_subdomains(domain)
