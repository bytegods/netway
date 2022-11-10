from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='netway',
    description='Python internet library',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='',
    author='Thesaderror & Mein',
    author_email='saderroraz@protonmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='sockets, request, http, https, get, port, fast',
    packages=find_packages(),
    install_requires=['sockets']
)
