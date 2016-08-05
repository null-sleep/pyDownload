import os
import hashlib
import sys
#import getpass
import urllib.parse
from mimetypes import guess_extension
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

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

def set_default_paths(flag = 1):
	"""
	Used to set the deafult download location and the temporary file path
	based on the enviornment
	"""
	OS = sys.platform
	uname = os.getlogin() # Instead of longer pwd.getpwuid(os.getuid())[0]
	default_dest = None
	filename = get_file_name(url)

	if flag == 1:
		switch = {
		'linux2': '/home/{}/Downloads/'.format(uname)+filename,
		'win32': 'C:\\Users\\{}\\Downloads\\'.format(uname)+filename,
		'darwin': 'C/Users/{}/Downloads/'.format(uname)+filename
		}
		default_dest = switch[OS]

	if (flag == 2 or default_dest == None):
		default_dest = os.getcwd() + '/'

	if flag == 3:
		default_dest = input(">") + '/'
	return default_dest

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






def pyDownload(url, dest = 1, hash = None, timeout =10):
	
	chunk = 1000 * 1000
	extension = guess_extension(urllib2.urlopen(url).info().get('Content-Type', -1).split()[0].rstrip(";"))
	temp_path = set_default_paths(dest) + extension
	if os.path.exists(temp_path):
		return
	temp_path += '.pyd'

	if os.path.exists(temp_path):
		open_size = os.path.getsize(temp_path)
	else:
		open_size = 0

	file_size = -1
	try:
		file_size = int(urllib2.urlopen(url).info().get('Content-Length', -1))
		while open_size < file_size:
			current_byte = open_size + chunk \
				if open_size + chunk < file_size \
				else file_size
			req = urllib2.Request(url)
			req.headers['Range'] = 'bytes={}={}'.format(open_size,current_byte)
			data_chunk = urllib2.urlopen(req, timeout=timeout).read()
	
			with open(temp_path, 'ab') as x:
				x.write(data_chunk)
			open_size = current_byte + 1
	except ImportError as e:
		print('IO Error - {}'.format(e))
	finally:
		if file_size == os.path.getsize(temp_path):
			os.rename(temp_path,temp_path[:-4])

url = 'https://www.safaribooksonline.com/library/cover/9780470532874/240h/'
#url = 'http://blog.udacity.com/2014/05/how-to-bulk-rename-files-with-python.html'


download = pyDownload(url)

