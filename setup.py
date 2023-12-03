from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in habeshahomes/__init__.py
from habeshahomes import __version__ as version

setup(
	name="habeshahomes",
	version=version,
	description="HabeshaHomes: Simplifying real estate management. Effortlessly list, manage, and track properties with ease. Built for agents, developers, and property enthusiasts.",
	author="Yeabsera",
	author_email="yeabseradeveloper@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
