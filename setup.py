
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='netway',
    version='0.4',
    license='MIT',
    description="Python internet library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Thesaderror & Mein",
    author_email='saderroraz@protonmail.com',
    packages=find_packages('src'),
    package_dir={'./netway': 'src'},
    url='',
    keywords='sockets, request, http, https, get, port, fast',
    install_requires=[
          'sockets'
      ],

)