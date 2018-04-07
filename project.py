#!C:\Python27\python.exe
print ("Content-Type: text/html\n")

from selenium import webdriver
from collections import Counter
from selenium.webdriver.common.keys import Keys
import emoji
import urllib3.request as ul
import time
import sys

username = open("post.txt","r").read()
driver=webdriver.Chrome("/chromedriver.exe")
driver.get("https://www.instagram.com/"+username+"/")                                        #Replacement
p='//*[@id="react-root"]/section/main'

while True:
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)                                                                                   #Scrolling time
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height==last_height:
        break


driver.implicitly_wait(100)

eee=driver.find_elements_by_xpath(p)
zzz=[ee.get_attribute('outerHTML') for ee in eee]

zzz=str(zzz)
zzz=emoji.emojize(zzz)

dsav=open("/rwdata.txt",'w')                                                    #Location of Raw data
dsav.write(zzz)
dsav.close()
wc=list()
wc1=list()
location='D:/mon'
z=zzz.split("src=")
zzz1=zzz.split('img alt="')
#print zzz1
count=0
for iyy in zzz1:
    if count>0:
        xc=iyy.split("class")[0]
        fdd=str(xc).split('id="')
        fdd1=str(fdd)
        fdd1=fdd1.replace("\\n."," ",1000)
        fdd1=fdd1.replace("\\n"," ",1000)
        fdd1=fdd1.replace("\\"," ",1000)
        fdd1=fdd1.replace("#"," ",1000)
        fdd1=fdd1.replace("['","",1000)
        fdd1=fdd1.replace("']"," ",1000)
        fdd1=" ".join(fdd1.split())
        fdd2=fdd1.split(" ")
        for tttt in fdd2:
            #print tttt
            wc.append(tttt)
        
    count=count+1


print("Photo count: ")
print(count)
print("<br> Word Count: ")
print(len(wc))
print("<br>") 
for wwww in wc:
   print (wwww)
   print("<br>")

print(Counter(wc))
print("<br>")

driver.quit()
