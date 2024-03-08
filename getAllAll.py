# 上次收获38个xml到达最深递归，这次直接提高，看他会不会stackOverFlow
# 命令行以21634结束，共获219个文件
# 发现问题——只获得了最后一级的文件，尝试修改
# 修改ing

import sys  # 导入sys模块
sys.setrecursionlimit(5000)  # 将默认的递归深度修改为3000

import requests
from lxml import etree
import time

import os

# add git ignore

# realUrl = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=1671"

# this is init url
# realUrl = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"
# this is its childen
realUrl = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=2"

# this is an empry url
# url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=1686"




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

    path = ".\\xmlFiles\\"

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

    time.sleep(0.2)

    parentId = urlTurnId(url)
    childIdList = getChildId(url)

    # if childIdList == []:
    # 问题好像应该是这样
    if len(childIdList) == 1:
        saveXmls(idTurnUrl(parentId))
    
        parentParentId = getParentId(parentId)
        if ifFileExist(parentParentId) == False:
            saveXmls(idTurnUrl(parentParentId))
            print("saved parent")
        
        return
    else:
        for i in childIdList:
            getAll(idTurnUrl(i))

def ifFileExist(id):
    path = ".\\xmlFiles\\"
    realPath = path + str(id) + ".xml"

    print(realPath)

    return os.path.exists(realPath)

def getParentId(url):
    
    pId = []

    response  = requests.get(url)
    
    if response.status_code == 200:
        root = etree.fromstring(response.content)

        for i in range(len(root.xpath("//id"))):
            pId = root.xpath("//parentId")[i].text

    else:
        print("response!=200")
        return "response!=200"

    return pId


print(getParent(realUrl))

# getAll(realUrl)





















