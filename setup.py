#!/bin/env python
'''
Created on 18th of Feb, 2015

@author: Edwin Tye (Edwin.Tye@gmail.com)
'''
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pygot',
      version='0.1.0',
      description='Global Optimization Toolbox',
      long_description=readme(),
      author="Edwin Tye",
      author_email="Edwin.Tye@phe.gov.uk",
      packages=[
                'pygot',
                'pygot.direct',
                'pygot.gradient'
                ],
      license='LICENCE.txt',
      install_requires=[
                    'scipy',
                    'numpy'
                        ],
      test_suite='nose.collector',
      tests_require=[
                     'nose',
                     'numpy',
                     ],
      scripts=[]
      )