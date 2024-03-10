from getAny import all

from retrying import retry

# for 武汉城市圈图书馆 using xmlFiles_WH
global path 
path = ".\\xmlFiles_WH\\"

# realUrl = "http://1.82.133.119:8082/opac/browse/query?category=cls&id=0"
realUrl = "http://interlib.library.hb.cn:8008/opac/browse/query?category=cls&id=0"
# 发现开始的initUrl只有域名与端口换了，剩下的一样


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        print("just have a test")
        getAll(realUrl)
    else:
        return "Awesome sauce!"

print(do_something_unreliable())