import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


url="C:\\Users\\buğra\\Desktop\\abd_borsaa_mydata.xlsx"

analız=pd.read_excel(url)






"""  
aa=analız['İndustry'].value_counts()
aa.plot(kind='bar')
plt.title("industry")
plt.show()

hıs=analız['Hisse']
kap=analız['kapanış']

sns.lineplot(x=hıs , y=kap ,marker="o" )
plt.title("kapanış fiyatları")
plt.show()

mar=analız['Market_değeri']
sns.lineplot(x=hıs, y=mar, marker="o")
plt.title("şirketlerin market değerleri")
plt.show()

ana=analız['kazanç_raporu']
analız['hight']
kap=analız['kapanış']
ac=analız['açılış']

sns.lineplot(x=kap, y=ac,marker="o" , color="blue")
sns.lineplot(x=kap, y=ac, marker="o" ,color="black")
plt.title("Endüştürü")
plt.show()

rak=analız['rakipler'].value_counts()
rak.plot(kind='bar')
plt.title("rakiplerin adeti")
plt.show()
"""
ul=analız['Ülke'].value_counts()
ul.plot(kind='pie')
plt.title("ülkeler")
plt.show()

bor=analız['para_birimi'].value_counts()
bor.plot(kind='pie')
plt.title("aa")
plt.show()

pabi=analız['Borsa'].value_counts()
pabi.plot(kind='pie')
plt.show()