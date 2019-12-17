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
##########################################################################################################################
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #브라우저 안 보임
chrome_options.add_argument('disable-gpu') # 가속 사용 x
chrome_options.add_argument('lang=ko_KR') # 가짜 플러그인 탑재

cursor = conn.cursor()
id_sql = 'SELECT ID FROM REST'
cursor.execute(id_sql)
rows = cursor.fetchall()

for row in rows:
    driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
    url = 'https://place.map.kakao.com/'+str(row[0])

    driver.get(url)
    time.sleep(3) #데이터 뜰때까지 기다려주는 시간
    soup = BeautifulSoup(driver.page_source, 'lxml')
    name = soup.find('h2',class_='tit_location').text
    week_list = []
    week4=[]

    if soup.find('strong',class_='tit_operation') is not None:  #영업시간 가져오는..
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
            week4 += (' '+str(week_list[i])) ##영업시간 가져오는

    menu3 = []
    menu4 = ''
    menu5 = ''
    menu6 = ''
    if soup.find('ul',class_='list_menu') is not None:
        menu_list1 = soup.find('ul',class_='list_menu').find_all('li',class_='photo_type')
        for menu in menu_list1:
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
    
    
        menu_list2 = soup.find('ul',class_='list_menu').find_all('li',class_='nophoto_type')
        for menu in menu_list2:
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
    
        menu_list3 = soup.find('ul',class_='list_menu').find_all('li',class_='menuonly_type')
        for menu in menu_list3:
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
