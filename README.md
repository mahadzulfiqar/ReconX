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


                               🚀 Usage

 Install Requirements
```bash
pip install -r requirements.txt

                               Run Modules
   1.Passive Recon

python3 scripts/passive/whois_lookup.py
python3 scripts/passive/dns_enum.py
python3 scripts/passive/subdomain_enum.py

  2.Active Recon

python3 scripts/active/port_scan.py
python3 scripts/active/banner_grab.py
python3 scripts/active/tech_detect.py

  3. Run via Main CLI

python3 recon.py --mode passive
python3 recon.py --mode active

                                       📦 Dependencies
   ...Python 3.6+

1.requests
2.socket
3.argparse
4.whois
5.dnspython
6.json, re, sys

...Install all using:
 
pip install -r requirements.txt

                                ✍️ Contributors

Tooba Zainab = active recon
Mahad Zulfiqar =  passive recon
Minahil Nadeem =  reporting CLI main

                               ⚠️ Disclaimer

This tool is for educational and authorized security testing purposes only.
Do not use it against targets without explicit permission.

