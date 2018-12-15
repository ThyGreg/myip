#!/usr/bin/env python3
import argparse
import json
import sys
from requests import get

# get ip from API
def getip():
    data = get("https://api.myip.com").text
    data = json.loads(data)
    return data

# commandlien argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="get public IP information")
    parser.add_argument("-i",
                        "--ip",
                        action="store_true",
                        help="print only IP")
    
    parser.add_argument("-c",
                        "--country",
                        action="store_true",
                        help="print only country")
    
    parser.add_argument("-C",
                        "--country-code",
                        action="store_true",
                        help="print only country code")
    
    parser.add_argument("-r",
                        "--raw",
                        action="store_false",
                        help="print raw output")
    return parser.parse_args()


args = parse_args()
output = getip()

# if nothing is specified, print all
if not args.ip and not args.country and not args.country_code:
    if args.raw:
        print("IP: ", end="")

    print(output["ip"])

    if args.raw:
        print("Country: ", end="")

    print(output["country"])

    if args.raw:
        print("CC: ", end="")

    print(output["cc"])
else:
    # print output
    if args.ip:
        if args.raw:
            print("IP: ", end="")
        print(output["ip"])
    if args.country:
        if args.raw:
            print("Country: ", end="")
        print(output["country"])
    if args.country_code:
        if args.raw:
            print("CC: ", end="")
        print(output["cc"])
