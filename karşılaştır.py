import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url="C:\\Users\\buğra\\Desktop\\abd_borsaa_mydata.xlsx"

karşılaştır=pd.read_excel(url)


print(karşılaştır.columns)

hisse=input("hisse: ").upper()
hissee=input("hisse: ").upper()


coll=["Hisse", "kapanış","açılış", "fiyat_aralığı_yüksek_düşük" ,"Fiyat_tahmini" ,"Volatilite" , "Market_değeri"]
krıatr=karşılaştır[karşılaştır["Hisse"].isin([hisse , hissee])]

print(krıatr[coll])
kap=krıatr['kapanış']
ac= krıatr['açılış']
vol=krıatr['Volatilite']
mar=krıatr['Market_değeri']
nam=krıatr['Hisse']
tahmin=krıatr['Fiyat_tahmini']
par=krıatr['para_birimi']
bor=krıatr['Borsa'] 
aralık=krıatr['fiyat_aralığı_yüksek_düşük']
tarih=krıatr['tarih']
ındus=krıatr['İndustry']
piyadef=krıatr['piyasa_defteri']
sns.barplot(x=krıatr['Hisse'], y=krıatr['kapanış'],color='black' , data=krıatr)
sns.barplot(x=krıatr['Hisse'] , y=krıatr['Fiyat_tahmini'] ,alpha=0.7 , color='yellow', data=krıatr)
plt.show()



sns.barplot(x=krıatr['Hisse'], y=krıatr['fiyat_aralığı_yüksek_düşük'], hue=par , data=krıatr)
plt.show()

 
sns.scatterplot(x=krıatr['Volatilite']  ,y=krıatr['Market_değeri'], hue=nam , data=krıatr)
plt.show()


sns.barplot(x=krıatr['Hisse'], y=krıatr['Market_değeri'], hue=ındus)
plt.show()

sns.barplot(x=krıatr['Hisse'], y=krıatr['piyasa_defteri'], hue=ındus)
plt.show()

sns.barplot(x=krıatr['Hisse'] , y=krıatr['Volatilite'] , hue=bor , data=krıatr)
plt.show()

cor=krıatr['Volatilite'].corr(krıatr['Market_değeri'])
print(cor)