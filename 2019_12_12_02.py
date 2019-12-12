from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.chrome.options import Options
import json
import csv

f = open('database1.csv','w',newline='',encoding='utf-8')
wr = csv.writer(f)



lists = []
for j in range(16):
    dict1 = {}
    for i in range(16):
        dict1[129.085923 + (0.000520*i)] = (35.233020 - (0.0004245*j))
    lists.append(dict1)
    
for dict1 in lists:    
    for k,v in dict1.items():
        # print(k,v,k+0.000520,v-0.0004245)
        for i in range(1,4):    
            open_api = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=%s,%s,%s,%s&x=129.090399&y=35.229574&sort=distance&page=%s'%(k,v,k+0.000520,v-0.0004245,i)
            api_key = 'f56b92905ade194d1254314f9e91d103'
            # print(open_api)
            res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
            dic1 = res.json()
            results = dic1['documents']
            meta = dic1['meta']['is_end']
            
            for result in results:
                name = result['place_name']    
                address = result['road_address_name']
                category = result['category_name']
                phone = result['phone']
                distance = int(result['distance'])
                url = result['place_url']
                new_url = url.replace('place.','').split('/')
                new_url = new_url[0] + '//' + new_url[2] + '/link/map/' + new_url[3]
                x = float(result['x'])
                y = float(result['y'])
                lists = [name,address,category,new_url,phone,url,distance,x,y]
               
                
                wr.writerow(lists)
            if meta == True:
                break
                

f.closed
print('끝')