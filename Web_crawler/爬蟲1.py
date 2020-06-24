#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import requests
from bs4 import BeautifulSoup
# import json

driver=webdriver.Chrome()
driver.get('https://www.google.com.tw/')
time.sleep(3)
driver.find_element_by_name("q").send_keys("高鐵\n")
time.sleep(2)
driver.find_element_by_css_selector('.DKV0Md').click()

selected_start=driver.find_element_by_id("StartStation")#出發站
start=Select(selected_start)
start.select_by_visible_text('板橋站')#輸入出發站
time.sleep(3)

selected_end=driver.find_element_by_id("EndStation")#到達站
start=Select(selected_end)
start.select_by_visible_text('左營站')#輸入到達站
time.sleep(3)

driver.find_element_by_id("DepartueSearchDate").click()
time.sleep(2)
driver.find_element_by_link_text("26").click()#輸入當月日期

selected_time=driver.find_element_by_id("DepartueSearchTime")
clock=Select(selected_time)
clock.select_by_visible_text('20:00')#輸入當天想搭乘時間
time.sleep(3)

driver.find_element_by_id("btnQuickSearchSubmit").click()#查詢鍵

index=driver.page_source
soup=BeautifulSoup(index,"html.parser")
articles=soup.select('.go_trip tbody .trip_no')
articles1=soup.select('.go_trip tbody .row_DepartureTime')
articles2=soup.select('.go_trip tbody .row_DestinationTime')
articles3=soup.select('.go_trip tbody td')
articles4=soup.select('.go_trip tbody .trip_label')

a0=[]
v=[]
for i in range(len(articles)):
    a0.append(str(articles[i]))
for j in range(len(a0)):
    b0=a0[j]
    b00=b0.replace('<td class="trip_no">','').replace('       </td>','')
    v.append(b00)
# print(v)

a1=[]
w=[]
for i in range(len(articles)):
    a1.append(str(articles1[i]))
for j in range(len(a1)):
    b1=a1[j]
    b11=b1.replace('<td class="row_DepartureTime">','').replace('       </td>','')
    w.append(b11)
# print(w)

a2=[]
x=[]
for i in range(len(articles)):
    a2.append(str(articles2[i]))
for j in range(len(a2)):
    b2=a2[j]
    b22=b2.replace('<td class="row_DestinationTime">','').replace('       </td>','')
    x.append(b22)
# print(x)

a3=[]
c=[]
y0=[]
y=[]
for i in range(len(articles3)):
    a3.append(str(articles3[i]))
for j in range(len(a3)):
    b3=a3[j]
    b33=b3.split('</td>')
    c.append(b33)
for k in range(len(c)):
    if k%8==3:
        y0.append(c[k])
for i in range(len(y0)):
    yy=str(y0[i])
    y2=yy.replace("['<td>","").replace("       ', '']","")
    y.append(y2)
# print(y)

a4=[]
z=[]
for i in range(len(articles)):
    a4.append(str(articles4[i]))
for j in range(len(a4)):
    b4=a4[j]
    b44=b4.replace('<label class="trip_label" style="background: #f00d67;">','').replace('</label>','').replace('<label class="trip_label">','')
    z.append(b44)
# print(z)

print("車次",'\t',"出發時間",'\t',"抵達時間",'\t',"行車時間",'\t',"早鳥優惠")
for i in range(len(v)):
    print(v[i],'\t',w[i],'\t','\t',x[i],'\t','\t',y[i],'\t','\t',z[i])
    
print('Done')

