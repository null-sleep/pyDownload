#-*- coding: utf-8 -*-
"""
Usage:
	pyd <url> [--hash=<h>] [--auth <u> <p>] [--timout <t>] [--dest <d>]

    Examples:

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
	