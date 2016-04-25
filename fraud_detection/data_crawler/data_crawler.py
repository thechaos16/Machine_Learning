# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:55:55 2016

@author: minkyu
"""

# for getting html file from url
from urllib.request import urlopen
from html.parser import HTMLParser
import chardet

class URLHandler(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.urldata = urlopen(url)
    
    # make url as string
    def url_parser(self):
        # this encoding should be checked automatically
        data = self.urldata.read()
        encoding = chardet.detect(data)
        new_url_data = str(data.decode(encoding['encoding']))
        return new_url_data
        
    # parse only data
    def handle_data(self, data):
        if 'Perez' in data:
            print(data)
            
    # put refined data into DB
    def store_db(self, db_path):
        pass
       
if __name__=='__main__':
    mm = URLHandler('http://espn.go.com/mlb/playbyplay?gameId=350615102')
    #mm = URLHandler('https://docs.python.org/3/library/html.parser.html')
    
    dd = mm.url_parser()
    mm.feed(dd)