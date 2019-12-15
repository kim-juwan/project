from selenium import webdriver
from bs4 import BeautifulSoup
import time, urllib.request
import requests
from selenium.webdriver import ChromeOptions
import json
import csv
import random
import os
import cx_Oracle as oci

#출발점 35.229574, 129.090399
#출발지 id = 566719727
#길찾기링크
#https://map.kakao.com/?map_type=TYPE_MAP&target=car&rt=,,974789,487247&rt1=&rt2=%EC%A3%BC%EC%9D%B8%EC%9D%98%EC%A3%BC%EB%B0%A9%20%EB%B6%80%EC%82%B0%EB%8C%80%EC%A0%90&rtIds=,844561318
# ServiceKey = 'sUcH%2FwCaqWYGBXIDnxw8DtVEwOJBy%2BVOyP0Vjekhc8%2FNN%2BQnpcyOyu%2BQcID8%2FvQ5Fxhe60%2F3QfsQEApZAoovbQ%3D%3D'
# open_api = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=300&cx=129.090399&cy=35.229574&ServiceKey='+ServiceKey


# res = requests.get(open_api)
# soup = BeautifulSoup(res.content, 'lxml')

# print(soup)
##################################################################################################################################
# # f = open('database.csv', 'a', newline = '', encoding='utf-8')
# # wr = csv.writer(f)

# for i in range(1,4):
#     open_api = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=129.088003,35.231322,129.089043,35.230473&x=129.090399&y=35.229574&sort=distance&page=%s'%i
#     api_key = 'f56b92905ade194d1254314f9e91d103'

#     res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
#     dic1 = res.json()
#     results = dic1['documents']
#     meta = dic1['meta']['is_end']
#     # print(meta)
#     for result in results:
#         name = result['place_name']
#         address = result['road_address_name']
#         category = result['category_name']
#         phone = result['phone']
#         distance = int(result['distance'])
#         url = result['place_url']
#         x = float(result['x'])
#         y = float(result['y'])
#         result_list = [name, address, category, phone, distance, url, x, y]
#         # print(result)
#         print('상호명:'+name)
#         print('주소:'+address)
#         print('카테고리:'+category)
#         print('전화번호:'+phone)
#         print('거리:'+str(distance)+'m')
#         # print(result_list)
#         print()
    
# #         wr.writerow(result_list)
# # f.close()
##########################################################################################################################
# # f = open('database.csv', 'a', newline = '', encoding='utf-8')
# # wr = csv.writer(f)

# #3.4 4.5    치코파닭, 치밥도시락
# #3.3 4.4    야미요미케이크, 감골수육국밥, 태창식당, 박기모조방낙지
# #3.2 4.3    비작 부산대점, 구름다리쌈도둑, 아사로바다야끼, 대패1900 부산대점, 역전, 날마다부엌
# #3.2 4.25   장인식빵 부산대점, 연화리, 오시게식육실비, 우럭잡는김선장, 한성식당, 살아있네문어
# #3.2 3-1.4-1 장인식빵 부산대점, 오시게식육실비, 텐시이자카야, 맘스터치 부산대2호점, 부산핫바다704 부산대본점, 벤스하버
# #3,2.5 3.5,3 한솥도시락 부산대역앞점, 장인식빵 부산대점
# #3.5,2 4,2.5 거꾸로가는시계 부산대역점, 우럭잡는김선장
# #3.5,2.5 4,3 오투정거장, 시네마뷔페
# #3,1 4,2    키친 노리터, 살몬마켓 부산대점, 라이코스, 계성상회, 이시봉족발보쌈 금정1호점, 미가도시락
# #2,4 3,5    섬진강재첩국, 친구푸드 부곡점
# #2,3 3,4    국수나무 부산대역점, 바우네나주곰탕 부곡점
# #2,2 2.5,2.5 오니기리와이규동 부산대지하철역점, 동해옥순대요리 부산대점, 스시심 타카이, 마당쇠돼지갈비 부산대점
# open_api = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=129.088003,35.231322,129.089043,35.230473&x=129.090399&y=35.229574&sort=distance&page=2'
# api_key = 'f56b92905ade194d1254314f9e91d103'

# res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
# dic1 = res.json()
# results = dic1['documents']
# meta = dic1['meta']['is_end']
# print(meta)
# for result in results:
#     name = result['place_name']
#     address = result['road_address_name']
#     category = result['category_name']
#     phone = result['phone']
#     distance = int(result['distance'])
#     url = result['place_url']
#     x = float(result['x'])
#     y = float(result['y'])
#     result_list = [name, address, category, phone, distance, url, x, y]
#     print('상호명:'+name)
#     print('주소:'+address)
#     print('카테고리:'+category)
#     print('전화번호:'+phone)
#     print('거리:'+str(distance)+'m')
#     # print(result_list)
#     print()

# #     wr.writerow(result_list)
# # f.close()
###################################################################################################################################################################################
# f = open('database1.csv','r')

# rd = csv.reader(f)

# for row in rd:
#     url = row[5]
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, 'lxml')
    # mydata = soup.find('title')
    # print(row[5])

# f.close()
###############################################
# # url = 'https://place.map.kakao.com/890873444'
# # url = 'https://place.map.kakao.com/27503177'
# # url = 'https://place.map.kakao.com/20057605'
# # url = 'https://place.map.kakao.com/607827435'
# # url = 'https://place.map.kakao.com/1236108011'
# # url = 'https://place.map.kakao.com/27457937'
# # url = 'https://place.map.kakao.com/844561318'
# url = 'https://place.map.kakao.com/742542844'
# # # res = requests.get(url)
# # # soup = BeautifulSoup(res.content, 'lxml')
# # # print(res.text)
# # # name = soup.find('h2',class_='tit_location').text.split('\n')[0]
# # # print(name)

# driver = webdriver.Chrome('./chromedriver.exe')
# driver.get(url)
# time.sleep(1)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# name = soup.find('h2',class_='tit_location').text
# # fold = soup.find('div', class_='fold_floor')
# week_list = []

# if soup.find('strong',class_='tit_operation') is not None:
#     if soup.find('div', class_= 'fold_contact') is None:
#         week1 = soup.find('strong',class_='tit_operation').text.split('\n')[0]
#         week_list.append(week1)
# # if fold is not None:
# #     stripped = fold.text.strip()
# #     print(stripped)

# week2 = soup.find_all('span', class_='txt_operation')
# # print(week2)
# for week3 in week2:
    
#     week3 = week3.text.strip()
#     # print(week3)
#     week_list.append(week3)

# if len(week_list) > 1 :
#     week4 = str(week_list[0])
#     for i in range(1, len(week_list)):
#         week4 += (' '+str(week_list[i]))

# driver.find_element_by_class_name('frame_g').click()
# time.sleep(1)
# img_soup = BeautifulSoup(driver.page_source, 'lxml')

# try:
#     img_url = img_soup.find('img', class_= 'img_photo').get('src')
#     savename = 'C:/Users/admin/Documents/crawling/'+name+'.jpg'
#     img = urllib.request.urlopen('https:'+img_url).read()

#     with open(savename, mode='wb')as f:
#         f.write(img)
# except:
#     print('이미지 없음')

# print(name)
# try:
#     print(week4)
# except:
#     print('영업시간정보 없음')

# # week1 = week.split(' ')[0]
# # week = soup.find('div', class_='location_present').text.strip().replace(' ','')
# # week1 = week.split('\n')
# # print(week1[0], ':', week1[-1])
# # print(week1)
# # for i in week1:
    
# driver.close()
################################################################################################################################
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #브라우저 안 보임
# chrome_options.add_argument('disable-gpu') # 가속 사용 x
# chrome_options.add_argument('lang=ko_KR') # 가짜 플러그인 탑재

# # driver.get(url)
# # driver.implicitly_wait(초) #페이지 로드 기다림

# # chrome_options = Options()
# # chrome_options.add_argument('--headless')
# f = open('database1.csv','r')

# rd = csv.reader(f)

# for row in rd:
#     driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
#     url = row[5]
#     driver.get(url)
#     time.sleep(3)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     name = soup.find('h2',class_='tit_location').text
#     week_list = []

#     if soup.find('strong',class_='tit_operation') is not None:
#         if soup.find('div', class_= 'fold_contact') is None:
#             week1 = soup.find('strong',class_='tit_operation').text.split('\n')[0]
#             week_list.append(week1)

#     week2 = soup.find_all('span', class_='txt_operation')

#     for week3 in week2:
#         week3 = week3.text.strip()
#         week_list.append(week3)
    
#     if len(week_list) > 1 :
#         week4 = str(week_list[0])
#         for i in range(1, len(week_list)):
#             week4 += (' '+str(week_list[i]))

#     driver.find_element_by_class_name('frame_g').click()
#     time.sleep(1)
#     img_soup = BeautifulSoup(driver.page_source, 'lxml')

#     try:
#         img_url = img_soup.find('img', class_= 'img_photo').get('src')
#         savename = 'C:/Users/admin/Documents/crawling/img/'+name+'.jpg'
#         img = urllib.request.urlopen('https:'+img_url).read()

#         with open(savename, mode='wb')as f:
#             f.write(img)
#     except:
#         print('이미지 없음')

#     print(name)
#     try:
#         print(week4)
#     except:
#         print('영업시간정보 없음')
    
#     driver.implicitly_wait(3)
# f.close()
##########################################################################################################################
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #브라우저 안 보임
chrome_options.add_argument('disable-gpu') # 가속 사용 x
chrome_options.add_argument('lang=ko_KR') # 가짜 플러그인 탑재

cursor = conn.cursor()
# id_sql = 'SELECT ID FROM REST'
# cursor.execute(id_sql)
# rows = cursor.fetchall()
f = open('database1.csv','r',encoding='utf-8')
rows = csv.reader(f)

for row in rows:
    # row = list(row)
    driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
    url = 'https://place.map.kakao.com/'+str(row[0])

    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    name = soup.find('h2',class_='tit_location').text
    week_list = []
    print(name)
    if soup.find('strong',class_='tit_operation') is not None:
        if soup.find('div', class_= 'fold_contact') is None:
            week1 = soup.find('strong',class_='tit_operation').text.split('\n')[0]
            week_list.append(week1)

    week2 = soup.find_all('span', class_='txt_operation')

    for week3 in week2:
        week3 = week3.text.strip()
        week_list.append(week3)

    if len(week_list) > 1 :
        week4 = str(week_list[0])
        for i in range(1, len(week_list)):
            week4 += (' '+str(week_list[i]))
    # week4 = ' '.join(week_list)
    menu3 = []
    menu4 = ''
    menu5 = ''
    menu6 = ''
    if soup.find('ul',class_='list_menu') is not None:
        menu_list = soup.find('ul',class_='list_menu').find_all('li',class_='photo_type')
        for menu in menu_list:
            menu_li1 = menu.find('div',class_='info_menu').text.strip().replace('명:','').split('\n')
            
            if len(menu_li1) > 2:
                if menu_li1[0] == menu_li1[2]:
                    menu_li2 = [menu_li1[0],menu_li1[1]]
                else:
                    menu_li2 = [menu_li1[0],menu_li1[1],menu_li1[2]]
                    
            elif len(menu_li1) == 2:
                menu_li2 = [menu_li1[0],menu_li1[1]]
            else:
                menu_li2 = [menu_li1[0]]

            menu2 = ' / '.join(menu_li2)

            menu3.append(menu2)

        menu4 = ' | '.join(menu3)
    
    
        menu_list = soup.find('ul',class_='list_menu').find_all('li',class_='nophoto_type')
        for menu in menu_list:
            menu_li1 = menu.find('div',class_='info_menu').text.strip().replace('명:','').split('\n')
            if len(menu_li1) > 2:
                if menu_li1[0] == menu_li1[2]:
                    menu_li2 = [menu_li1[0],menu_li1[1]]
                else:
                    menu_li2 = [menu_li1[0],menu_li1[1],menu_li1[2]]
                    
            elif len(menu_li1) == 2:
                menu_li2 = [menu_li1[0],menu_li1[1]]
            else:
                menu_li2 = [menu_li1[0]]


            menu2 = ' / '.join(menu_li2)
            menu3.append(menu2)
        menu5 = ' | '.join(menu3)
    
    
        menu_list = soup.find('ul',class_='list_menu').find_all('li',class_='menuonly_type')
        for menu in menu_list:
            menu_li1 = menu.find('div',class_='info_menu').text.strip().replace('명:','').split('\n')
        
            

            menu3.append(menu_li1[0])


        menu6 = ' | '.join(menu3)
    
    
    try:    
        driver.find_element_by_class_name('frame_g').click()
        time.sleep(1)
        img_soup = BeautifulSoup(driver.page_source, 'lxml')
    except:
        pass
    img=''
    try:
        img_url = img_soup.find('img', class_= 'img_photo').get('src')
        img = urllib.request.urlopen('https:'+img_url).read()
    except:
        pass
    try:
        tr_menu = [(menu4 +' | '+ menu5 +' | '+ menu6).strip(' | '), row[0]]
        week_sql = 'UPDATE REST SET MENU=:1 WHERE ID=:2'
        cursor.execute(week_sql, tr_menu)
        print(tr_menu)
    except:
        pass
    
    try:
        tr_week = [week4, row[0]]
        week_sql = 'UPDATE REST SET WEEK=:1 WHERE ID=:2'
        cursor.execute(week_sql, tr_week)
        print(tr_week)

    except:
        pass

    try:
        tr_img = [img, row[0]]
        img_sql = 'UPDATE REST SET IMAGE=:1 WHERE ID=:2'
        cursor.execute(img_sql, tr_img)
        # print(img)
    except:
        pass

    driver.implicitly_wait(3)
    
    conn.commit()
    driver.quit()
