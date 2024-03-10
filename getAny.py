# getAny.py can get any library's list by change the path

import sys  # 导入sys模块
sys.setrecursionlimit(5000)  # 将默认的递归深度修改为3000

import requests
from lxml import etree
import time

import os

# for 武汉城市圈图书馆 using xmlFiles_WH
global path 
path = ".\\xmlFiles_WH\\"

# realUrl = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"
realUrl = "http://interlib.library.hb.cn:8008/opac/browse/query?category=cls&id=0"
# 发现开始的initUrl只有域名与端口换了，剩下的一样







def getChildId(url):
    
    idList = []

    response  = requests.get(url)
    
    if response.status_code == 200:
        root = etree.fromstring(response.content)

        for i in range(len(root.xpath("//id"))):
            print(root.xpath("//id")[i].text)
            idList.append(root.xpath("//id")[i].text)

    else:
        print("response!=200")
        return "response!=200"

    return idList

def saveXmls(url):

    # path = ".\\xmlFiles\\"

    index = url.find("id=")
    fileNameWihtOutpPostfix = url[index + len("id="):]

    response  = requests.get(url)
    
    if response.status_code == 200:

        content = response.content

        realPath = path + fileNameWihtOutpPostfix + ".xml"

        with open(realPath, "wb") as file:
            file.write(content)
            print("writed " +realPath+ " success")
        
    else:
        print("response!=200")
        return "response!=200"
    
    return 
    
def idTurnUrl(id):
    return "http://1.82.133.119:8082/opac/browse/query?category=cls&id=" + str(id)

def urlTurnId(url):
    index = url.find("id=")
    fileNameWihtOutpPostfix = url[index + len("id="):]
    return fileNameWihtOutpPostfix

def getAll(url):

    # time.sleep(4)

    parentId = urlTurnId(url)
    childIdList = getChildId(url)

    parentParentId = getParentId(idTurnUrl(parentId))
    if ifFileExist(parentParentId) == False and parentParentId != 999999999:
        saveXmls(idTurnUrl(parentParentId))
        print("saved parentparent")

    # if childIdList == []:
    # 问题好像应该是这样
    if len(childIdList) == 1:
        if ifFileExist(parentId) == False and parentId != 999999999:
            print("saved parent")
            saveXmls(idTurnUrl(parentId))
   
        return
    else:
        for i in childIdList:
            getAll(idTurnUrl(i))

def ifFileExist(id):
    # path = ".\\xmlFiles\\"
    realPath = path + str(id) + ".xml"

    print(realPath)

    return os.path.exists(realPath)

def getParentId(url):
    
    # pId = []

    response  = requests.get(url)
    
    # just for differ
    pId = 999999999
    
    if response.status_code == 200:
        root = etree.fromstring(response.content)

        for i in range(len(root.xpath("//id"))):
            pId = root.xpath("//parentId")[i].text

    else:
        print("response!=200")
        return "response!=200"

    return pId




getAll(realUrl)






















