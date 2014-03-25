#!/usr/bin/env python2

from distutils.core import setup
#from os.path import abspath
#from os.path import join as path_join
#from os import getcwd
#from shutil import rmtree

#pathname = getcwd()

packages = ['DogecoinExchangeRateIndicator']

setup(name = 'DogecoinExchangeRateIndicator',
      version = '0.1',
      description = 'Python indicator for displaying the latest exchange rate of dogecoin/bitcoin at cryptsy.com',
      long_description = '',
      author = 'Dirk Rother',
      author_email = 'dirrot.dev@gmail.com',
      url = 'https://github.com/Dirrot/python-indicator-dogecoin-cryptsy-exchange-rate',
      classifiers = [],
      packages = [],
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
                'scripts/indicator-dogecoin'])])


#try:
#    rmtree(abspath(path_join(pathname, 'build/')))
#except:
#    pass
