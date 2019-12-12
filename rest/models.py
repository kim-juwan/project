from django.db import models
import cx_Oracle as oci
# Create your models here.
from django.db import connection


class database():
    def select():
        cursor = connection.cursor()
        select_sql = 'SELECT * FROM REST ORDER BY ID DESC'
        cursor.execute(select_sql)
        data = cursor.fetchall()
        return data