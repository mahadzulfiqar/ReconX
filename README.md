Custom Recon Tool – Modular Reconnaissance Tool

Custom Recon Tool is a lightweight, modular reconnaissance framework designed for penetration testers. It includes both passive and active information gathering modules, integrated via a central CLI controller.



                       🧠 Features

- 🔍 Passive Recon
  - WHOIS Lookup
  - DNS Record Enumeration (A, MX, NS, TXT)
  - Subdomain Enumeration using public APIs (crt.sh, AlienVault, etc.)

- 🔧 Active Recon
  - Port Scanning (TCP sockets)
  - Banner Grabbing
  - Technology Detection using HTTP headers

- 📄 Reporting
  - Structured output for analysis
  - Easily extendable and script-friendly

                        📁 Project Structure

ReconX/
├── recon.py # Main CLI controller
├── scripts/
│ ├── passive/
│ │ ├── whois_lookup.py
│ │ ├── dns_enum.py
│ │ ├── subdomain_enum.py
│ ├── active/
│ │ ├── port_scan.py
│ │ ├── banner_grab.py
│ │ ├── tech_detect.py
├── reports/ # Stores generated reports
├── utils/ # Shared helper modules (optional)
├── requirements.txt
└── README.md

yaml
Copy
Edit
                               🚀 Usage

### Install Requirements
```bash
pip install -r requirements.txt
Run Modules
Passive Recon
bash
Copy
Edit
python3 scripts/passive/whois_lookup.py
python3 scripts/passive/dns_enum.py
python3 scripts/passive/subdomain_enum.py
Active Recon
bash
Copy
Edit
python3 scripts/active/port_scan.py
python3 scripts/active/banner_grab.py
python3 scripts/active/tech_detect.py
Run via Main CLI
bash
Copy
Edit
python3 recon.py --mode passive
python3 recon.py --mode active

                                       📦 Dependencies
Python 3.6+

requests

socket

argparse

whois

dnspython

json, re, sys

Install all using:

bash
Copy
Edit
pip install -r requirements.txt

                                ✍️ Contributors

Tooba Zainab = active recon
Mahad Zulfiqar =  passive recon
Minahil Nadeem =  reporting CLI main

                               ⚠️ Disclaimer

This tool is for educational and authorized security testing purposes only.
Do not use it against targets without explicit permission.

