SELECT * FROM abd_borsaa_sqll

SELECT Hisse , kapan�� FROM abd_borsaa_sqll ORDER BY kapan�� DESC
SELECT Hisse , kapan�� FROM abd_borsaa_sqll  ORDER  BY kapan�� ASC  

SELECT Hisse , Volatilite FROM abd_borsaa_sqll ORDER BY Volatilite ASC
SELECT Hisse , Volatilite FROM abd_borsaa_sqll ORDER BY Volatilite DESC

SELECT Hisse ,a��l��,kapan��  ,de�i�im, a��l��_kapan��_fiyat_fark� FROM abd_borsaa_sqll ORDER BY de�i�im ASC
SELECT Hisse ,a��l�� ,kapan�� ,de�i�im , a��l��_kapan��_fiyat_fark� FROM abd_borsaa_sqll ORDER BY de�i�im DESC

SELECT  Borsa  ,COUNT(Borsa) as borsa_adeti FROM abd_borsaa_sqll GROUP BY  Borsa ORDER BY borsa_adeti DESC;

SELECT  �lke, COUNT(�lke) AS �LKE_SAYIS FROM abd_borsaa_sqll GROUP BY �lke ORDER BY �LKE_SAYIS DESC

SELECT para_birimi , COUNT(para_birimi) as para_birimi_say�lar� FROM abd_borsaa_sqll GROUP BY  para_birimi  ORDER BY para_birimi_say�lar� DESC

SELECT industry  ,COUNT(industry) AS end�st�r�_adetleri FROM abd_borsaa_sqll GROUP BY industry ORDER BY end�st�r�_adetleri DESC