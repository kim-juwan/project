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

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')


cursor = conn.cursor()
id_sql = 'SELECT ID FROM REST'
cursor.execute(id_sql)

rows = cursor.fetchall()

for row in rows:
    week=''
    menu=''

    del_menu = [week,menu, row[0]]
    del_sql = f"UPDATE REST SET WEEK=\'{week}\',MENU=\'{menu}\' WHERE ID={row[0]}"
    cursor.execute(del_sql)
    print(1)
    conn.commit()
