from bs4 import BeautifulSoup
import html5lib
import requests
url="https://www.google.com"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
alllinks=set() 
anchor=soup.find_all('a')
for link in anchor:
    if(link!="#"):
        alllinks.add( "https://www.google.com"+link.get('href'))
for i in alllinks:
    print(i+"\n")