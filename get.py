import requests
from lxml import etree

# 目标二：http://111.51.121.242:9001/InDigLib/frontV2/CLCNavigation.action
# 目标三，具体图书信息 http://1.82.133.119:8082/opac/book/900011140?index=1&globalSearchWay=callno&base=q%3De092%26searchType%3Dstandard%26isFacet%3Dfalse%26view%3Dstandard%26searchWay%3Dcallno%26ro%3D10%26sortWay%3Dcallno_sort%26sortOrder%3Dasc%26searchWay0%3Dmarc%26logical0%3DAND%26rows%3D1&searchKeyword=E092

url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"
# url_2 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=2"
# url_3 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=998"
# url_4 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=13"

# real_url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=13"
# real_url_2 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=6954"
# real_url_3 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=16578"

dir = ".\\xmlFiles\\"

# cls = classification?


response  = requests.get(url)

# print(content.text)

print(type(response))

# 所有 XML 文档中的文本均会被解析器解析。 只有 CDATA 区段（CDATA section）中的文本会被解析器忽略。

if response.status_code == 200:
    # 获取响应内容
    content = response.content

    # filename = input( "请输入保存文件的名称：")

    # with open(filename, "wb") as file:
    #     file.write(content)

    root = etree.fromstring(content)

   
    
    # for i in range(len(root.xpath("//id"))):
    #     print(root.xpath("//categoryDesc")[i].text)

    



def getChildId(url):
    
    ids = []

    response  = requests.get(url)
    
    if response.status_code == 200:
        root = etree.fromstring(response.content)

        for i in range(len(root.xpath("//id"))):
            print(root.xpath("//id")[i].text)
            ids.append(root.xpath("//id")[i].text)

    else:
        print("response!=200")
        return "response!=200"

    return ids

getChildId(url)