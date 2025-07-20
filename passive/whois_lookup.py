import whois



domain = input("Enter domain for WHOIS lookup: ")

try:

    w = whois.whois(domain)

    print(w)

except Exception as e:

    print(f"Error during WHOIS lookup: {e}")
