'''
Created on 13.02.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

import logging
import json
from urllib2 import Request, urlopen
from urllib2 import HTTPError, URLError

class CryptsyAPI(object):
    
    ''' 
    The last know price.
    If the api query throws an exception or the api is
    temporally not available, this price would be displayed.
    After the api is available, this current price would be fetched
    and displayed.
    '''
    last_price = 0
    
    ''' 
    Enable debug file logging
    Enable:  logging.DEBUG 
    Disable: logging.INFO
    '''
    LOGGING = logging.INFO
    
    ''' Dogecoin ID'''
    CURRENCY_DOGECOIN_ID = 132
    
    def __init__(self):
        ''' Uncomment this line for file logging. '''
        #logging.basicConfig(filename = 'IndicatorDogecoinValue.log',format = '%(asctime)s [%(message)s]', level = self.LOGGING)
        if logging.getLogger(__name__).isEnabledFor(logging.DEBUG):
            logging.info('-------------------------------------------')
            logging.info('----------------- LOGGING -----------------')
    
    def _api_query(self):
        '''
        This method pulls the latest trading price from the cryptsy api.
        '''
        url = "http://pubapi.cryptsy.com/api.php?method={}&marketid={}".format("singlemarketdata", self.CURRENCY_DOGECOIN_ID)
        request = Request(url)
        
        try:
            response = urlopen(request)
            result = json.loads(response.read())
            
            if result['return'] != False:
                self.last_price = result
                
            if logging.getLogger(__name__).isEnabledFor(logging.DEBUG):
                logging.info('Data: %s ...', str(result)[0:50])
                
            return result
        except HTTPError as e:
            if logging.getLogger(__name__).isEnabledFor(logging.DEBUG):
                logging.info('HTTPError: The Server couldn\'t fulfill the request. Error code: %s', str(e.code))
            return self.last_price
        except URLError as e:
            if logging.getLogger(__name__).isEnabledFor(logging.DEBUG):
                logging.info('URLError: We failed to reach a server. Reason: %s', str(e.code))
            return self.last_price
        else:
            # Everything is fine.
            pass         
    
    def getLatestDogePrice(self):
        '''
        This method returns the latest exchange price.
        '''
        
        data = self._api_query()
        
        try:
            '''
            Gets from the latest trade the current price.
            '''
            return data['return']['markets']['DOGE']['recenttrades'][0]['price']
        except:
            
            if logging.getLogger(__name__).isEnabledFor(logging.DEBUG):
                logging.debug('Failed: ', str(data))
            
            ''' 
            If the server api doesn't provide any informations during
            the first api_query request. Error code: 502
            '''
            if self.last_price == 0:
                return "0"
            
            '''
            If the server api doesn't provide any informations, but the
            query request has been succeded.
            '''
            if data['return'] == False:
                return self.last_price['return']['markets']['DOGE']['recenttrades'][0]['price']
            
            '''
            If the server couldn't fulfill the request (error 502) the latest
            known exchange rate would be used.
            '''
            return self.last_price['return']['markets']['DOGE']['recenttrades'][0]['price']
