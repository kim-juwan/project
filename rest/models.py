from django.db import models
import cx_Oracle as oci
# Create your models here.
from django.db import connection


class Database():
    ## 오름차순 정렬로 데이터 베이스에서 가져오기
    def Select_Desc():
        cursor = connection.cursor()
        select_sql = 'SELECT * FROM REST ORDER BY ID DESC'
        cursor.execute(select_sql)
        data = cursor.fetchall()
        return data
    ## 내림차순 정렬로 데이터 베이스에서 가져오기
    def Select_Asc():
        cursor = connection.cursor()
        select_sql = 'SELECT * FROM REST ORDER BY ID ASC'
        cursor.execute(select_sql)
        data = cursor.fetchall()
        return data
    