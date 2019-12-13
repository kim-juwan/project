from django.db import models
import cx_Oracle as oci
# Create your models here.
from django.db import connection
import random

class Database():
    ## 오름차순 정렬로 데이터 베이스에서 가져오기
    def __init__(self):
        self.cursor = connection.cursor()

    def Select_Desc(self):
        select_sql = 'SELECT * FROM REST ORDER BY ID DESC'
        self.cursor.execute(select_sql)
        result_data = self.cursor.fetchall()
        return result_data
    ## 내림차순 정렬로 데이터 베이스에서 가져오기
    def Select_Asc(self):
        select_sql = 'SELECT * FROM REST ORDER BY ID ASC'
        self.cursor.execute(select_sql)
        result_data = self.cursor.fetchall()
        return result_data
    def Select_Search(self,search_word):
        search_sql="SELECT * FROM REST WHERE NAME LIKE '%'|| :text ||'%' ORDER BY DIST ASC"
        self.cursor.execute(search_sql,text=search_word)
        result_data = self.cursor.fetchall()
        return result_data

class Func():
    def randnum(self,data,n):
        sample_data = random.sample(data,n)
        return sample_data
