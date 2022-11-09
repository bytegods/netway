from setuptools import setup, find_packages


setup(
    name='netway',
    version='0.1',
    license='MIT',
    author="Thesaderror & Mein",
    author_email='saderroraz@protonmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords='sockets, request, http, https, get, port, fast',
    install_requires=[
          'sockets',
          'threading',
      ],

)
