#!/usr/bin/env python
import os

from fdfs_client import __version__

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

sdict = {
    'name': 'py3fdfsv2',
    'version': __version__,
    'description': 'Python client for Fastdfs ver 4.06',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'scott yuan',
    'author_email': 'scottzer8@gmail.com',
    'maintainer': 'Jian Dai',
    'maintainer_email': 'daijian1@qq.com',
    'keywords': ['Fastdfs', 'Distribute File System'],
    'license': 'GPLV3',
    'packages': ['fdfs_client'],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
    # 'ext_modules' : [Extension('fdfs_client.sendfile',
    #                          sources = ['fdfs_client/sendfilemodule.c'])],
}

setup(**sdict)
