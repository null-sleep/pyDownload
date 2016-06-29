import requests
import hashlib
import sys
import os

def get_file_name(url):
	return url.split('/')[-1]

def check_os():
	OS = sys.platform
	OS_uname = pwd.getpwuid( os.getuid() )[ 0 ]
	
	if OS == 'linux' or 'linux2' or 'Linux':
		default_dest = '/home/{}/Downloads'.format(OS_uname)
	elif OS == 'win32' or 'Windows':
		default_dest = 'C:\Users\{}\Downloads'.format(OS_uname)
	elif OS == 'darwin':
		default_dest = 'C/Users/{}/Downloads'.format(OS_uname)
	else default_dest = -1
	return default_dest

def hash_check(default_dest, hash):
	m = hashlib.md5()

	with open(default_dest, 'rb') as f:
		while True:
			chunk = f.read(1000 * 1000)
			if not chunk:
				break
			m.update(chunk)
	return m.hexadigest() == hash

