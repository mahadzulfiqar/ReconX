CustomReconTool – Cybersecurity Reconnaissance Tool

Overview:

CustomReconTool is a Python-based command-line reconnaissance tool designed for cybersecurity professionals and students. It supports both active and passive information gathering techniques, offering a modular structure to simplify analysis of target systems and domains. The tool is intended for educational and ethical penetration testing purposes only.

Project Structure

The repository is organized as follows:

customrecontool/
├── active/
│   ├── port\_scan.py
│   ├── banner\_grab.py
│   ├── tech\_detect.py
│   └── **init**.py
├── passive/
│   ├── dns\_enum.py
│   ├── subdomain\_enum.py
│   ├── whois\_lookup.py
│   └── **init**.py
├── main.py
├── cli.py
├── requirements.txt
└── README.md

Features:

Active Reconnaissance

- TCP port scanning using socket-based techniques
- Banner grabbing to identify running services
- Detection of technologies via HTTP headers

Passive Reconnaissance

- WHOIS record lookup for domain registration data
- DNS record enumeration
-Subdomain enumeration using online services

Usage:

To run all modules (active and passive) using the main controller script:
python main.py

To run modules selectively via the command-line interface:
python cli.py --target example.com --mode all

Available CLI modes:

-active
- passive
- all

Installation:

Step 1: Clone the repository
git clone [https://github.com/yourusername/customrecontool.git](https://github.com/yourusername/customrecontool.git)
cd customrecontool

Step 2: Install the required Python dependencies
pip install -r requirements.txt

Requirements:

 Python version 3.6 or higher
 Dependencies listed in the requirements.txt file

Author:

Minahil Nadeem

License:

This project is intended strictly for ethical and academic use. Unauthorized or malicious use of this tool is prohibited. The author does not assume any responsibility for misuse of this software.










