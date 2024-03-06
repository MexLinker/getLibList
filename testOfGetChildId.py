import requests
from lxml import etree


# url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=1671"

# this is empty
url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=1686"


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

    fileName = ""

    response  = requests.get(url)
    
    if response.status_code == 200:
    
        

        root = etree.fromstring(response.content)

        for i in range(len(root.xpath("//id"))):
            print(root.xpath("//parentId")[i].text)

            # ???
            # if root.xpath("//parentId")[i].text == "" :
            #     print("This is A Noe Xml, you should not save it")
            #     return "This is A Noe Xml, you should not save it"

            fileName = root.xpath("//parentId")[i].text + ".xml"
        

        # filename = input( "请输入保存文件的名称：")

        # with open(filename, "wb") as file:
        # file.write(content)
        
    else:
        print("response!=200")
        return "response!=200"
    
    print(fileName)

    return 
    


# idList = getChildId(url)

# print(idList)

saveXmls(url)

















