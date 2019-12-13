import pandas as pd
from ./rest import models
# read csv file'
columns = ['이름','주소','분류','url1','tel','url2','LNG','LAT']
df = pd.read_csv('database1.csv') # df is pandas.DataFrame
df = df.drop_duplicates(['이름'])
print("##### data #####")

models.Func.randnum()