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
        self.urldata = urlopen(url)
    
    # make url as string
    def url_parser(self):
        # this encoding should be checked automatically
        data = self.urldata.read()
        encoding = chardet.detect(data)
        new_url_data = str(data.decode(encoding['encoding']))
        return new_url_data
    
    def html_parser(self, data_from='espn'):
        if data_from.lower() == 'espn':
            return self.data_from_espn()
        elif data_from.lower() == 'statcast':
            return self.data_from_baseball_savant()
        elif data_from.lower() == 'battlenet':
            return self.data_from_battle_net()
        else:
            raise NotImplementedError()
    
    # battle net
    def data_from_battle_net(self):
        pass
    
    # statcast
    # it returns list of dictionary
    def data_from_baseball_savant(self):
        url_data = self.url_parser()
        soup = BeautifulSoup(url_data, 'lxml')
        valid_list = soup.find_all('script')
        for elm in valid_list:
            if 'leaderboard_data' in str(elm):
                data = str(elm).split('leaderboard_data = ')[1].split('</script>')[0]
                data = data.replace('\n','')
                data = data.replace(';','')
        return json.loads(data)
            
    # espn play-by-play data
    def data_from_espn(self):
        url_data = self.url_parser()
        soup = BeautifulSoup(url_data, 'lxml')
        valid_list = soup.find_all('table')
        is_valid = False
        valid_data = []
        # table parser
        for elm in valid_list:
            row_lists = elm.find_all('tr')
            one_inning = []
            for row in row_lists:
                new_row = list(row.find_all('td'))
                if len(new_row) != 0:
                    # this condition is only for espn data, so this file should be moved to MajorLeague project
                    #if is_valid:
                    #    valid_data.append(new_row)
                    if 'Play-By-Play' in str(new_row[0]):
                        is_valid = True
                if is_valid:
                    if len(new_row) != 0:
                        one_inning.append(new_row)
                    else:
                        if len(one_inning) != 0:
                            valid_data.append(one_inning)
                            one_inning = []
        # parser each cell
        html_return = []
        for inning in valid_data:
            inn = []
            for data in inning:
                row = []
                for column in data:
                    column =  str(column)
                    parsed_column = column.split('<')
                    for elm in parsed_column:
                        if not elm.endswith('>') and elm != '':
                            real_data = elm.split('>')[1]
                            break
                    row.append(real_data)
                inn.append(row)
            html_return.append(inn)
        return html_return
        
    # put refined data into DB
    def store_db(self, db_path):
        pass
       
if __name__=='__main__':
    url = 'https://baseballsavant.mlb.com/statcast_leaderboard'
    mm = URLHandler(url = url, year = 2016, abs = 30, player_type = 'pitcher')
    dd = mm.html_parser('statcast')
