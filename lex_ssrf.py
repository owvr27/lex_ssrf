#!/usr/bin/env python3
import argparse
from scanner import scan
from reporter import report

BANNER = """
LΞX-SSRF
Advanced Server-Side Request Forgery Detector
Made by Omar Abdelsalam
"""

print(BANNER)

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("--oob", required=True, help="Your OOB domain")

args = parser.parse_args()

findings = scan(args.url, args.oob)
report(findings)
