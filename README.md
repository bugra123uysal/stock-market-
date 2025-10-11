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
## Analiz Google gemini ile 
Muhteşem 7'linin Analiz tarihi : 10.10.2025  20:00:00

Big 7 Hisseleri Piyasa ve Performans Analizi
Bu analiz, NVIDIA (NVDA), Microsoft (MSFT), Apple (AAPL), Google (GOOGL), Amazon (AMZN), Meta (META) ve Tesla (TSLA) hisselerinin belirli bir dönemdeki performansını ve risk profilini incelemektedir.

1. Sektörel Dağılım
Sektör	Şirket Adedi	Açıklama
Technology (Teknoloji)	2	MSFT, AAPL, (GOOGL/META genelde İletişim Hizmetleri olsa da teknoloji bazlı kabul edilir.)
Media (Medya)	2	META, GOOGL
Semiconductors (Yarı İletken)	1	NVDA
Retail (Perakende)	1	AMZN
Automobiles (Otomobil)	1	TSLA
Bulgu: Analiz edilen grup, beklendiği gibi Teknoloji ve Medya/İletişim Hizmetleri sektörlerinde yoğunlaşmaktadır. Bu, bu grubun küresel teknolojik trendlere ve reklam piyasasına karşı oldukça hassas olduğunu gösterir.

2. Piyasa Değeri Liderliği (Market Cap)
Grafik: şirketlerin market değerleri

Bulgu: Piyasa değeri sıralamasında zirvede açık ara NVDA yer almaktadır. Onu sırasıyla MSFT ve AAPL takip etmektedir.

Yorum: NVDA'nın diğer şirketlere kıyasla belirgin şekilde yüksek piyasa değeri, yapay zeka ve yarı iletken teknolojilerine olan yoğun yatırımcı güvenini ve sektördeki liderliğini vurgulamaktadır.

3. Günlük Değişim Analizi (Kısa Vadeli Performans)

Bulgu: Analiz edilen günde (veya kısa dönemde) tüm hisseler düşüş yaşamıştır (değişim değeri negatiftir).

En Çok Düşen: NVDA (Yaklaşık -5.3, açılış-kapanış fiyat farkı: -10345) ve TSLA (Yaklaşık -5.1) en sert düşüşü kaydetmiştir.

En Az Düşen: MSFT (Yaklaşık -1.7) nispeten en stabil performansı göstermiştir.

Yorum: NVDA'nın hem en değerli hisse olup hem de en çok düşen hisseler arasında yer alması, yüksek volatilitenin ve piyasadaki sert düzeltmelerin bu hisse üzerinde daha yıkıcı etkiler yaratabildiğini gösterir.

4. Oynaklık Analizi (Volatilite)
Grafik: volatilite

Bulgu:

En Oynak (Yüksek Risk/Getiri Potansiyeli): TSLA ve NVDA açık ara en yüksek volatiliteye sahiptir.

En Stabil (Düşük Risk): MSFT ve GOOGL en düşük volatiliteyi sergilemektedir.

Yorum: Yüksek volatilite, bir yandan yüksek risk taşırken, diğer yandan da kısa vadeli ticarette yüksek getiri potansiyeli sunar. TSLA ve NVDA, yatırımcılar için hem yüksek risk hem de yüksek ödül vaat eden hisselerdir. MSFT ise daha güvenli ve öngörülebilir bir performans sergilemektedir.

5. Fiyat Tahminleri 
Grafik: fiyat tahminleri

Bulgu: Bu grafikte, fiyat tahmini (siyah çubuk) ile gerçekleşen kapanış fiyatı (sarı çubuk) karşılaştırılmıştır.

Tahminin Başarısı: Çoğu hissede tahmin, gerçekleşen kapanış fiyatına çok yakındır.

En Yüksek Fiyat Hissesi: META (730 birim civarı) açılış ve kapanış fiyatları ile listedeki en yüksek fiyata sahiptir.

Yorum:  Meta hariç çoğu hisse için (kısa vadeli) tahminleri oldukça başarılıdır.

Veri Analisti Özeti
Bu analiz sonucunda, "Muhteşem Yedili" şirketlerinin büyük ölçüde teknoloji ağırlıklı olduğu ve NVDA ile TSLA'nın hem piyasa liderleri hem de en oynak hisseler olduğu görülmüştür. Düşüş yaşanan bir günde dahi, MSFT nispeten daha az kayıpla en istikrarlı performansı sergileyerek, portföyde bir denge unsuru olarak öne çıkmaktadır.

Bu bulgular, yatırım stratejilerinin riske tahammül düzeyine göre şekillendirilmesi gerektiğini göstermektedir:

Düşük Risk İştahı: MSFT ve GOOGL'a odaklanılmalıdır.

Yüksek Risk İştahı: NVDA ve TSLA'nın yüksek volatilite potansiyelinden yararlanılabilir.

