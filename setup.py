from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gmail_rest/__init__.py
from gmail_rest import __version__ as version

setup(
	name="gmail_rest",
	version=version,
	description="access gmail using rest api and oauth authentication",
	author="tridz",
	author_email="fadil@tridz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
