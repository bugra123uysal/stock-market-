   # stock-market
Finhub API kullanarak ABD borsasındaki şirketlerin açılış–kapanış fiyatı, piyasa değeri, volatilite vb. verilerini toplayıp, Python ve SQL ile analiz ve görselleştirme yapan bir finans veri analizi projesi.

   ## Libraries
import pandas as pd
import requests
from datetime import datetime , timedelta
import matplotlib.pylab as plt
import seaborn as sns

   ## Columns
   'Hisse', 'kapanış', 'hight', 'low', 'açılış', 'değişim',
       'Volatilite', 'açılış_kapanış_fiyat_farkı',
       'fiyat_aralığı_yüksek_düşük', 'Fiyat_tahmini', 'tarih', 'Ülke',
       'para_birimi', 'Borsa', 'İndustry', 'İpo_tarih', 'Market_değeri',
       'piyasa_defteri', 'haberler', 'kazanç_raporu', 'rakipler'

   ## Symbols 
   NVDA, MSFT, AAPL, GOOGL, AMZN, META, TSLA

   # Grafikler ve tablolar
<img width="1712" height="884" alt="Ekran görüntüsü 2025-10-11 012107" src="https://github.com/user-attachments/assets/eb2786e3-be71-4f68-afce-1775c61cef3b" />
<img width="1757" height="891" alt="Ekran görüntüsü 2025-10-11 012053" src="https://github.com/user-attachments/assets/ba81add9-7515-4aa8-8ce3-4a9534599c30" />
<img width="1734" height="915" alt="Ekran görüntüsü 2025-10-11 023118" src="https://github.com/user-attachments/assets/b8a30571-cd92-4fca-998f-fde254e04a9e" />
<img width="1630" height="934" alt="Ekran görüntüsü 2025-10-11 011954" src="https://github.com/user-attachments/assets/994dfb56-1a8c-46fa-8935-dc820be2044a" />
<img width="1690" height="939" alt="Ekran görüntüsü 2025-10-11 011941" src="https://github.com/user-attachments/assets/af329321-fb12-43b3-aa55-a6859d44ed7b" />
<img width="1617" height="940" alt="Ekran görüntüsü 2025-10-11 011925" src="https://github.com/user-attachments/assets/061a68c8-6aa3-4160-bc7c-70c4ee8df882" />
<img width="264" height="121" alt="Ekran görüntüsü 2025-10-11 005314" src="https://github.com/user-attachments/assets/7c6e228e-ff3a-4ec0-b224-fc0ed4d2bb48" />
<img width="483" height="162" alt="Ekran görüntüsü 2025-10-11 005229" src="https://github.com/user-attachments/assets/136cd24a-7854-46c4-a91d-5ef61b03924f" />
<img width="209" height="163" alt="Ekran görüntüsü 2025-10-11 004202" src="https://github.com/user-attachments/assets/e2d4a475-4c9f-4dc4-829b-516384591003" />
<img width="154" height="159" alt="Ekran görüntüsü 2025-10-11 004005" src="https://github.com/user-attachments/assets/8b6c13ec-faea-4d2b-b8bd-078ccaabbc7e" />
