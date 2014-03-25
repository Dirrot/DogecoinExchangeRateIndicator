#!/usr/bin/env python2

#from distutils.core import setup
from setuptools import setup

setup(name = 'DogecoinExchangeRateIndicator',
      version = '0.1',
      description = 'Python indicator for displaying the latest exchange rate of dogecoin/bitcoin at cryptsy.com',
      long_description = '',
      author = 'Dirk Rother',
      author_email = 'dirrot.dev@gmail.com',
      license = "GNU General Public License version 2 or later",
      url = 'https://github.com/Dirrot/python-indicator-dogecoin-cryptsy-exchange-rate',
      packages = [],
#      install_requires = ['libappindicator'],
      data_files = [
            ('/opt/extras.ubuntu.com/DogecoinExchangeRateIndicator', [
                'DogecoinExchangeRateIndicator/__init__.py',
                'DogecoinExchangeRateIndicator/constants.py',
                'DogecoinExchangeRateIndicator/cryptsy.py',
                'DogecoinExchangeRateIndicator/DogecoinExchangeRateIndicator.py']),
            ('/opt/extras.ubuntu.com/DogecoinExchangeRateIndicator/share', [
                'README.md', 
                'LICENSE',
                'img/donation-qr-code.png']),
            ('/opt/extras.ubuntu.com/DogecoinExchangeRateIndicator/icons', [
                'DogecoinExchangeRateIndicator/icons/the_d.jpg', 
                'DogecoinExchangeRateIndicator/icons/logo_cryptsy.jpg', 
                'DogecoinExchangeRateIndicator/icons/logo_bitcoinwisdom.png']),
            ('/usr/bin', [
                'scripts/indicator-dogecoin'])],
      keywords = "dogecoin exchange rate indicator cryptcurrency",
      classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: X11 Applications',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Office/Business :: Financial'],
      )

