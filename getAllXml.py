import requests
from lxml import etree


# url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=1671"

# this is init url
# url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"

# this is an empry url
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

    path = ".\\xmlFiles\\"

    index = url.find("id=")
    fileNameWihtOutpPostfix = url[index + len("id="):]

    response  = requests.get(url)
    
    if response.status_code == 200:

        content = response.content

        realPath = path + fileNameWihtOutpPostfix + ".xml"

        with open(realPath, "wb") as file:
            file.write(content)
            print("writed success")
        
    else:
        print("response!=200")
        return "response!=200"
    
    return 
    
# idList = getChildId(url)
#     currnetUrl
#     saveXmls(currnetUrl)

idList = getChildId(url)
if idList == []:
    print("this is em")

if getChildId(url) != []:
    for i in getChildId(url):
        idList.append(i)

if getChildId(url) != []:
    for i in getChildId(url):
        idList.append(i)
        callSlef()
else:
    

















