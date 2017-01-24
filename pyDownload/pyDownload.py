import os
import requests
import shutil
import hashlib
from threading import Thread
import urllib.parse

def download_file(url, start, end, part, file_name):
    local_filename = file_name+".part"+str(part)
    try:
    	start = os.path.getsize(local_filename)
    except OSError:
    	pass
    headers = {'Range': 'bytes={}-{}'.format(start, end)}
    r = requests.get(url, headers=headers, stream=True)
    with open(local_filename, 'ab') as f:
        shutil.copyfileobj(r.raw, f)
	return local_filename

def simple_download(url, file_name):
    try:
    	start = os.path.getsize(local_filename)
    except OSError:
    	start = 0
    headers = {'Range': 'bytes={}-'.format(start)}
    r = requests.get(url, headers=headers, stream=True)
    with open(local_filename, 'ab') as f:
        shutil.copyfileobj(r.raw, f)
	return local_filename

def get_file_name(url):
	# Checks if url has query variables.
	# If so, it tries to find the name of the file from it.
	file_name = None
	queries = urlparse.urlparse(url)
	params = dict(urlparse.parse_qsl(queries.query))
	if 'name' in params:
		file_name = params['name']
	if 'Name' in params:
		file_name = params['Name']
	if file_name == None:
		name = url.split('/')[-1]
		# in case url had / at the end
		if name == "":
			name = url.split('/')[-2]
	# assumes if file name > 50 it is not the proper name
	if len(name) > 50:
		name = "untitled"
	return name

def merge(file_name):
	tempfiles = []
	for i in range(1,6):
		tempfiles.append(file_name+".part"+str(i))
	with open(temp_file, "w") as fo:
	     for tempfile in tempfiles:
	          with open(tempfile,'r') as fi: fo.write(fi.read())

def call_threads(url, size, file_name):
	# change thread calls to lambda function later
	thread1 = Thread(target=download_file, (url, 0, (size/5), 1), file_name)
	thread2 = Thread(target=download_file, (url, (size/5) + 1, (size/5)*2, 2), file_name)
	thread3 = Thread(target=download_file, (url, ((size/5)*2) + 1, (size/5)*3, 3), file_name)
	thread4 = Thread(target=download_file, (url, ((size/5)*3) + 1, (size/5)*4, 4), file_name)
	thread5 = Thread(target=download_file, (url, ((size/5)*4) + 1, size, 5), file_name)
	t = [thread1, thread2, thread3, thread4, thread5]
	for x in t:
		x.start()
	for x in t:
		x.join()
	merge(file_name)
	print("File Successfully Downloaded")


def hash_check(hash_value, file_name):
	# Assumes you are using MD5 or SHA-256
	if hash_value == 0:
		print('Error: No hash value provided.')
		return -1

		result = None
	# Assumes if hashsum length is 32 it is md5
	if len(str(hash_value)) == 32:
		BLOCKSIZE = 65536
		hasher = hashlib.md5()
		with open(file_name, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
    	return hasher.hexdigest() == hash_value

	# Assumes if hashsum length is 64 it is sha256
	if len(str(hash_value)) == 32:
		BLOCKSIZE = 65536
		hasher = hashlib.shaa256()
		with open(file_name, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
    	return hasher.hexdigest() == hash_value

def main(url, hash_value):
	r = requests.head(url)
	if r.status_code != 200:
		print("Recieved Error Code: " + r.status_code)
		return
	file_name = get_file_name(url)
	try:
		size = r.headers['content-length']
		call_threads(url, size, file_name)
	except KeyError:
		simple_download(url, file_name)
	if hash != '':
		printhash_check(hash_value, file_name)

#url = 'https://dl.google.com/android/repository/tools_r25.2.3-windows.zip'
#url2 = 'https://www.fosshub.com/qBittorrent.html/qbittorrent_3.3.10_setup.exe'
#url3 = 'http://williampatino.com/2015/wp-content/uploads/2016/12/William_Patino_Photography_NewZealand_Norwest_Lakes-copy.jpg'
#x = download_file(url, 0, 153393413, 1)
#y = download_file(url, 1025, 153393413+1, 2)

