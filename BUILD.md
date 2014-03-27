ppa/
└── dogecoinexchangerateindicator_0.1.3~saucy
    ├── applications
    │   └── DogecoinExchangeRateIndicator.desktop
    ├── debian
    │   ├── changelog
    │   ├── compat
    │   ├── control
    │   ├── copyright
    │   └── rules
    └── dogecoinexchangerateindicator
        ├── constants.py
        ├── cryptsy.py
        ├── DogecoinExchangeRateIndicator.py
        ├── icons
        │   ├── logo_bitcoinwisdom.png
        │   ├── logo_cryptsy.jpg
        │   └── the_d.jpg
        ├── __init__.py
        ├── scripts
        │   └── indicator-dogecoin
        └── share
            ├── donation-qr-code.png
            ├── LICENSE
            └── README.md

7 directories, 17 files

Steps:
cd ppa/dogecoinexchangerateindicator_0.1.3~saucy/debian
update changelog
update copyright
cd ../../
tar -czf dogecoinexchangerateindicator_0.1.3~saucy.tar.gz dogecoinexchangerateindicator_0.1.3~saucy/
mv dogecoinexchangerateindicator_0.1.3~saucy.tar.gz dogecoinexchangerateindicator_0.1.3~saucy.orig.tar.gz
cd dogecoinexchangerateindicator_0.1.3~saucy
debuild -S -k"0xGPGKEY" 
cd ..
dput ppa:dirrot/dogecoinexchangerateindicator dogecoinexchangerateindicator_0.1.3-0ubuntu1~saucy_source.changes

