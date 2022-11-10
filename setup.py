from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.7'
DESCRIPTION = 'Python internet library'
LONG_DESCRIPTION = "Netway is python library that allows you to send HTTP requests and receive responses,create socket servers and more..."

# Setting up
setup(
    name="netway",
    version=VERSION,
    author="Thesaderror & Mein",
    author_email="saderroraz@protonmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['sockets'],
    keywords=['sockets', 'request', 'http', 'https', 'get', 'port', 'fast'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)