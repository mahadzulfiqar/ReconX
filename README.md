# ReconX — Modular Reconnaissance Toolkit

[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![Build](https://img.shields.io/github/actions/workflow/status/<your-username>/ReconX/python-ci.yml?branch=main)]()

ReconX is a modular, educational reconnaissance toolkit written in Python for authorized security testing and learning. It bundles passive and active reconnaissance utilities (WHOIS, DNS, subdomain enumeration, port scanning, banner grabbing) and exports structured reports for further analysis.

> ⚠️ **IMPORTANT:** This tool is for **education and authorized security testing only**. Do not use ReconX against systems you do not have explicit permission to test.

---

## Features
- WHOIS lookup
- DNS record enumeration (A, AAAA, NS, MX, SOA, TXT)
- Subdomain enumeration (wordlist-based)
- Threaded TCP port scanner with banner grabbing (planned / v2)
- Exports results in JSON and plain-text
- CLI with `argparse` and simple output options
- Modular layout for easy extension

---

## Quick demo (example)
```bash
$ python main.py --target example.com --mode passive --output reports/example_report.json
