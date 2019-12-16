from django.db import models
import cx_Oracle as oci
# Create your models here.
from django.db import connection
import random
from base64 import b64encode

class Database():
    ## 오름차순 정렬로 데이터 베이스에서 가져오기
    def __init__(self):
        self.cursor = connection.cursor()

    def Select_Desc(self):
        select_sql = 'SELECT * FROM REST ORDER BY DIST DESC'
        self.cursor.execute(select_sql)
        result_data = self.cursor.fetchall()
        return result_data
    ## 내림차순 정렬로 데이터 베이스에서 가져오기
    def Select_Asc(self):
        select_sql = 'SELECT * FROM REST ORDER BY DIST ASC'
        self.cursor.execute(select_sql)
        result_data = self.cursor.fetchall()
        return result_data
    def Word_Search(self,search_word,no,row):
        search_sql= f"SELECT * FROM REST WHERE NAME LIKE \'%{search_word}%\' ORDER BY DIST ASC"
        self.cursor.execute(search_sql)
        for i in range(no):
            result_data = self.cursor.fetchmany(row)
        return result_data

    def Select_Row(self,no,row):
        select_sql = 'SELECT * FROM REST ORDER BY DIST ASC'
        self.cursor.execute(select_sql)
        for i in range(no):
            result_data = self.cursor.fetchmany(row)
        return result_data
    def Search_Asc(self,search_word):
        search_sql= f"SELECT * FROM REST WHERE NAME LIKE \'%{search_word}%\' ORDER BY DIST ASC"
        self.cursor.execute(search_sql)
        result_data = self.cursor.fetchall()
        return result_data
class Func(Database):
    def __init__(self):
        pass
    def Randnum(self,data,n):
        sample_data = random.sample(data,n)
        return sample_data
    def Pagination(self,no,row,data,search_word):
        super().__init__()
        if len(super().Search_Asc(search_word))%row == 0:
            leng = len(super().Search_Asc(search_word))//row 
        else:
            leng = len(super().Search_Asc(search_word))//row + 1
        
        
        
        
        page = leng // 10 + 1
        page_1 = leng % 10
        
        for i in range(1,page+1):
            if ((10*(i-1))+1) <= no <= ((10*(i))+1):
                ran10 = range(    (10*(i-1))+1,   (10*(i))+ 1    )
        if  (((page-1)*10)+1) <= no <= leng+1:
            ran10 = range((((page-1)*10)+1),leng+1)
        return [ran10,leng]
    def Image_Data(self,data):
        image = []
        new_data = []
        

        for img in data:
            name = img[2]
            addr = img[1]
            cate = img[4]
            dist = img[8]
            idno = img[0]

            if img[9]:
                idata = img[9].read()  
                image = b64encode(idata).decode("utf-8")
            else :
                file = open("static/icon/sashimi.png","rb")
                idata = file.read()
                image = b64encode(idata).decode("utf-8")
            
            
            img2 = [name,addr,cate,dist,image,idno]
            
            
            new_data.append(img2)
        return new_data
        