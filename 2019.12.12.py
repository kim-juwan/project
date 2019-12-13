import urllib,json,csv,requests
from bs4 import BeautifulSoup

f = open('database.csv', 'a', newline = '', encoding='utf-8')
wr = csv.writer(f)

for i in range(1,3):
    open_api = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=129.088003,35.233020,129.090083,35.231322&x=129.090399&y=35.229574&sort=distance&page=%s'%i
    api_key = 'f56b92905ade194d1254314f9e91d103'
    
    res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
    dic1 = res.json()
    results = dic1['documents']
    meta = dic1['meta']['is_end']
    # print(meta)
    for result in results:
        name = result['place_name']
        address = result['road_address_name']
        category = result['category_name']
        phone = result['phone']
        distance = int(result['distance'])
        url = result['place_url']
        x = float(result['x'])
        y = float(result['y'])
        result_list = [name, address, category, phone, distance, url, x, y]
        print('상호명:'+name)
        print('주소:'+address)
        print('카테고리:'+category)
        print('전화번호:'+phone)
        print('거리:'+str(distance)+'m')
        # print(result_list)
        print()
    
        wr.writerow(result_list)
f.close()
