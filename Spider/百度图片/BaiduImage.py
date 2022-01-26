from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error

findImg = re.compile('.*"objURL":"(.*?)".*')

def  baidtu_uncomplie(url):
    res = ''
    c = ['_z2C$q', '_z&e3B', 'AzdH3F']
    d= {'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', '2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', '4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.', 'AzdH3F':'/'}
    if(url==None or 'http' in url):
        return url
    else:
        j= url
        for m in c:
            j=j.replace(m,d[m])
        for char in j:
            if re.match('^[a-w\d]+$',char):
                char = d[char]
            res= res+char
        return res

def askUrl(baseurl):
    headRes = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    request = urllib.request.Request(baseurl, headers=headRes)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData(url):
    data = []
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    link = re.findall(findImg, str(soup))
    return link

def main():
    num = 0
    for ti in range(0, 2):
        # pn是一直在变的
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8413274655075546170&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%88%9D%E9%9F%B3%E6%9C%AA%E6%9D%A5&queryWord=%E5%88%9D%E9%9F%B3%E6%9C%AA%E6%9D%A5&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=" + str(ti * 30) + "&rn=30&gsm=5a&1643200281298="
        data = getData(url)
        for i in data:
            img = baidtu_uncomplie(i).replace("_z&06t;vjB", ".")
            #print(img)
            urllib.request.urlretrieve(img, './SpiImg/%d.jpg'%num)
            num = num + 1

if __name__ == '__main__':
    main()