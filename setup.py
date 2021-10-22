import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
readme = ""
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        readme = f.read()

setup(
    name='dhcp',
    version='1.0.2',
    description='A Netbox plugin for dhcp service management',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/anderson-acrs/dhcp',
    author='anderson claudio',
    license='GNU General Public License v3.0',
    package_data={
        '': ['LICENSE'],
    },
    install_requires=[],
    packages=find_packages(),
    include_package_data=True
)
