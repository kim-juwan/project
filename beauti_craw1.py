from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.chrome.options import Options
import json
import cx_Oracle as oci
 

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()
   
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
                try:
                    category = result['category_name'].split('>')[1]
                    category = category.strip()
                except:
                    category = '기타'

                phone = result['phone']
                distance = int(result['distance'])
                url = result['place_url']
                new_url = url.replace('place.','').split('/')
                
                x = float(result['x'])
                y = float(result['y'])
                lists = [new_url[3],name,address,category,phone,distance,x,y]
               
                try:
                    insert_sql = 'INSERT INTO REST(ID,NAME,ADDR,CATE,PHONE,DIST,LNG,LAT) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)'
                    cursor.execute(insert_sql,lists)
                except:
                    print('pass')
                    pass
                    
                print(1)
            if meta == True:
                break
                
conn.commit()
print('끝')