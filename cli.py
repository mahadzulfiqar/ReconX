import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Custom Recon Tool CLI")
    subparsers = parser.add_subparsers(dest='mode')

    # Active Tools
    active = subparsers.add_parser('active', help='Run active recon tools')
    active.add_argument('--tool', choices=['portscan', 'banner', 'tech'], required=True)

    # Passive Tools
    passive = subparsers.add_parser('passive', help='Run passive recon tools')
    passive.add_argument('--tool', choices=['whois', 'dns', 'subdomain'], required=True)

    args = parser.parse_args()

    if args.mode == 'active':
        if args.tool == 'portscan':
            os.system("python active/port_scan.py")
        elif args.tool == 'banner':
            os.system("python active/banner_grab.py")
        elif args.tool == 'tech':
            os.system("python active/tech_detect.py")

    elif args.mode == 'passive':
        if args.tool == 'whois':
            os.system("python passive/whois_lookup.py")
        elif args.tool == 'dns':
            os.system("python passive/dns_enum.py")
        elif args.tool == 'subdomain':
            os.system("python passive/subdomain_enum.py")

if __name__ == "__main__":
    main()
