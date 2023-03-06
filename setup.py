
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='QTPyLib',
    version='1.5.84',
    description='Quantitative Trading Python Library',
    long_description=long_description,
    url='https://github.com/Atila027/algo-trading-platform-interactive-IB.git',
    author='Atila',
    author_email='atila423027@gmail.com',
    license='LGPL',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    platforms = ['any'],
    keywords='qtpylib qtpy algotrading algo trading interactive brokers tws ibgw ibpy ezibpy',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    install_requires=[
        'python-dateutil>=2.5.3','ezibpy>=1.12.66',
        'flask>=0.11.1','numpy>=1.11.1','pandas>=0.22.0','pymysql>=0.7.6',
        'pytz>=2016.6.1','requests>=2.10.0','pyzmq>=15.2.1',
        'nexmo>=1.2.0','twilio>=5.4.0','ibpy2>=0.8.0',
    ],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    include_package_data=True,
    package_data={
        'static': ['qtpylib/_webapp/*'],
        'db': ['qtpylib/schema.sql*']
    },
)
