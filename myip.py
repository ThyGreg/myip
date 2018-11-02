import argparse
import json
from requests import get

parser = argparse.ArgumentParser(description='get public IP information')
parser.add_argument('-i', '--ip', action='store_true', help='print only IP')
parser.add_argument('-c', '--country', action='store_true', help='print only country')
parser.add_argument('-s', '--country-code', action='store_true', help='print only country code')
parser.add_argument('--raw',action='store_true', help='print raw output')

args = parser.parse_args()

data = get('https://api.myip.com').text
data = json.loads(data)

if args.raw:
    if not args.country and not args.country_code: print(data['ip'])
    if args.ip: exit(0)
    if not args.country_code: print(data['country'])
    if args.country: exit(0)
    print(data['cc'])
else:
    if not args.country and not args.country_code: print('IP:', data['ip'])
    if args.ip: exit(0)
    if not args.country_code: print('Country:', data['country'])
    if args.country: exit(0)
    print('CC:', data['cc'])