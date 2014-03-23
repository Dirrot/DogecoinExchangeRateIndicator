#!/usr/bin/env python2

from distutils.core import setup
from os.path import abspath
from os.path import join as path_join
from os import getcwd
from shutil import rmtree

pathname        =        getcwd()

packages        =       ['IndicatorDogecoinExchangeRate']

setup(name            =        'IndicatorDogecoinExchangeRate',
      version        =        '0.1',
      description    =        'Python indicator for displaying the latest exchange rate of dogecoin/bitcoin at cryptsy.com',
      author        =        'Dirrot',
      author_email  =       'dirrot.dev@gmail.com',
      url            =        'https://github.com/Dirrot/python-indicator-dogecoin-cryptsy-exchange-rate',
      packages        =        packages,
      package_dir    =        {
                               'JDownloader.py' : abspath(path_join(pathname, 'IndicatorJDownloader/')), 
                               'JDRemote.py' : abspath(path_join(pathname, 'IndicatorJDownloader/'))
                            },
      data_files    =        [
                              ('share/IndicatorDogecoinExchangeRate', ['README.md', 'LICENSE','img/donation-qr-code.png']),
                              ('share/IndicatorDogecoinExchangeRate/icons', ['IndicatorDogecoinExchangeRate/icons/the_d.jpg', 'IndicatorDogecoinExchangeRate/icons/logo_cryptsy.jpg', 'IndicatorDogecoinExchangeRate/icons/logo_bitcoinwisdom.png']),
                              ('/usr/bin', ['scripts/indicator-dogecoin'])
                            ],
      

    )


try:
    rmtree(abspath(path_join(pathname, 'build/')))
except:
    pass
