"""setuptools configuration for adder"""
from setuptools import setup

setup(name='adder',
      version='0.1',
      description='A mighty package to add things',
      url='http://github.com/jamesmcdonald/adder',
      author='James McDonald',
      author_email='james@jamesmcdonald.com',
      license='MIT',
      packages=['adder'],
      zip_safe=False,
      test_suite='nose.collector',
      setup_requires=['nose', 'nosexcover', 'setuptools-lint'],
     )
