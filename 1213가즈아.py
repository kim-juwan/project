import json,csv,urllib,requests
from bs4 import BeautifulSoup

#csv파일로 DB생성
f=open('ddatebase.csv','a', newline='',encoding='utf-8')
wr=csv.writer(f)

#openapi열기
for i in range(1,4):
    open_api='https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=129.088003,35.233020,129.090083,35.231322&x=129.090399&y=35.229574&sort=distance&page=%s'%i
    api_key='f56b92905ade194d1254314f9e91d103'

    #데이터 가져오기
    res=requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key})
    dic1=res.json()
    results=dic1['documents']
    meta=dic1['meta']['is_end']

    for j in results:
        name= j['place_name']
        address=j['road_address_name']
        category=j['category_name']
        phone=j['phone']
        distance=int(j['distance'])
        url=j['place_url']
        x=float(j['x'])
        y=float(j['y'])
        
        results_list=[name,address,category,phone,distance,url,x,y]
        print('상호명:'+name)
        print('주소:'+address)
        print('카테고리:'+category)
        print('전화번호:'+phone)
        print('거리:'+str(distance)+'m')
        print()

        wr.writerow(results_list)
f.close()