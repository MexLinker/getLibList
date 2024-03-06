import requests

# 目标二：http://111.51.121.242:9001/InDigLib/frontV2/CLCNavigation.action
# 目标三，具体图书信息 http://1.82.133.119:8082/opac/book/900011140?index=1&globalSearchWay=callno&base=q%3De092%26searchType%3Dstandard%26isFacet%3Dfalse%26view%3Dstandard%26searchWay%3Dcallno%26ro%3D10%26sortWay%3Dcallno_sort%26sortOrder%3Dasc%26searchWay0%3Dmarc%26logical0%3DAND%26rows%3D1&searchKeyword=E092

url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"
url_2 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=2"
url_3 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=998"
url_4 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=13"

real_url = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=13"
real_url_2 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=6954"
real_url_3 = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=16578"



# cls = classification?


content = requests.get(url)

# print(content.text)

print(type(content))

# 所有 XML 文档中的文本均会被解析器解析。 只有 CDATA 区段（CDATA section）中的文本会被解析器忽略。








