# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:55:55 2016

@author: minkyu
"""

# for getting html file from url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import chardet

class URLHandler():
    def __init__(self, url):
        self.url = url
        self.urldata = urlopen(url)
    
    # make url as string
    def url_parser(self):
        # this encoding should be checked automatically
        data = self.urldata.read()
        encoding = chardet.detect(data)
        new_url_data = str(data.decode(encoding['encoding']))
        return new_url_data
    
    def html_parser(self):
        url_data = self.url_parser()
        soup = BeautifulSoup(url_data, 'lxml')
        valid_list = soup.find_all('table')
        for elm in valid_list:
            row_lists = elm.find_all('td')
            print(row_lists)
        return valid_list
        
    # put refined data into DB
    def store_db(self, db_path):
        pass
       
if __name__=='__main__':
    mm = URLHandler('http://espn.go.com/mlb/playbyplay?gameId=350615102')
    #mm = URLHandler('https://docs.python.org/3/library/html.parser.html')
    
    dd = mm.html_parser()
    #print(dd)