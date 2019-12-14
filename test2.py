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

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #브라우저 안 보임
chrome_options.add_argument('disable-gpu') # 가속 사용 x
chrome_options.add_argument('lang=ko_KR') # 가짜 플러그인 탑재


conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

cursor = conn.cursor()

driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
url = 'https://place.map.kakao.com/11877634'

driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')




name = soup.find('h2',class_='tit_location').text

# print(name)


week_list = []
if soup.find('strong',class_='tit_operation') is not None:
    if soup.find('div', class_= 'fold_contact') is None:
        week1 = soup.find('strong',class_='tit_operation').text.split('\n')[0]
        week_list.append(week1)

week2 = soup.find_all('span', class_='txt_operation')

for week3 in week2:
    week3 = week3.text.strip()
    week_list.append(week3)

week4 = ' '.join(week_list)
# print(type(week4))
try:
    tr_week = [week4, name]
    week_sql = 'UPDATE REST SET WEEK=:1 WHERE NAME=:2'
    cursor.execute(week_sql, tr_week)
    # print(tr_week)

except:
    pass


menu3 = []
menu4 = ''
menu5 = ''
menu6 = ''
if soup.find('ul',class_='list_menu').find('li',class_='photo_type') is not None:
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
    print(1)
if soup.find('ul',class_='list_menu').find('li',class_='nophoto_type') is not None:
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
    print(menu5)
if soup.find('ul',class_='list_menu').find('li',class_='menuonly_type') is not None:
    menu_list = soup.find('ul',class_='list_menu').find_all('li',class_='menuonly_type')
    for menu in menu_list:
        menu_li1 = menu.find('div',class_='info_menu').text.strip().replace('명:','').split('\n')
    
        

        menu3.append(menu_li1[0])


    menu6 = ' | '.join(menu3)
    print(3)


tr_menu = [(menu4 +' | '+ menu5 +' | '+ menu6).strip(' | '), name]
week_sql = 'UPDATE REST SET MENU=:1 WHERE NAME=:2'
cursor.execute(week_sql, tr_menu)
print(tr_menu)
driver.implicitly_wait(3)
driver.quit()
conn.commit()
