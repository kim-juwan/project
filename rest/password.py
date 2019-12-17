import bcrypt
from django.db import connection
from django.db import models
import cx_Oracle as oci

password = 'rest'
password2 = 'rest'
salt = bcrypt.gensalt()
hashs = bcrypt.hashpw(bytes(password,encoding='utf-8'), salt)


if bcrypt.checkpw(bytes(password2, encoding='utf-8'),hashs):
    print('match')
else:
    print('fail')
data = [1,hashs]
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
insert_sql = 'INSERT INTO EP VALUES (:1,:2)'
cursor = conn.cursor()
cursor.execute(insert_sql,data)
conn.commit()