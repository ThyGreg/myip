# myip
Get IP address with options

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
3. Run 'pip install pyinstaller'
4. Go into the script directory
5. Run 'pyinstaller -F myip.py'
6. The executable for your os will be saved in the 'dist' folder ;)
