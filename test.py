import cx_Oracle as oci
import base64
from base64 import b64encode
import os

dirname=os.path.dirname(__file__)
savename = dirname+'/test.jpg'


conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

cursor = conn.cursor()
id_sql = "SELECT IMAGE FROM REST WHERE NAME LIKE '%'|| :text ||'%'"
cursor.execute(id_sql,text='뚜레쥬르')
img = cursor.fetchone()
if img[0]:
    data1 = img[0].read()
    # img = b64encode(data1).decode("utf-8")
else:
    file =  open("./static/img/default.jpg", "rb")
    data1 = file.read()
    # img = b64encode(data1).decode("utf-8")
with open(savename,mode='wb') as f:
    f.write(data1)
    print('저장되었습니다.')
# print(img)