# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:55:55 2016

@author: minkyu
"""

# for getting html file from url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import chardet
import json

class URLHandler():
    def __init__(self, **kwargs):
        if 'url' not in kwargs:
            raise KeyError('URL should be in input argument!')
        self.url = str(kwargs['url'])
        if len(kwargs) >= 2:
            self.url += '?'
        for key, data in kwargs.items():
            if key == 'url':
                continue
            self.url += (key + '=' + str(data) + '&')
        self.urldata = urlopen(self.url)
    
    # make url as string
    def url_parser(self):
        # this encoding should be checked automatically
        data = self.urldata.read()
        encoding = chardet.detect(data)
        new_url_data = str(data.decode(encoding['encoding']))
        return new_url_data
    
    def html_parser(self, data_from='espn'):
        if data_from.lower() == 'battlenet':
            return self.data_from_battle_net()
        else:
            raise NotImplementedError()
    
    # battle net
    def data_from_battle_net(self):
        pass
    
    # league of legend crawler
    def data_from_(self):
        pass
    
    # put refined data into DB
    def store_db(self, db_path):
        pass
       
if __name__=='__main__':
    pass
