import tweepy
import requests
from bs4 import BeautifulSoup
import random
import time
from openpyxl import load_workbook

api_key =""
api_secret =""
bearer_token =r""
access_token = ""
access_token_secret=""

client = tweepy.Client(bearer_token,api_key,api_secret,access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token, access_token_secret)
api = tweepy.API(auth)


trendlist1=[]
trendlist2=[]
trendlist3=[]
trendlist4=[]
trendlist5=[]
trendlist6=[]
trendlist7=[]

def trends():
  url1="https://codepedia.info/twitter-trends"
  url2 ="https://codepedia.info/twitter-trends/united-states"
  url3 ="https://codepedia.info/twitter-trends/united-kingdom"
  url4 ="https://codepedia.info/twitter-trends/france"
  url5 ="https://codepedia.info/twitter-trends/canada"
  url6 ="https://codepedia.info/twitter-trends/germany"
  url7= "https://codepedia.info/twitter-trends/australia"

  response1 = requests.get(url1)
  response2 = requests.get(url2)
  response3 = requests.get(url3)
  response4 = requests.get(url4)
  response5 = requests.get(url5)
  response6 = requests.get(url6)
  response7 = requests.get(url7)

  html_icerigi1= response1.content
  html_icerigi2= response2.content
  html_icerigi3= response3.content
  html_icerigi4= response4.content
  html_icerigi5= response5.content
  html_icerigi6= response6.content
  html_icerigi7= response7.content
  soup1 = BeautifulSoup(html_icerigi1,"html.parser")
  soup2 = BeautifulSoup(html_icerigi2,"html.parser")
  soup3 = BeautifulSoup(html_icerigi3,"html.parser")
  soup4 = BeautifulSoup(html_icerigi4,"html.parser")
  soup5 = BeautifulSoup(html_icerigi5,"html.parser")
  soup6 = BeautifulSoup(html_icerigi6,"html.parser")
  soup7 = BeautifulSoup(html_icerigi7,"html.parser")

  
  for t1 in soup1.find_all("a",{"class": "aLnk"}):
    trendlist1.append(t1.text)
    if len(trendlist1)==10:
      break



  for t2 in soup2.find_all("a",{"class": "aLnk"}):
    trendlist2.append(t2.text)
    if len(trendlist2)==10:
      break

  for t3 in soup3.find_all("a",{"class": "aLnk"}):
    trendlist3.append(t3.text)
    if len(trendlist3)==10:
      break

  for t4 in soup4.find_all("a",{"class": "aLnk"}):
    trendlist4.append(t4.text)
    if len(trendlist4)==10:
      break

  for t5 in soup5.find_all("a",{"class": "aLnk"}):
    trendlist5.append(t5.text)
    if len(trendlist5)==10:
      break

  for t6 in soup6.find_all("a",{"class": "aLnk"}):
    trendlist6.append(t6.text)
    if len(trendlist6)==10:
      break

  for t7 in soup7.find_all("a",{"class": "aLnk"}):
    trendlist7.append(t7.text)
    if len(trendlist7)==10:
      break





def iterating_column(path,sheet_name,col):
    workbook = load_workbook(filename =path)
    sheet = workbook[sheet_name]
    global tweetsend
    tweetsend= []
    for cell in sheet[col]:
        tweetsend.append(f"{cell.value}")
    

     
def starts():
    iterating_column("dene.xlsx",sheet_name="Sayfa1",col="A")
    trends()

    alltrend = trendlist1+trendlist2+trendlist3+trendlist4+trendlist5+trendlist6+trendlist7
    x =1
    while (x<750):
     client.create_tweet(text =tweetsend[x]+random.choice(alltrend)+random.choice(alltrend)+random.choice(alltrend)+str(random.randint(1, 10000)))
     print("{} tweet sent...".format(x))
     time.sleep(125)
     x+=1

starts()


