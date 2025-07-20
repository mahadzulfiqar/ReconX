# dns_enum.py

import dns.resolver

def get_dns_records(domain):
    record_types = ['A', 'MX', 'TXT', 'NS']

    print(f"\n[DNS Enumeration for: {domain}]")
    print("----------------------------------")

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"\n{record_type} Records:")
            for rdata in answers:
                print(f" - {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"\n{record_type} Records: No Answer")
        except dns.resolver.NXDOMAIN:
            print(f"\n{record_type} Records: Domain does not exist")
        except Exception as e:
            print(f"\n{record_type} Records: Error - {e}")

# Test the function directly
if _name_ == "_main_":
    domain = input("Enter domain for DNS enumeration: ")
    get_dns_records(domain)
