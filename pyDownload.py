import os
import requests
import hashlib
import sys
import getpass
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def get_file_name(url):
	name = url.split('/')[-1]
	str(name)
	if len(name) > 50 or name == '':
		name = 'untitled'
	return name

def check_os(flag = 1):
	OS = sys.platform
	OS_uname = getpass.getuser()
	
	default_dest = None
	if flag == 1:
		if OS == 'linux' or 'linux2' or 'Linux':
			default_dest = '/home/{}/Downloads'.format(OS_uname)
		if OS == 'win32' or 'Windows':
			default_dest = 'C:\\Users\\{}\\Downloads'.format(OS_uname)
		if OS == 'darwin':
			default_dest = 'C/Users/{}/Downloads'.format(OS_uname)
		if default_dest == None:
			default_dest = os.getcwd()
	if flag == -1:
		default_dest = input(">>")
	print(default_dest)
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





def pyDownload(url, dest = check_os(), hash = None, timeout =10):
	
	chunk = 1000 * 1000
	filename = get_file_name(url)
	print (filename)
	temp_path = dest + '\\' + filename
	if os.path.exists(temp_path):
		return
	temp_path = temp_path + '.pyd'
	print(temp_path)
	if os.path.exists(temp_path):
		open_size = os.path.getsize(temp_path)
	else:
		open_size = 0

	file_size = -1
	try:
		file_size = int(urllib2.urlopen(url).info().get('Content-Length', -1))
		print('Something happening?')
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
			os.rename(temp_path,temp_path[:-5])

url = 'https://www.safaribooksonline.com/library/cover/9780470532874/240h/'
#url = 'http://blog.udacity.com/2014/05/how-to-bulk-rename-files-with-python.html'

download = pyDownload(url)