from selenium import webdriver
from bs4 import BeautifulSoup
import time, urllib.request, requests, json, csv, random, os
from selenium.webdriver import ChromeOptions
import cx_Oracle as oci

# conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
# cursor = conn.cursor()
# XY_sql = 'SELECT ID, LAT, LNG FROM REST'
# cursor.execute(XY_sql)
# rows = cursor.fetchall()
open_api = 'https://dapi.kakao.com/v2/local/geo/transcoord.json?x=37&y=127&input_coord=WGS84&output_coord=WCONGNAMUL'
api_key = 'f56b92905ade194d1254314f9e91d103'
res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
print(res)
for row in rows:
    id = row[0]
    y = row[1]
    x = row[2]
    
    open_api = 'https://dapi.kakao.com/v2/local/geo/transcoord.json?x=%s&y=%s&input_coord=WGS84&output_coord=WCONGNAMUL'%(x,y)
    api_key = 'f56b92905ade194d1254314f9e91d103'

    res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
    print(res)
    dic1 = res.json()

    xy = [int(dic1['documents'][0]['x']), int(dic1['documents'][0]['y']), id]
    cong_sql = 'UPDATE REST SET XCONG=:1, YCONG=:2 WHERE ID=:3'
    cursor.execute(cong_sql, xy)
    print(xy)
print('끝')
conn.commit()
