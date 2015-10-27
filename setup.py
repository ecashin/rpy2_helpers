# python2.7 setup.py sdist

from setuptools import setup


setup(
    name='rpy2_helpers',
    description='Easier R use from Python',
    author='Ed L. Cashin',
    author_email='ed.cashin@acm.org',
    url='https://github.com/ecashin/rpy2_helpers',
    version='0.1',
    scripts = ['rpy2_helpers.py'],
    install_requires=[
        'click',
        'numpy',
        'rpy2',
    ],
)
