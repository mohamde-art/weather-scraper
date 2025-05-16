import requests
from bs4 import BeautifulSoup
import csv

usl='https://www.accuweather.com/'
heardes={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
data=requests.get(usl,headers=heardes).text
soup=BeautifulSoup(data,'html.parser')
wather=soup.find('div',class_="nearby-locations content-module")
wathers=[]
city=soup.find_all('span',class_="text title no-wrap")
Temp=soup.find_all('span',class_="text temp")
for cit,tem in zip(city,Temp):
    wathers.append([
        cit.get_text(strip=True),
        tem.get_text(strip=True)
    ])

with open('wathers.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Tempicher'])  # كتابة رأس الأعمدة
    writer.writerows(wathers)  # كتابة كل صف في الملف دفعة واحدة

print("تم حفظ البيانات في ملف wathers.csv بنجاح.")        



