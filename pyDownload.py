import utlis.py
import os
dest = utils.check_os()
def pyDownload(url, dest, hash = None, timeout =10):
	if os.path.exists(dest):
		return
	chunk = 1000 * 1000
	temp_path = dest + '.pyd'
	current size = os