#-*- coding: utf-8 -*-
"""
Usage:
	pyd <url> [--hash <value>] [--auth <u> <p] [--version]

    Examples:
    pyd https://www.python.org/static/img/python-logo.png  : Download's the python logo from their homepage
    pyd https://www.example.com/... --auth username password : When authentication is required
    pyd https://www.example.com/... --auth username : Takes password after the command without being displayed on screen (like in terminals)

    Options:
    -h,--help
"""
from docopt import docopt
import getpass
import pyDownload

def start():
	arguments = docopt(__doc__)
	pyDownload.main(arguments[0], arguments[1])

if __name__ == '__main__':
        start()	
