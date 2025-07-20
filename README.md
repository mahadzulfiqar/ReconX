# Custom Reconnaissance Tool

This is a modular command-line reconnaissance tool built in Python as part of the Cybersecurity Summer Internship Project under the Reverse 4K Summer Training Camp. It includes both passive and active reconnaissance modules, along with a centralized main controller and a CLI interface.



 File: `main.py` – Main Controller

 Purpose:
This is the **central controller** of the entire reconnaissance tool. It manages module selection, controls execution order, and serves as the core driver of the application.

 Features:
- Integrates all passive and active modules
- Dynamically runs selected modules
- Logs and prints output from each phase
- Acts as the base entry point (will later integrate with `cli.py`)

 Description:
The script starts by importing all the individual modules (like `subdomain_enum`, `whois_lookup`, etc.). It then defines a central `run_all()` function, which executes each module sequentially. This file will be executed once the CLI interface is finalized and connected.



Note:  
Make sure all the module scripts (e.g., `subdomain_enum.py`, `dns_enum.py`, `whois_lookup.py`, etc.) are located in the **same GitHub repository directory** as `main.py`. This ensures proper importing and execution.
