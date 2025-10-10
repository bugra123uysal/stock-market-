import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

url="C:\\Users\\buğra\\Desktop\\abd_borsaa_mydata.xlsx"

analız=pd.read_excel(url)


print(analız.columns)

ana=analız['kazanç_raporu']
kap=analız['kapanış']
ac=analız['açılış'] 
vol=analız['Volatilite']
nam=analız['Hisse']
tahmin=analız['Fiyat_tahmini']
mar=analız['Market_değeri']
rakip=analız['rakipler']
deg=analız['değişim']


aa=analız['İndustry'].value_counts()
aa.plot(kind='bar')
plt.title("industry")
plt.grid(True)
plt.show()

sns.barplot(x=nam, y=mar, data=analız)
plt.title("şirketlerin market değerleri")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()




sns.barplot(x=analız['Hisse'] , y=analız['Volatilite'] , data=analız)
plt.title("volatilite")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

sns.barplot(x=analız['Hisse'] , y=analız['değişim'] , data=analız)
plt.grid(True)
plt.xticks(rotation=90)
plt.title("değişim")
plt.show()

ul=analız['Ülke'].value_counts()
ul.plot(kind='pie', autopct='%1.1f%%')
plt.title("ülkeler")
plt.grid(True)
plt.show()

bor=analız['para_birimi'].value_counts()
bor.plot(kind='pie', autopct="%1.1f%%")
plt.title("Para birimleri")
plt.grid(True)
plt.show()

pabi=analız['Borsa'].value_counts()
pabi.plot(kind='pie', autopct="%1.1f%%")
plt.title("Borsa")
plt.grid(True)
plt.show()

sns.lineplot(x=nam, y=ac, marker="o" ,color="black")
sns.lineplot(x=nam , y=kap ,marker="o", color="yellow" )
plt.title("kapanış-açılış fiyatları")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

sns.lineplot(x=nam , y=tahmin , marker='o', color='black')
sns.lineplot(x=nam , y=kap, marker='o', color='yellow')
plt.title("tahmini fiyatla kapanış fiyatı")
plt.grid(True)
plt.show()


  
kıyas=analız[['Hisse','açılış','kapanış']].melt(
    id_vars='Hisse' , var_name='Fiyat_tipi' ,value_name='fiyat_degeri'
)

sns.barplot(x='Hisse'  , y='fiyat_degeri'  ,hue='Fiyat_tipi', data=kıyas, palette=['black', 'yellow'] )

plt.grid(True)
plt.xticks(rotation=90)
plt.show()

kıyas_tahmin=analız[['Hisse', 'Fiyat_tahmini', 'kapanış']].melt(

    id_vars='Hisse' , var_name='Fiyat_tipi', value_name='fiyat_degeri'
)

sns.barplot(x='Hisse', y='fiyat_degeri', hue='Fiyat_tipi', data=kıyas_tahmin , palette=['black', 'yellow'])
plt.title("fiyat tahmileri")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

print("En yüksek market değeri:", analız.loc[analız['Market_değeri'].idxmax(), 'Hisse'])
print("En yüksek değişim değeri", analız.loc[analız['değişim'].idxmax(), 'değişim'])
print("En yüksek Volatilite değeri", analız.loc[analız['Volatilite'].idxmax(), 'Volatilite'])
print("En yüksek açılış_kapanış_fiyat_farkı değeri", analız.loc[analız['açılış_kapanış_fiyat_farkı'].idxmax(), 'açılış_kapanış_fiyat_farkı'])
print("En yüksek fiyat_aralığı_yüksek_düşük değeri", analız.loc[analız['fiyat_aralığı_yüksek_düşük'].idxmax(), 'fiyat_aralığı_yüksek_düşük'])
print("En yüksek Fiyat_tahmini değeri", analız.loc[analız['Fiyat_tahmini'].idxmax(), 'Fiyat_tahmini'])
print("En yüksek piyasa_defteri değeri", analız.loc[analız['piyasa_defteri'].idxmax(),'piyasa_defteri'  ])
print("En yüksek kazanç_raporu değeri", analız.loc[analız['kazanç_raporu'].idxmax(), 'kazanç_raporu' ])
