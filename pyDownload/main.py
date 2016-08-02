#-*- coding: utf-8 -*-
"""
Usage:
	pyd <url> [--hash <value>] [--auth <u> <p] [--timout <t>] [--dest <d>]

    Examples:
    pyd https://www.python.org/static/img/python-logo.png  : Download's the python logo from their homepage
    pyd --dest cur : Download's to current directory instead of default downloads folder
    pyd --dest set : Let's you decide the download 
    pyd https://www.example.com/... --auth username password : When authentication is required
    pyd https://www.example.com/... --auth username : Takes password after the command without being displayed on screen (like in terminals)
    pyd https://www.example.com/... --hash


    Options:
    -h,--help
"""
from docopt import docopt
import getpass,pyDownload

def start():
	arguments = docopt(__doc__)
	print(arguments)
	print("Olle!")
	p = getpass.getpass()
	