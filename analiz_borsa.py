import pandas as pd

url="C:\\Users\\buğra\\Desktop\\abd_borsaa_mydata.xlsx"

analız=pd.read_excel(url)


print(analız.columns)
print(analız.isnull().sum())
print(analız.info())
print(analız.dtypes)