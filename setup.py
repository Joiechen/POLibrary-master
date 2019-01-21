# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('page_objects/__init__.py','rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='polibrary',
    version=version,
    url='',
    author='joiechen',
    author_email='joiechen@xingren.com',
    description='selenium_appium based Page Objects Library',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['selenium>=3.14.1','Appium-Python-Client==0.30'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    extras_require={
    },
)