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
    def Search_Ascword(self,search_word):
        search_sql= f"SELECT * FROM REST WHERE NAME LIKE \'%{search_word}%\' ORDER BY DIST ASC"
        self.cursor.execute(search_sql)
        result_data = self.cursor.fetchall()
        return result_data
    def Search_Asccate(self,cate):
        search_sql = f"SELECT * FROM (SELECT * FROM REST WHERE CATE LIKE \'{cate[0]}\' OR CATE LIKE \'{cate[1]}\' OR CATE LIKE \'{cate[2]}\' OR CATE LIKE \'{cate[3]}\' OR CATE LIKE \'{cate[4]}\' OR CATE LIKE \'{cate[5]}\' OR CATE LIKE \'{cate[6]}\' OR CATE LIKE \'{cate[7]}\' OR CATE LIKE \'{cate[8]}\' OR CATE LIKE \'{cate[9]}\' OR CATE LIKE \'{cate[10]}\' OR CATE LIKE \'{cate[11]}\' OR CATE LIKE \'{cate[12]}\' OR CATE LIKE \'{cate[13]}\' OR CATE LIKE \'{cate[14]}\') WHERE (DIST < {cate[15]}) ORDER BY DIST ASC"
        # search_sql = f"SELECT * FROM (SELECT * FROM REST WHERE CATE LIKE \'%{cate[0]}%\' OR CATE LIKE \'%{cate[1]}%\' OR CATE LIKE \'%{cate[2]}%\' OR CATE LIKE \'%{cate[3]}%\' OR CATE LIKE \'%{cate[4]}%\' OR CATE LIKE \'%{cate[5]}%\' OR CATE LIKE \'%{cate[6]}%\' OR CATE LIKE \'%{cate[7]}%\' OR CATE LIKE \'%{cate[8]}%\' OR CATE LIKE \'%{cate[9]}%\' OR CATE LIKE \'%{cate[10]}%\' OR CATE LIKE \'%{cate[11]}%\' OR CATE LIKE \'%{cate[12]}%\' OR CATE LIKE \'%{cate[13]}%\' OR CATE LIKE \'%{cate[14]}%\') WHERE (DIST < {cate[15]}) ORDER BY DIST ASC"
        self.cursor.execute(search_sql)
        result_data = self.cursor.fetchall()
        return result_data
    def Select_One(self,idno):
        select_sql = f'SELECT * FROM REST WHERE ID={idno}'
        self.cursor.execute(select_sql)
        result_data = self.cursor.fetchone()
        return result_data
    def Cate_Search(self,no,row,cate):
        search_sql = f"SELECT * FROM (SELECT * FROM REST WHERE CATE LIKE \'{cate[0]}\' OR CATE LIKE \'{cate[1]}\' OR CATE LIKE \'{cate[2]}\' OR CATE LIKE \'{cate[3]}\' OR CATE LIKE \'{cate[4]}\' OR CATE LIKE \'{cate[5]}\' OR CATE LIKE \'{cate[6]}\' OR CATE LIKE \'{cate[7]}\' OR CATE LIKE \'{cate[8]}\' OR CATE LIKE \'{cate[9]}\' OR CATE LIKE \'{cate[10]}\' OR CATE LIKE \'{cate[11]}\' OR CATE LIKE \'{cate[12]}\' OR CATE LIKE \'{cate[13]}\' OR CATE LIKE \'{cate[14]}\') WHERE (DIST < {cate[15]}) ORDER BY DIST ASC"
        # search_sql = f"SELECT * FROM (SELECT * FROM REST WHERE CATE LIKE \'%{cate[0]}%\' OR CATE LIKE \'%{cate[1]}%\' OR CATE LIKE \'%{cate[2]}%\' OR CATE LIKE \'%{cate[3]}%\' OR CATE LIKE \'%{cate[4]}%\' OR CATE LIKE \'%{cate[5]}%\' OR CATE LIKE \'%{cate[6]}%\' OR CATE LIKE \'%{cate[7]}%\' OR CATE LIKE \'%{cate[8]}%\' OR CATE LIKE \'%{cate[9]}%\' OR CATE LIKE \'%{cate[10]}%\' OR CATE LIKE \'%{cate[11]}%\' OR CATE LIKE \'%{cate[12]}%\' OR CATE LIKE \'%{cate[13]}%\' OR CATE LIKE \'%{cate[14]}%\') WHERE (DIST < {cate[15]}) ORDER BY DIST ASC"
        # search_sql = f"SELECT * FROM (SELECT * FROM REST WHERE CATE LIKE (\'%{cate[0]}%\' OR \'%{cate[1]}%\' OR \'%{cate[2]}%\' OR \'%{cate[3]}%\' OR \'%{cate[4]}%\' OR \'%{cate[5]}%\' OR \'%{cate[6]}%\' OR \'%{cate[7]}%\' OR \'%{cate[8]}%\' OR \'%{cate[9]}%\' OR \'%{cate[10]}%\' OR \'%{cate[11]}%\' OR \'%{cate[12]}%\' OR \'%{cate[13]}%\' OR \'%{cate[14]}%\')) WHERE (DIST < {cate[15]}) "
        self.cursor.execute(search_sql)
        for i in range(no):
            result_data = self.cursor.fetchmany(row)
        return result_data
    
class Func(Database):
    def __init__(self):
        pass
    def Randnum(self,data,n):
        sample_data = random.sample(data,n)
        return sample_data
    def Pagination_word(self,no,row,data,search_word):
        super().__init__()
        if len(super().Search_Ascword(search_word))%row == 0:
            leng = len(super().Search_Ascword(search_word))//row 
        else:
            leng = len(super().Search_Ascword(search_word))//row + 1
        
        
        
        
        page = leng // 10 + 1
        
        
        for i in range(1,page+1):
            if ((10*(i-1))+1) <= no <= ((10*(i))+1):
                ran10 = range(    (10*(i-1))+1,   (10*(i))+ 1    )
        if  (((page-1)*10)+1) <= no <= leng+1:
            ran10 = range((((page-1)*10)+1),leng+1)
        return [ran10,leng]
    def Image_Data(self,data):
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
    def Image_Encoder(self,data):
        if data[9]:
            idata = data[9].read()  
            image = b64encode(idata).decode("utf-8")
        else :
            file = open("static/icon/sashimi.png","rb")
            idata = file.read()
            image = b64encode(idata).decode("utf-8")
        return image
    def Pagination_cate(self,no,row,data,cate):
        super().__init__()
        if len(super().Search_Asccate(cate))%row == 0:
            leng = len(super().Search_Asccate(cate))//row 
        else:
            leng = len(super().Search_Asccate(cate))//row + 1
        
        
        
        
        page = leng // 10 + 1
        
        
        for i in range(1,page+1):
            if ((10*(i-1))+1) <= no <= ((10*(i))+1):
                ran10 = range(    (10*(i-1))+1,   (10*(i))+ 1    )
        if  (((page-1)*10)+1) <= no <= leng+1:
            ran10 = range((((page-1)*10)+1),leng+1)
        return [ran10,leng]
    def Menu_Encoder(self,data):
        if data[10] is not None:
            menu = data[10].read().split('|')
        else :
            menu = ['등록된 메뉴 정보가 없습니다.']
        return menu