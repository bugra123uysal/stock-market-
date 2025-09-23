import pandas as pd
import requests
from datetime import datetime , timedelta
import matplotlib.pylab as plt
import seaborn as sns
bra=[]
api_key="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"
symbol=["AAPL","AMZN","TSM","AMD" ] 

   
   


for hısse in symbol:


   url=f"https://finnhub.io/api/v1/quote?symbol={hısse}&token={api_key}"
   #1 ay
   
  

   zaman_url=f"https://finnhub.io/api/v1/stock/profile2?symbol={hısse}&token={api_key}"
   url_zmn=requests.get(zaman_url).json()

    # haberler
   nee=f"https://finnhub.io/api/v1/company-news?symbol={hısse}&from=2025-01-01&to=2025-09-22&token={api_key}"
   newss=requests.get(nee).json()
     # kazanç raporu
   earn=f"https://finnhub.io/api/v1/stock/earnings?symbol={hısse}&token={api_key}"
   ear=requests.get(earn).json()
   # rakipler
   rakipler=f"https://finnhub.io/api/v1/stock/peers?symbol={hısse}&token={api_key}"
   rakip=requests.get(rakipler).json()




   
   al=requests.get(url)
   data=al.json()
   bra.append({
      "Hisse": {hısse},
      "kapanış": data["c"],
      "hight": data["h"],
      "low": data["l"],
      "açılış":data["o"],
      "tarih": pd.to_datetime(data["t"], unit="s"),
      "Ülke":url_zmn.get("country"),
      "para_birimi":url_zmn.get("currency"),
      "Borsa":url_zmn.get("exchange"),
      "İndustry":url_zmn.get("finnhubIndustry"),
      "İpo_tarih":url_zmn.get("ipo"),
      "Market değeri": url_zmn.get("marketCapitalization")   ,
      "piyasa defteri":url_zmn.get("shareOutstanding") ,
      "haberler":newss ,
      "kazanç_raporu": ear,
      "rakipler": rakip,
    
      

    })
  

brahs=pd.DataFrame(bra)

brahs.to_excel("C:\\Users\\buğra\\Desktop\\abd_borsaa_mydata.xlsx")




