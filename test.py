import pandas as pd
# from . import models as m
import random
import csv
# read csv file'
# func = m.Func()
# columns = ['이름','주소','분류','url1','tel','url2','LNG','LAT']
# df = pd.read_csv('database1.csv') # df is pandas.DataFrame
# df = df.drop_duplicates(['이름'])
# print("##### data #####")
with open('database1.csv','r',encoding='utf-8') as f:
    wr = csv.reader(f)
    # data = [1,2,3,4,5,6,7,8,9]
    lists = []
    for i in wr:
        lists.append(i)
    print(random.sample(lists,5))
# print(func.randnum(data,5))