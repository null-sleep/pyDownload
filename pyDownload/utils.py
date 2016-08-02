import os
import requests
import hashlib
import sys
import urllib.parse
from mimetypes import guess_extension

def set_default_paths(flag = 1):
	"""
	Used to set the deafult download location and the temporary file path
	based on the enviornment
	"""
	OS = sys.platform()
	uname = os.getlogin() # Instead of longer pwd.getpwuid(os.getuid())[0]
	default_dest = None
	filename = get_file_name(url)

	if flag == 1:
		switch = {
		'linux2': '/home/{}/Downloads/'.format(uname+'/'+filename),
		'win32': 'C:\\Users\\{}\\Downloads\\'.format(uname+'\\'+filename),
		'darwin': 'C/Users/{}/Downloads/'.format(uname+'/'+filename)
		}
		default_dest = switch[OS]

	if (flag == 2 or default_dest == []):
		default_dest = os.getcwd() + '/'

	if flag == 3:
		default_dest = input(">") + '/'
	return default_dest


def get_file_name(url, flag = 1):
	# Checks if url has query variables.
	# If so, it tries to find the name of the file from it.
	file_name = None
	if flag == 1:
		parsed = urllib.parse.urlparse(url)
		params = urllib.parse.parse_qsl(parsed.query)
		for x,y in params:
			if x == 'name' or x =='Name' :
				file_name = y

		if file_name == None:
			name = url.split('/')[-1]
			if name == "":
				name = url.split('/')[-2]

		if len(name) > 50:
			name = "untitled"
	# flag = 1 for setting the name automatically, flag = -1 for user to set the name
	elif flag == -1:
		name = input('File Name:\n>>>')
	return name


def authentication():
	pass

def hash_check(file_dest, hash_value = None):
	# Assumes you are using MD5 or SHA-256
	if hash_value == None:
		print('Error: No hash value provided.')
		return -1

	result = None
	if len(hash_value) == 32:
		m = hashlib.md5()

		with open(default_dest, 'rb') as f:
			while True:
				chunk = f.read(1024 * 1024)
				if not chunk:
					break
				m.update(chunk)
		result = m.hexadigest() == hash_value

	if len(hash_value) == 64:
		m = hashlib.sha256()

		with open(default_dest, 'rb') as f:
			while True:
				chunk = f.read(1024 * 1024)
				if not chunk:
					break
				m.update(chunk)
		result = (m.hexadigest() == hash_value)


def pyDownload(url, dest=1, hash = False, auth = False, timeout):

	chunk = 1024*1024
	if not auth:
		r = requests.get(url)
	else:
		user_name = input("User Name: ")
		password = input("Password: ")
	extension = guess_extension(r.headers['content-type'].split()[0].rstrip(";"))
	temp_path = default_dest(dest) + extension
	if os.path.exists(temp_path):
		return

	temp_path += ".pyd"

	if os.path.exists(temp_path):
		open_size = os.path.getsize(temp_path)
	else:
		open_size = 0

	file 

