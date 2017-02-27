#!/usr/bin/python

import pandas, os, requests
from bs4 import BeautifulSoup

r=requests.get("http://www.century21.com/real-estate/gilroy-ca/LCCAGILROY/?k=1&o=price-asc")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"property-card-primary-info"})
# all[0].find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")

l=[]

for item in all:
    d={}
    d["Price"]=item.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")
    try:
        d["Beds"]=item.find_all("div",{"class":"property-beds"})[0].text.replace("\n","")
    except:
        d["Beds"]="No beds"
        pass
    try:
        d["Baths"]=item.find_all("div",{"class":"property-baths"})[0].text.replace("\n","")
    except:
        d["Baths"]="No Baths"
    try:
        d["Sqft"]=item.find_all("div",{"class":"property-sqft"})[0].text.replace("\n","")
    except:
        d["Sqft"]="No Sqft."
    l.append(d)

df=pandas.DataFrame(1)
df.to_csv("OutputHousing.csv")