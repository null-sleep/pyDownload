import urllib
import sys
import os

def url_fix(url):
	pass:


class urlOpener(urllib.FancyURLopener):
    """ Subclass to ignore error 206 (partial file)"""
    def http_error_206(self, url, fp, errcode, errmsg, headers, data=None):
        pass    # On encounter with this error, nothing happens


def download(url, dest = check_os(), file_name = , verbose = 0):  # file_name
	loop = 1
	exitSize = 0
	URLclass = urlOpener()
	dest = dest + '/' + file_name   # updates destination link by adding filename

	# Checks if file exist. If it does it gets the header position, else sets up a new file
	if os.path.exists(dest):
		outputFile = open(file_name,"ab")
		currentSize = os.path.getsize(dest)
		URLclass.addheader("Range", "bytes={}-".format(currentSize))
	else:
		outputFile = open(dest,"wb")

	page = URLclass.open(url)
	"""
	Try adding get name function using page.info().headers or from url
	"""

	numBytes = 0
	fileSize = int(page.headers['Content-Length'])



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

def download_resume(url, dest = check_os(), hash = None, timeout = 10):
	"""
	"""
	myUrlclass = myURLOpener()
	if os.path.exists(dest):
        outputFile = open(dest,"ab")
        existSize = os.path.getsize(dest)
        # If the file exists, then download only the remainder
        myUrlclass.addheader("Range","bytes=%s-" % (existSize))
    else:
        outputFile = open(dest,"wb")

    file = myUrlclass.open(url)
