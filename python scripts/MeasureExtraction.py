# coding:utf-8
from bs4 import BeautifulSoup
#first： install： pip3 install bs4
content = open('/Users/hu/Desktop/abba-fernando.xml', 'rb').read()
soup = BeautifulSoup(content, 'xml')
mRestList = soup.find_all(attrs={"tstamp.ges": "0s"})
for mRest in mRestList:
    measure = mRest.parent.parent.parent
    print(measure)

