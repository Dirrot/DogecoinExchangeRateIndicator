#!/usr/bin/python -tt
'''
Created on 13.02.2014

@author: Dirk Rother
@contact: dirrot.dev@gmail.com
@license: GPL
@version: 0.1

'''

import os
import gtk
import appindicator
import webbrowser
from decimal import Decimal
from cryptsy import CryptsyAPI
from constants import Constants

class DogecoinExchangeRateIndicator():
    '''
    This class represents an indicator, which displays the current
    value of the dogecoin/bitcoin exchange rate using the available 
    informations at cryptsy.com
    '''
    
    '''
    Updates the exchange price of dogecoin/bitcoin every x seconds.
    '''
    PING_FREQUENCY = 3
    
    def __init__(self):
        '''
        Simple constructor for the indicator.
        '''
        self.api = CryptsyAPI()  
        self.ind = appindicator.Indicator("IndicatorDogecoinValue", Constants.ICON_PATH,appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_label('0')
        self.menu = gtk.Menu()
        self._setupMenu()
        self.ind.set_menu(self.menu)    
        
    def _setupMenu(self):
        '''
        This method generates the indicators menues.
        '''
        
        ''' cryptsy '''
        menu_cryptsy = gtk.ImageMenuItem("cryptsy.com")
        image_cryptsy = gtk.Image()
        image_cryptsy.set_from_file(Constants.ICON_CRYPTSY)
        menu_cryptsy.set_image(image_cryptsy)
        menu_cryptsy.set_always_show_image(True)
        menu_cryptsy.connect("activate", self._openBrowserWithCryptsy, "Start", self.ind)
        menu_cryptsy.show()
        self.menu.append(menu_cryptsy)
        
        ''' bitcoinwisdom '''
        menu_bitcoinwisdom = gtk.ImageMenuItem("bitcoinwisdom.com")
        image_bitcoinwisdom = gtk.Image()
        image_bitcoinwisdom.set_from_file(Constants.ICON_BITCOINWISDOM)
        menu_bitcoinwisdom.set_image(image_bitcoinwisdom)
        menu_bitcoinwisdom.set_always_show_image(True)
        menu_bitcoinwisdom.connect("activate", self._openBrowserWithBitcoinwisdom, "Start", self.ind)
        menu_bitcoinwisdom.show()
        self.menu.append(menu_bitcoinwisdom)
        
        ''' exit '''
        menu_exit = gtk.MenuItem("exit")
        menu_exit.connect("activate", gtk.main_quit)
        self.menu.append(menu_exit)
    
    def _openBrowserWithCryptsy(self, widget, optionName, indicator):
        '''
        This method executes the given command to open the cryptsy website
        in the browser.
        ''' 
        webbrowser.open(Constants.URL_CRYPTSY)
        return True
    
    def _openBrowserWithBitcoinwisdom(self, widget, optionName, indicator):
        '''
        This method executes the given command to open the cryptsy website
        in the browser.
        '''
        webbrowser.open(Constants.URL_BITCOINWISDOM)
        return True
    
    def _getCurrentValue(self): 
        '''
        This method get the current value of the dogecoin/bitcoin exchange rate
        and formats it to the satoshi representation. 
        '''
        value = self.api.getLatestDogePrice()
        format_value = 0
        if value != "0":
            format_value = Decimal(value) * Decimal("1E8")
        self.ind.set_label(str(format_value))  
        return True
         
    def main(self):
        '''
        Runs and updates the Indicator.
        '''  
        gtk.timeout_add(self.PING_FREQUENCY * 1000, self._getCurrentValue)
        gtk.main()

if __name__ == '__main__':
    '''
    Runs the indicator.
    '''
    indicator = DogecoinExchangeRateIndicator()
    indicator.main()
    
