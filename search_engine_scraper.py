from bs4 import BeautifulSoupimport requestsprint('Please enter URL: ')yahoo_url = 'https://search.yahoo.com/search;_ylt=AwrCxh_mDgVYT2wAbW5XNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10BGdwcmlkA0MwUHZqaUNSUU9HeUh6X3RnLng4ekEEbl9yc2x0AzAEbl9zdWdnAzMEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI2BHF1ZXJ5A2RhbWllbiUyMGhvYmRheSUyMGZhY2Vib29rBHRfc3RtcAMxNDc2NzUyMjYy?p=damien+hobday+facebook&fr2=sb-top&fr=yfp-t&fp=1'bing_url = 'http://www.bing.com/search?q=damien%20hobday%20facebook&qs=n&form=QBRE&pq=damien%20hobday%20fa&sc=0-16&sp=-1&sk=&cvid=F5C85FA16CC44354BBFD2108EFF2337C'yahoo_r = requests.get(yahoo_url)bing_r = requests.get(bing_url)yahoo_data = yahoo_r.contentbing_data = bing_r.contentyahoo_soup = BeautifulSoup(yahoo_data,'html.parser')bing_soup = BeautifulSoup(bing_data,'html.parser')yahoo_list = []bing_list = []if 'yahoo' in yahoo_url:    for x in yahoo_soup.find_all('ol', class_= 'mb-15 reg searchCenterMiddle'):        for y in x.find_all('a'):            if '98.139.21.31' not in (y.get('href')):                yahoo_list.append(y.get('href'))if 'bing' in bing_url:    for x in bing_soup.find_all('ol', id= 'b_results'):        for y in x.find_all('a'):            #if '98.139.21.31' not in (y.get('href')):            if isinstance((y.get('href')), str) and 'search?q' not in y.get('href'):                bing_list.append(y.get('href'))print (yahoo_list)print (bing_list)#yahoo class=:"mb-15 reg searchCenterMiddle"