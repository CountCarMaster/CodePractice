from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error

findImg = re.compile('<a target="_self" class="down".*href="(.*)"></a>')

def askUrl(baseurl):
    headRes = {
        "cookies":"BDqhfp=python%2B%E5%AD%97%E5%85%B8%E9%81%8D%E5%8E%86%26%26NaN-1undefined%26%263968%26%265; BIDUPSID=B84B819D307780DBCA1A34F4F369FBEE; PSTM=1598539597; BDUSS=W9HOHVDVFZwfjI3elVQZllxUi1YUWYyMGdmQWMwQ0t5dmdSbGQzeTFqOWdYSTFnRVFBQUFBJCQAAAAAAQAAAAEAAAA75wMoxMy4x8j9t9bMx3cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGDPZWBgz2VgW; BDUSS_BFESS=W9HOHVDVFZwfjI3elVQZllxUi1YUWYyMGdmQWMwQ0t5dmdSbGQzeTFqOWdYSTFnRVFBQUFBJCQAAAAAAQAAAAEAAAA75wMoxMy4x8j9t9bMx3cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGDPZWBgz2VgW; __yjs_duid=1_92df397d311412d95668de7b663c85091620537264687; BAIDUID=CE51A146870B0D7EEBEDA31797E6F96D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID_BFESS=yI0OJeC62w0omI6HNyHuowf96V5Yx87TH6aoxGnyPf1cFx3RKukmEG0PhU8g0K4bGxQJogKKymOTHrIF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbCq_KLMtCt3fP36q45Eh-FVMfv0etJyaR38aCJvWJ5TMCo6D-nVyjKnXlr7-4Rf5JKq-D5wMIPbShPC-tnWQPC-0MDD5M5OtariLRvE3l02Vbnae-t2yT0VQp7IBtRMW238Wl7mWPozsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjj6jK4JKDNKHJMK; H_PS_PSSID=35703_35105_35732_34584_35490_35700_35246_35796_26350_35746; BAIDUID_BFESS=3A4532E2EC2879C37F95F82F8DAC054A:FG=1; ZD_ENTRY=empty; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22a%22%2C%22%E6%A9%A1%E7%9A%AE%E6%B3%A5%22%2C%22%E5%94%B1%E6%AD%8C%22%2C%22%E6%89%8B%E6%9C%BA%E5%A3%81%E7%BA%B8%20%E6%B5%85%E8%89%B2%22%2C%22%E5%A3%81%E7%BA%B8%22%2C%22%E5%A3%81%E7%BA%B8%20%E5%88%9D%E9%9F%B3%22%2C%22%E5%A3%81%E7%BA%B8%20%E5%8A%A8%E6%BC%AB%22%5D; cleanHistoryStatus=0; ab_sr=1.0.1_MjFjNzA3ZjI4MzNmZmYyZDBiMzZiMGFmYmI3NmYyZjFlOWRmNmJiNGIxMjM5NjUzODE5NmNkMTU3NDJhYWRjNTkwYjJjNzE3NmFlM2RjOTk4MDIyN2RjM2NhZTIyNGQ1ZWZkMjg3YTNmNWQyNjViODU1NTE5YWM1OWFmODM3YTk=",
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
    print(html)
    return html

def getData(url):
    data = []
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    num = 0
    for item in soup.find_all('li', class_="imgitem"):
        link = re.findall(findImg, item)
        data.append(link)
        print(item)
        num += 1
        if num >= 1:
            break
    return data

def main():
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1643188887871_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=a"
    data = getData(url)
    print(data)

if __name__ == '__main__':
    main()