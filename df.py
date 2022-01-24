from bs4 import BeautifulSoup
import requests


r = requests.get("https://www.defenseworld.net/")

html_content = r.content

soup = BeautifulSoup(html_content,"html.parser")
a  = soup.find("div",class_='col-sm-16 col-xs-16')
link = a.find('a')
href = link.get('href')
r2 = requests.get('https://www.defenseworld.net/'+str(href))
html_content2 = r2.content
soup2 =BeautifulSoup(html_content2,"html.parser")
title = soup2.find('div',class_="col-md-12 col-sm-16 col-xs-16")
title2 = title.find_all('h4',class_="mt-0")
for l in title2:
    l2 = l.find('a')
    link3 = l2.get('href')
    # print('https://www.defenseworld.net/'+str(link3))
    r3 = requests.get('https://www.defenseworld.net/'+str(link3))
    html_content3 = r3.content
    # print(html_content3)
    soup3 = BeautifulSoup(html_content3,'html.parser')
    # print(soup3)
    titles = soup3.find('h1',class_='mt-0')
    print(titles.text)
    date = soup3.find('ul',class_='news-meta')
    print(date.text)
    con = soup3.find('div',class_='media-content mt-20 mb-20')
    print(con.text)
    # p = con.find_all('p')
    # for pc in p:
    #     print(pc.get_text())
    # time = date.find('li')
    # print(time)
    # da  = time.find('span',class_='ion-android-data icon')
    # print(da.text)
    # for ti in titles:
    #     print(ti)


