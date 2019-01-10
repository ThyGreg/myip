# myip
Get public IP address with options

# usage
usage: myip.py [-h] [-i] [-c] [-s] [--raw]

get public IP information

optional arguments:
  -h, --help          show this help message and exit
  -i, --ip            print only IP
  -c, --country       print only country
  -s, --country-code  print only country code
  --raw               print raw output

# compile for your system
1. Install python3
2. Install python3-pip
3. Run 'pip3 install pyinstaller' (if 'pip3' was not found, try 'pip' instead)
4. Go into the script directory
5. Run 'pyinstaller -F myip.py'
6. The executable for your OS will be saved in the 'dist' folder ;)

# credit
API: https://www.myip.com/api-docs/
