from setuptools import setup
import io

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='goodvibes2',
  packages=['goodvibes2'],
  version='3.2',
  description='A python program to compute corrections to thermochemical data from frequency calculations',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='TheorChemGroup',
  author_email='j.a.velmiskina@gmail.com',
  url='https://github.com/TheorChemGroup/GoodVibes2',
  download_url='https://github.com/TheorChemGroup/GoodVibes2/archive/refs/heads/master.zip',
  keywords=['compchem', 'thermochemistry', 'orca', 'gaussian', 'vibrational-entropies', 'temperature'],
  classifiers=[],
  install_requires=['numpy','cclib'],
  python_requires='>=3.7',
  include_package_data=True,
  entry_points={
    'console_scripts': [
        'goodvibes = goodvibes.GoodVibes:main',
    ],
  }
)
