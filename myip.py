#!/usr/bin/env python3
import argparse
import json
import sys
from requests import get


# get IP from API
def getip():
    data = get("https://api.myip.com").text
    data = json.loads(data)
    return data


# commandline argument parser
parser = argparse.ArgumentParser(description="get public IP information")
parser.add_argument("-i", "--ip", action="store_true",
                    help="print only IP")
parser.add_argument("-c", "--country",
                    action="store_true", help="print only country")
parser.add_argument("-C", "--country-code",
                    action="store_true", help="print only country code")
parser.add_argument("-r", "--raw", action="store_false",
                    help="print raw output")
args = parser.parse_args()
output = getip()

# some variables
ip = args.ip
country = args.country
cc = args.country_code
raw = args.raw

# if nothing is specified, print all
if not ip and not country and not cc:
    ip, country, cc = True, True, True

if ip:
    if raw:
        print("IP: ", end="")
    print(output["ip"])
if country:
    if raw:
        print("Country: ", end="")
    print(output["country"])
if cc:
    if raw:
        print("CC: ", end="")
    print(output["cc"])
