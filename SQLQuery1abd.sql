SELECT * FROM abd_borsaa_sqll

SELECT Hisse , kapanýþ FROM abd_borsaa_sqll ORDER BY kapanýþ DESC
SELECT Hisse , kapanýþ FROM abd_borsaa_sqll  ORDER  BY kapanýþ ASC  

SELECT Hisse , Volatilite FROM abd_borsaa_sqll ORDER BY Volatilite ASC
SELECT Hisse , Volatilite FROM abd_borsaa_sqll ORDER BY Volatilite DESC

SELECT Hisse ,açýlýþ,kapanýþ  ,deðiþim, açýlýþ_kapanýþ_fiyat_farký FROM abd_borsaa_sqll ORDER BY deðiþim ASC
SELECT Hisse ,açýlýþ ,kapanýþ ,deðiþim , açýlýþ_kapanýþ_fiyat_farký FROM abd_borsaa_sqll ORDER BY deðiþim DESC

SELECT  Borsa  ,COUNT(Borsa) as borsa_adeti FROM abd_borsaa_sqll GROUP BY  Borsa ORDER BY borsa_adeti DESC;

SELECT  Ülke, COUNT(Ülke) AS ÜLKE_SAYIS FROM abd_borsaa_sqll GROUP BY Ülke ORDER BY ÜLKE_SAYIS DESC

SELECT para_birimi , COUNT(para_birimi) as para_birimi_sayýlarý FROM abd_borsaa_sqll GROUP BY  para_birimi  ORDER BY para_birimi_sayýlarý DESC

SELECT industry  ,COUNT(industry) AS endüstürü_adetleri FROM abd_borsaa_sqll GROUP BY industry ORDER BY endüstürü_adetleri DESC