from bs4 import BeautifulSoup as bs
import requests
link=("https://www.flipkart.com/canon-eos-m50-mark-ii-vlogger-kit-mirrorless-camera-ef-m-15-45mm-lens/p/itm1398d193d0005?pid=DLLG4NTMTDF4BETY&lid=LSTDLLG4NTMTDF4BETYH94GVG&marketplace=FLIPKART&q=canon&store=search.flipkart.com&srno=s_1_11&otracker=search&otracker1=search&fm=organic&iid=c8f9a688-1588-4c25-a8be-ce959f729837.DLLG4NTMTDF4BETY.SEARCH&ppt=hp&ppn=homepage&ssid=m2522i53000000001667548782456&qH=6638070bc99321b3")
page=requests.get(link)
page.content
soup=bs(page.content,"html.parser")
soup
print(soup.prettify())
list(soup.children)
title=soup.title
title
print(title.string)
price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
print(price)
product_price=[]
for i in range(0,len(price)):
    product_price.append(price[i].get_text())
product_price
names=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
names
cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name
comment=soup.find_all("p",class_="_2-N8zT")
comment
cust_comment=[]
for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())
cust_comment
star=soup.find_all("div",class_="_3LWZlK _1BLPMq")
star
cust_stars=[]
for i in range(0,len(star)):
    cust_stars.append(star[i].get_text())
cust_stars
review=soup.find_all("div",class_="t-ZTKy")
review
cust_review=[]
for i in range(0,len(review)):
    cust_review.append(review[i].get_text())
cust_review
rating=soup.find_all("div",class_="_1uJVNT")
rating
cust_rating=[]
for i in range(0,len(rating)):
    cust_rating.append(rating[i].get_text())
cust_rating
rstar=soup.find_all("span",class_="_26f_zl")
rstar
cust_rstar=[]
for i in range(0,len(rstar)):
    cust_rstar.append(rstar[i].get_text())
cust_rstar
likndis=soup.find_all("span",class_="_3c3Px5")
likndis
cust_likndis=[]
for i in range(0,len(likndis)):
    cust_likndis.append(likndis[i].get_text())
cust_likndis
dateofbuyingprod=soup.find_all("p",class_="_2sc7ZR")
dateofbuyingprod
cust_dateofbuyingprod=[]
for i in range(0,len(dateofbuyingprod)):
    cust_dateofbuyingprod.append(dateofbuyingprod[i].get_text())
cust_dateofbuyingprod
import pandas as pd
df=pd.DataFrame()
df["Customer_Names"]=cust_name
df["Comments"]=cust_comment
df["Stars"]=cust_stars
df["Review"]=cust_review
df
df.to_csv("CANON PRODUCT FIRST TEN REVIEW",index=False)
df1=pd.read_csv("CANON PRODUCT FIRST TEN REVIEW")
df1
