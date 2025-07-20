import requests

def detect_tech(url):
    try:
        res = requests.get(url)
        headers = res.headers
        print(f"[+] HTTP Headers for {url}:")
        for key, value in headers.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[-] Error: {e}")

if _name_ == "_main_":
    url = input("Enter full URL (http://example.com): ")
    detect_tech(url)
