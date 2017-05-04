#!/bin/python3
# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url) :
    try :
        html = urlopen(url)
    except HTTPError as e :
        return None
    try :
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
        #title = bsObj.h1
    except AttributeError as e :
        return None
    return title
title1 = getTitle("http://www.pythonscraping.com/pages/page1.html")
title2 = getTitle("http://www2015.tyut.edu.cn/cn/index.html")
for t in title1,title2 :
    if t == None :
        print("Title could not be found")
    else :
        print(t)
