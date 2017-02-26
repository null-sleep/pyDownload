
try:
	from setuptools import setup, find_packages
except ImportError as e:
	from distutils.core import setup

dependencies = ['docopt', 'termcolor', 'requests']

setup(
	name = 'pyDownload',
	version = '1.0.2',
	description = 'CLI based download utility',
	url = 'https://github.com/Dhruv-Jauhar/pyDownload',
	author = 'Dhruv Jauhar',
	author_email = 'dhruv.jhr@gmail.com',
	license = 'MIT',
	install_requires = dependencies,
	packages = find_packages(),
	entry_points = {
		'console_scripts': ['pyd = pyDownload.main:start'],
	},
	classifiers=(
		'Development Status :: 4 - Beta',
		'Intended Audience :: End Users/Desktop',
		'Natural Language :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.4',
		#'Programming Language :: Python :: 3 :: Only',
		'Topic :: Utilities'

	)
)
